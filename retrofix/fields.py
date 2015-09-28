##############################################################################
#
#    Copyright (C) 2013 NaN Projectes de Programari Lliure, S.L.
#                            http://www.NaN-tic.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import sys
try:
    import cdecimal
    # Use cdecimal globally
    if 'decimal' not in sys.modules:
        sys.modules["decimal"] = cdecimal
except ImportError:
    pass
from decimal import Decimal
import re
from datetime import datetime
import banknumber

from .formatting import format_string, format_number
from .exception import RetrofixException

__all__ = ['Field', 'Char', 'Const', 'Account', 'Number', 'Numeric', 'Integer',
    'Date', 'Selection', 'Boolean', 'SIGN_DEFAULT', 'SIGN_12', 'SIGN_N',
    'SIGN_POSITIVE', 'BOOLEAN_01', 'BOOLEAN_12', 'BOOLEAN_X']


class Field(object):
    def __init__(self):
        self._name = None
        self._size = None

    def set_from_file(self, value):
        assert len(value) == self._size, ('Invalid length of field "%s". '
            'Expected "%d" but got "%d".' % (self._name, self._size,
                len(value)))
        return value

    def get_for_file(self, value):
        if value is None:
            value = ''
        return format_string(value, self._size)

    def get(self, value):
        return value

    def set(self, value):
        return value


class Char(Field):
    def __init__(self):
        self._name = None
        self._size = None

    def set(self, value):
        if len(value) > self._size:
            value = value[:self._size]
        return super(Char, self).set(value)


class Const(Char):
    def __init__(self, const):
        super(Const, self).__init__()
        self._const = const

    def set_from_file(self, value):
        assert value == self._const, ('Invalid value "%s" in Const field '
            '"%s". Expected "%s".' % (value, self._name, self._const))
        return super(Const, self).set_from_file(value)

    def get_for_file(self, value):
        return self._const

    def get(self, value):
        return self._const

    def set(self, value):
        assert value == self._const, ('Invalid value for field "%s"'
            % self._name)
        return super(Const, self).set(value)


class Account(Char):
    def __init__(self):
        super(Account, self).__init__()

    def set_from_file(self, value):
        account = value.strip()
        if account and not banknumber.check_code('ES', account):
            raise RetrofixException('Invalid bank account "%s" in field "%s"'
                % (value, self._name))
        return super(Account, self).set_from_file(value)

    def set(self, value):
        account = value
        if account:
            account = account.strip()
        if account and not banknumber.check_code('ES', account):
            raise RetrofixException('Invalid bank account "%s" in field "%s"'
                % (value, self._name))
        return super(Account, self).set(value)


class Number(Char):
    def __init__(self, align='left'):
        super(Number, self).__init__()
        self._align = align

    def set_from_file(self, value):
        assert re.match('[0-9]*$', value), (
            'Non-number value "%s" in field "%s"' % (value, self._name))
        return super(Number, self).set_from_file(value)

    def set(self, value):
        assert re.match('[0-9]*$', value), (
            'Non-number value "%s" in field "%s"' % (value, self._name))

        l = self._size - len(value)
        if self._align == 'right':
            if l:
                value = (l * '0') + value

        return super(Number, self).set(value)


SIGN_DEFAULT = 'default'
SIGN_12 = 'sign_12'
SIGN_N = 'sgin_n'
SIGN_POSITIVE = 'positive'


class Numeric(Field):
    def __init__(self, decimals=2, sign=SIGN_DEFAULT):
        super(Numeric, self).__init__()
        self._decimals = decimals
        self._sign = sign

    def get_sign(self, value):
        if self._sign == SIGN_DEFAULT:
            return '' if value >= Decimal('0.0') else '-'
        if self._sign == SIGN_12:
            return '2' if value >= Decimal('0.0') else '1'
        if self._sign == SIGN_N:
            return '' if value >= Decimal('0.0') else 'N'
        if self._sign == SIGN_POSITIVE:
            assert value >= Decimal('0.0'), ('Field "%s" must be >= 0.0 but '
                'got "%.2f"' % (self._name, value))
            return ''

    def set_from_file(self, value):
        super(Numeric, self).set_from_file(value)
        sign = 1
        if self._sign in (SIGN_12, SIGN_N):
            sign = -1 if value[0] in ('1', 'N') else 1
            value = value[1:]
        num = sign * Decimal('%s.%s' % (value[:-self._decimals],
                value[-self._decimals:]))
        return num

    def get_for_file(self, value):
        if value is None:
            value = Decimal('0')
        sign = self.get_sign(value)
        length = self._size - len(sign)
        assert length > 0, ('Number formatting error. Field size '
            '"%d" but only "%d" characters left for formatting field "%s".') % (
                self._size, length, self._name)
        return sign + format_number(abs(value), length, self._decimals)

    def set(self, value):
        try:
            return Decimal(value)
        except ValueError:
            raise RetrofixException('Invalid value "%s" for Numeric Field "%s"'
                % (value, self._name))


class Integer(Numeric):
    def __init__(self):
        super(Integer, self).__init__(decimals=0)


class Date(Field):
    def __init__(self, pattern):
        super(Date, self).__init__()
        self._pattern = pattern

    def set_from_file(self, value):
        if value == '0' * len(value):
            return
        try:
            return datetime.strptime(value, self._pattern)
        except ValueError:
            raise RetrofixException('Invalid date value "%s" does not '
                    'match pattern "%s" in field "%s"' % (value,
                    self._pattern, self._name))

    def get_for_file(self, value):
        if value is None:
            res = ''
        else:
            res = datetime.strftime(value, self._pattern)
        return super(Date, self).get_for_file(res)

    def set(self, value):
        assert value, datetime
        return super(Date, self).set(value)


class Selection(Char):
    def __init__(self, selection):
        super(Selection, self).__init__()
        self._selection = selection
        self._keys = dict([(x[0], x[1]) for x in selection])
        self._values = dict([(x[1], x[0]) for x in selection])

    def get_for_file(self, value):
        return super(Selection, self).get_for_file(value)

    def set_from_file(self, value):
        assert value in self._keys, ('Value "%s" not found in selection field '
            '"%s". Expected one of: %s' % (value, self._name, self._keys))
        return super(Selection, self).set_from_file(value)

    def set(self, value):
        assert value in self._values, ('Value "%s" not found in selection field '
            '"%s". Expected one of: %s' % (value, self._name, self._values))
        value = self._values[value]
        return super(Selection, self).set(value)


BOOLEAN_01 = {
    True: '1',
    False: '0',
    }

BOOLEAN_12 = {
    True: '1',
    False: '2',
    }

BOOLEAN_X = {
    True: 'X',
    False: ' ',
    }


class Boolean(Field):
    def __init__(self, formatting=None):
        super(Boolean, self).__init__()
        if formatting is None:
            formatting = BOOLEAN_01
        self._formatting = formatting

    def set_from_file(self, value):
        for key, text in self._formatting:
            if value == text:
                return key
        raise RetrofixException('Invalid value "%s" for boolean field "%s"' % (
                value, self._name))

    def get_for_file(self, value):
        return self._formatting[bool(value)]

    def get(self, value):
        return bool(value)

    def set(self, value):
        return super(Boolean, self).set(bool(value))

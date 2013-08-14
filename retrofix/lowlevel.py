# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011-2012 NaN Projectes de Programari Lliure, S.L.
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


try:
    import sys
    import cdecimal
    # Use cdecimal globally
    if 'decimal' not in sys.modules:
        sys.modules["decimal"] = cdecimal
except ImportError:
    pass

from decimal import Decimal
import banknumber

import re
from datetime import datetime

BLANK = ' '

# Record structures:
# * Initial position starting at 1 (instead of 0)
# * Length
# * Field name
# * Field type
# * Field format:
#   * A: Alphanumeric
#   * N: Numeric
#   * D: Date
#   * E: Enumerate
#   * ACCOUNT: Account (20 digit account)

class RetrofixException(BaseException):
    pass

def enum_value_to_text(value, enum):
    for item in enum:
        if item[0] == value:
            return item[1].upper()
    return None

def enum_text_to_value(text, enum):
    for item in enum:
        if item[1].upper() == text.upper():
            return item[0]
    return None


class Record(dict):
    def __init__(self, structure=None):
        """
        Creates a Record object optionally using a structure.

        If structure is defined, only fields defined in the structure
        will be allowed.
        """
        self._structure = structure
        if self._structure:
            self._fields = set([x[2] for x in self._structure])
            # We initialize all fields so we avoid developers
            # to explicitly initialize 'free' fields
            for field in self._fields:
                self[field] = ''
        else:
            self._fields = None

    def __getattr__(self, name):
        if self._structure:
            if not name in self and name in self._fields:
                self[name] = ''
        return self[name]

    def __setattr__(self, name, value):
        if name.startswith('_'):
            return super(Record, self).__setattr__(name, value)
        if self._structure:
            assert name in self._fields, 'Field "%s" does not exist.' % name
        if isinstance(value, (str, unicode)):
            self[name] = value.upper()
        else:
            self[name] = value


# Reading

def extract_record(line, structure, first_position=1):
    record = Record()
    for field in structure:
        assert len(field) >= 4, (
                'Field "%s" does not have the 4 required items' % field)

        start = field[0] - first_position
        end = start + field[1]
        key = field[2]
        ftype = field[3]

        if len(field) > 4:
            options = field[4]
        else:
            options = ''
        stroptions = str(options)

        assert key not in record, 'Duplicate key "%s" in record structure' % key
        value = line[start:end]

        if stroptions.startswith('='):
            match = options[1:]
            assert value == match, 'In field "%s", "%s" != "%s"' % (key,
                    value, match)

        if ftype == 'N':
            assert re.match('[0-9]*$', value), (
                    'Non-numeric value "%s" in field "%s"' % (value, key))
            sign = 1
            if options and options[-1] == '-':
                    if value[0] == '1':
                        sign = -1
                    elif value[0] == '2':
                        sign = 1
                    else:
                        raise RetrofixException('Invalid numeric value "%s". First '
                            'character should be "1" for negative or "2" for '
                            'positive values.')
                    value = value[1:]
            if options and options[0] == '2':
                value = sign * Decimal('%s.%s' % (value[:-2], value[-2:]))
        elif ftype == 'D':
            if value == '0'*len(value):
                value = None
            else:
                try:
                    value = datetime.strptime(value, options)
                except ValueError:
                    raise RetrofixException('Invalid date value "%s" does not '
                            'match pattern "%s" in field "%s"' % (value,
                            options, key))
        elif ftype == 'ACCOUNT':
            if value == ' '*len(value):
                value = None
            else:
                assert banknumber.check_code('ES', value), (
                        'Invalid bank account "%s" in field "%s"' %
                        (value, key))
        elif ftype == 'E':
            value = enum_value_to_text(value.strip(), options)
        else:
            value = value.strip()

        record[key] = value
    return record

def valid_record(line, structure, first_position=1):
    try:
        extract_record(line, structure, first_position=first_position)
        return True
    except (AssertionError, RetrofixException), e:
        return False


# Writing

def format_string(text, length, fill=' ', align='<'):
    """
    Formats the string into a fixed length ASCII (iso-8859-1) record.

    Note:
        'Todos los campos alfanuméricos y alfabéticos se presentarán alineados a la izquierda y
        rellenos de blancos por la derecha, en mayúsculas sin caracteres especiales, y sin vocales acentuadas.
        Para los caracteres específicos del idioma se utilizará la codificación ISO-8859-1. De esta
        forma la letra “Ñ” tendrá el valor ASCII 209 (Hex. D1) y la “Ç”(cedilla mayúscula) el valor ASCII
        199 (Hex. C7).'

    Original code by: Pexego
    """

    if not text:
        return fill*length

    #
    # String uppercase
    #
    text = text.upper()

    #
    # Turn text (probably unicode) into an ASCII (iso-8859-1) string
    #
    if isinstance(text, (unicode)):
        ascii_string = text.encode('iso-8859-1', 'ignore')
    else:
        ascii_string = str(text or '')
    # Cut the string if it is too long
    if len(ascii_string) > length:
        ascii_string = ascii_string[:length]
    # Format the string
    #ascii_string = '{0:{1}{2}{3}s}'.format(ascii_string, fill, align, length) #for python >= 2.6
    if align == '<':
        ascii_string = str(ascii_string) + (length-len(str(ascii_string)))*fill
    elif align == '>':
        ascii_string = (length-len(str(ascii_string)))*fill + str(ascii_string)
    else:
        assert False, 'Wrong aling option. It should be < or >'

    # Sanity-check
    assert len(ascii_string) == length, (
            'The formated string must match the given length')
    # Return string
    return ascii_string


def format_number(number, int_length, dec_length=0, include_sign=False):
    """
    Formats the number into a fixed length ASCII (iso-8859-1) record.
    Note:
        'Todos los campos numéricos se presentarán alineados a la derecha
        y rellenos a ceros por la izquierda sin signos y sin empaquetar.'
        (http://www.boe.es/boe/dias/2008/10/23/pdfs/A42154-42190.pdf)

    :param number: Decimal value
    :param int_length: Number of digits to be used for the integer part
    :param dec_length: Number of digits to be used for the decimal part
    :param include_sign: Wether the sign should be added or not

    Original code by: Pexego
    """

    # TODO: Allow defining how the sign should be shown

    #
    # Separate the number parts (-55.23 => int_part=55, dec_part=0.23, sign='N')
    #
    if number == '':
        number = Decimal('0.0')

    sign = number > 0 and ' ' or 'N'
    number = abs(number)
    int_part = int(number)

    # Format the string
    ascii_string = ''
    if include_sign:
        ascii_string += sign

    if dec_length > 0:
        ascii_string += '%0*.*f' % (int_length+dec_length+1,dec_length, number)
        ascii_string = ascii_string.replace('.','')
    elif int_length > 0:
        ascii_string += '%.*d' % (int_length, int_part)

    assert (len(ascii_string) == (include_sign and 1 or 0) + int_length +
            dec_length), "The formated string must match the given length"

    return ascii_string


def format_boolean(value, yes='X', no=' '):
    """
    Formats a boolean value into a fixed length ASCII (iso-8859-1) record.

    Original code by: Pexego
    """
    return value and yes or no


def write_record(record, first_position=1):
    assert record._structure, 'Record with a structure expected.'

    current_position = 0
    text = ''
    for field in record._structure:
        start = field[0] - first_position
        length = field[1]
        key = field[2]
        ftype = field[3]

        if len(field) > 4:
            options = field[4]
        else:
            options = ''
        stroptions = str(options)

        value = record[key]

        if stroptions.startswith('='):
            match = options[1:]
            if not value:
                value = match
            else:
                assert value == match, 'In field "%s", "%s" != "%s"' % (key,
                    value, match)

        if ftype == 'N':
            if isinstance(value, (Decimal, int)):
                if options and options[0] == '2':
                    minus = 2
                    sign = ''
                    if options[-1] == '-':
                        minus += 1
                        if value >= 0.0:
                            sign = '2'
                        else:
                            sign = '1'
                    value = sign + format_number(value, length - minus, 2)
                elif not options:
                    sign = ''
                    value = sign + format_number(value, length)
                else:
                    raise Exception('Invalid option "%s" o field "%s".' % (
                            options, field))
            else:
                assert re.match('[0-9]*$', value), ('Non-numeric value "%s" in '
                            'field "%s"') % (value, key)
                value = format_string(value, length, fill='0', align='>')
        elif ftype == 'D':
            value = datetime.strftime(value, options)
        elif ftype == 'ACCOUNT':
            assert banknumber.check_code('ES', value)
            value = format_string(value, length)
        elif ftype == 'E':
            value = enum_text_to_value(value, options)
            if value is None:
                raise RetrofixException('Invalid value "%s" for field "%s". Valid '
                        'values are: %s' % (value, key, stroptions))

        else:
            value = format_string(value, length)

        assert len(value) == length, ('Size of record "%s" should be %d but it '
            'is %d (%s)') % (value, length, len(value), str(record))
        assert start >= current_position, 'Start: %d, Current Position: %d' % (
            start, current_position)
        text += BLANK * (start - current_position)
        text += value
        current_position = len(text)

    return text


def write(records):
    data = ''
    for record in records:
        data += write_record(record)
    return data

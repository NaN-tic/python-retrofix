##############################################################################
#
#    Copyright (C) 2011-2013 NaN Projectes de Programari Lliure, S.L.
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


from .fields import Field
from .exception import RetrofixException

BLANK = ' '

# Record structures:
# * Initial position starting at 1 (instead of 0)
# * Length
# * Field name
# * Field type


class Record(object):
    def __init__(self, structure):
        """
        Creates a Record object using a structure.

        Only fields defined in the structure will be allowed.
        """
        self._structure = structure
        self._fields = {}
        self._values = {}
        keys = set()
        for line in self._structure:
            size = line[1]
            name = line[2]
            field = line[3]
            if not isinstance(field, Field):
                field = field()
            field._size = size
            field._name = name
            if name in keys:
                raise AssertionError('Duplicate field name "%s".' % name)
            keys.add(name)
            self._fields[name] = field

    def get_for_file(self, name):
        return self._fields[name].get_for_file(self._values.get(name))

    def set_from_file(self, name, value):
        self._values[name] = self._fields[name].set_from_file(value)

    def __getattr__(self, name):
        if name not in self._fields:
            raise AssertionError('Field "%s" does not exist.' % name)
        return self._fields[name].get(self._values.get(name))

    def __setattr__(self, name, value):
        if name.startswith('_'):
            return super(Record, self).__setattr__(name, value)
        if name not in self._fields:
            raise AssertionError('Field "%s" does not exist.' % name)
        self._values[name] = self._fields[name].set(value)

    def load(self, line, first_position=1):
        for field in self._structure:
            start = field[0] - first_position
            end = start + field[1]
            key = field[2]
            value = line[start:end]
            self.set_from_file(key, value)

    @staticmethod
    def extract(line, structure, first_position=1):
        record = Record(structure)
        record.load(line, first_position=first_position)
        return record

    @staticmethod
    def valid(line, structure, first_position=1):
        record = Record(structure)
        try:
            record.load(line, first_position=first_position)
            return True
        except (AssertionError, RetrofixException):
            return False

    def write(self, first_position=1):
        current_position = 0
        text = ''
        for field in self._structure:
            start = field[0] - first_position
            length = field[1]
            name = field[2]

            value = self.get_for_file(name)

            if len(value) != length:
                raise AssertionError('Field "%s" should be of size "%d" but '
                    'got "%d" on record "%s".' % (name, length, len(value),
                        str(self)))
            if start < current_position:
                raise AssertionError('Error writing field "%s". ' 'Start: %d,'
                    'Current Position: %d' % (name, start, current_position))
            text += BLANK * (start - current_position)
            text += value
            current_position = len(text)
        return text

    def __repr__(self):
        return repr(self._values)

    def __str__(self):
        return str(self._values)

    def __eq__(self, other):
        if self._structure != other._structure:
            return False
        for field in self._fields.keys():
            if self.get_for_file(field) != other.get_for_file(field):
                return False
        return True


def write(records, separator='\r\n'):
    data = ''
    for record in records:
        data += record.write() + separator
    return data

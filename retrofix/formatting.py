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
from decimal import Decimal


def format_string(text, length, fill=' ', align='<'):
    if not text:
        return fill * length
    if isinstance(text, unicode):
        text = text.encode('iso-8859-1', 'ignore')
    else:
        text = str(text or '')
    if len(text) > length:
        text = text[:length]
    text = '{0:{1}{2}{3}s}'.format(text, fill, align, length)
    assert len(text) == length, 'Formatted string must match the given length'
    return text

def format_number(number, size, decimals=0):
    assert number >= Decimal('0.0')
    length = size
    if decimals > 0:
        length += 1
    text = '{0:{1}{2}{3}.{4}f}'.format(number, '0', '>', length, decimals)
    text = text.replace('.', '')
    assert len(text) == size, ('Formatted number "%s" must match the given '
        'length "%d". Got: "%s".' % (number, size, text))
    return text

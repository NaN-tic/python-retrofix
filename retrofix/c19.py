# encoding: utf8
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

from record import Record
from fields import *

# Currency ISO codes:
#
# Dólar australiano    036
# Dólar canadiense     124
# Corona Danesa        208
# Yen japonés          392
# Dólar neozelandés    554
# Corona noruega       578
# Corona sueca         752
# Franco suizo         756
# Libra esterlina      826
# Dólar USA            840
# Euro                 978

PRESENTER_HEADER_RECORD = (
        (  1,  2, 'record_code', Const('51')),
        (  3,  2, 'data_code', Const('80')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Number),
        ( 17,  6, 'creation_date', Date('%d%m%y')),
        ( 23,  6, 'free', Char),
        ( 29, 40, 'name', Char),
        ( 69, 20, 'free_1', Char),
        ( 89,  4, 'bank_code', Number),
        ( 93,  4, 'bank_office', Number),
        ( 97, 12, 'free_2', Char),
        (109, 40, 'free_3', Char),
        (149, 14, 'free_4', Char),
        )

ORDERING_HEADER_RECORD = (
        (  1,  2, 'record_code', Const('53')),
        (  3,  2, 'data_code', Const('80')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Number),
        ( 17,  6, 'creation_date', Date('%d%m%y')),
        ( 23,  6, 'payment_date', Date('%d%m%y')),
        ( 29, 40, 'name', Char),
        ( 69, 20, 'account', Account),
        ( 89,  8, 'free_1', Char),
        ( 97,  2, 'procedure', Char), # Type?
        ( 99, 10, 'free_2', Char),
        (109, 40, 'free_3', Char),
        (149, 14, 'free_4', Char),
        )

REQUIRED_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', Const('56')),
        (  3,  2, 'data_code', Const('80')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Number),
        ( 17, 12, 'reference_code', Char),
        ( 29, 40, 'name', Char),
        ( 69, 20, 'account', Account),
        ( 89, 10, 'amount', Numeric(sign=SIGN_POSITIVE)),
        ( 99, 16, 'free_1', Char),
        (115, 40, 'concept', Char),
        (155,  8, 'free_2', Char)
        )

FIRST_OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', Const('56')),
        (  3,  2, 'data_code', Const('81')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Char),
        ( 17, 12, 'reference_code', Char),
        ( 29, 40, 'second_field_concept', Char),
        ( 69, 40, 'third_field_concept', Char),
        (109, 40, 'fourth_field_concept', Char),
        (149, 14, 'free', Char),
        )  # Annex 2. CSB 19 Norm.

SECOND_OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', Const('56')),
        (  3,  2, 'data_code', Const('82')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Char),
        ( 17, 12, 'reference_code', Char),
        ( 29, 40, 'fifth_field_concept', Char),
        ( 69, 40, 'sixth_field_concept', Char),
        (109, 40, 'seventh_field_concept', Char),
        (149, 14, 'free', Char),
        )  # Annex 2. CSB 19 Norm.

THIRD_OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', Const('56')),
        (  3,  2, 'data_code', Const('83')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Char),
        ( 17, 12, 'reference_code', Char),
        ( 29, 40, 'eighth_field_concept', Char),
        ( 69, 40, 'ninth_field_concept', Char),
        (109, 40, 'tenth_field_concept', Char),
        (149, 14, 'free', Char),
        )  # Annex 2. CSB 19 Norm.

FOURTH_OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', Const('56')),
        (  3,  2, 'data_code', Const('84')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Char),
        ( 17, 12, 'reference_code', Char),
        ( 29, 40, 'eleventh_field_concept', Char),
        ( 69, 40, 'twelfth_field_concept', Char),
        (109, 40, 'thirteenth_field_concept', Char),
        (149, 14, 'free', Char),
        )  # Annex 2. CSB 19 Norm.

FIFTH_OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', Const('56')),
        (  3,  2, 'data_code', Const('85')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Char),
        ( 17, 12, 'reference_code', Char),
        ( 29, 40, 'fourteenth_field_concept', Char),
        ( 69, 40, 'fifteenth_field_concept', Char),
        (109, 40, 'sixteenth_field_concept', Char),
        (149, 14, 'free', Char),
        )  # Annex 2. CSB 19 Norm.

SIXTH_OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', Const('56')),
        (  3,  2, 'data_code', Const('86')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Char),
        ( 17, 12, 'reference_code', Char),
        ( 29, 40, 'name', Char),
        ( 69, 40, 'address', Char),
        (109, 35, 'city', Char),
        (144,  5, 'zip', Char),
        (149, 14, 'free', Char),
        )  # Annex 2. CSB 19 Norm.

OPTIONAL_RECORD = SIXTH_OPTIONAL_INDIVIDUAL_RECORD  # Annex 3. CSB 19 Norm.

ORDERING_FOOTER_RECORD = (
        (  1,  2, 'record_code', Const('58')),
        (  3,  2, 'data_code', Const('80')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Number),
        ( 17, 12, 'free_1', Char),
        ( 29, 40, 'free_2', Char),
        ( 69, 20, 'free_3', Char),
	# Suma de los importes del ordenante
        ( 89, 10, 'amount_sum', Numeric(sign=SIGN_POSITIVE)),
        ( 99,  6, 'free_4', Char),
 	# Número de domiciliaciones del ordenante
        (105, 10, 'required_count', Integer),
	# Número total de registros del ordenante
        (115, 10, 'record_count', Integer),
        (125, 20, 'free_5', Char),
        (145, 18, 'free_6', Char),
        )

PRESENTER_FOOTER_RECORD = (
        (  1,  2, 'record_code', Const('59')),
        (  3,  2, 'data_code', Const('80')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Number),
        ( 17, 12, 'free_1', Char),
        ( 29, 40, 'free_2', Char),
	# Número de ordenantes
        ( 69,  4, 'ordering_count', Integer),
        ( 73, 16, 'free_3', Char),
	# Suma total de importes
        ( 89, 10, 'amount_sum', Numeric(sign=SIGN_POSITIVE)),
        ( 99,  6, 'free_4', Char),
	# Número total de domiciliaciones
        (105, 10, 'required_count', Integer),
	# Número total de registros del soporte
        (115, 10, 'record_count', Integer),
        (125, 20, 'free_5', Char),
        (145, 18, 'free_6', Char),
        )

# Structure:
# Depth
#c19_file_structure = (
#    PRESENTER_HEADER_RECORD,
#    ORDERING_HEADER_RECORD,
#    REQUIRED_INDIVIDUAL_RECORD,
#    OPTIONAL_RECORD
#    ORDERING_FOOTER_RECORD
#    PRESENTER_FOOTER_RECORD,
#)


def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, PRESENTER_HEADER_RECORD))

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, ORDERING_HEADER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if Record.valid(current_line, REQUIRED_INDIVIDUAL_RECORD):
            record = Record.extract(current_line, REQUIRED_INDIVIDUAL_RECORD)
        elif Record.valid(current_line, OPTIONAL_RECORD):
            record = Record.extract(current_line, OPTIONAL_RECORD)
        elif Record.valid(current_line, ORDERING_FOOTER_RECORD):
            record = Record.extract(current_line, ORDERING_FOOTER_RECORD)
        elif Record.valid(current_line, PRESENTER_FOOTER_RECORD):
            record = Record.extract(current_line, PRESENTER_FOOTER_RECORD)
        else:
            raise Exception('Invalid record: %s' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records

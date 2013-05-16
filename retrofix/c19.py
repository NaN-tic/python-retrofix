# encoding: utf8
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

from lowlevel import extract_record, valid_record

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

# See lowlevel.py for record structures

PRESENTER_HEADER_RECORD = (
        (  1,  2, 'record_code', 'N', '=51'), # 00
        (  3,  2, 'data_code', 'N', '=80'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'N'),
        ( 17,  6, 'creation_date', 'D', '%d%m%y'),
        ( 23,  6, 'free', 'A'),
        ( 29, 40, 'name', 'A'),
        ( 69, 20, 'free_1', 'A'),
        ( 89,  4, 'bank_code', 'N'),
        ( 93,  4, 'bank_office', 'N'),
        ( 97, 12, 'free_2', 'A'),
        (109, 40, 'free_3', 'A'),
        (149, 14, 'free_4', 'A'),
        )

ORDERING_HEADER_RECORD = (
        (  1,  2, 'record_code', 'N', '=53'),
        (  3,  2, 'data_code', 'N', '=80'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'N'),
        ( 17,  6, 'creation_date', 'D', '%d%m%y'),
        ( 23,  6, 'payment_date', 'D', '%d%m%y'),
        ( 29, 40, 'name', 'A'),
        ( 69, 20, 'account', 'ACCOUNT'), # Complete account number
        ( 89,  8, 'free_1', 'A'),
        ( 97,  2, 'procedure', 'A'), # Type?
        ( 99, 10, 'free_2', 'A'),
        (109, 40, 'free_3', 'A'),
        (149, 14, 'free_4', 'A'),
        )

REQUIRED_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', 'N', '=56'),
        (  3,  2, 'data_code', 'N', '=80'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'N'),
        ( 17, 12, 'reference_code', 'A'),
        ( 29, 40, 'name', 'A'),
        ( 69, 20, 'account', 'ACCOUNT'),
        ( 89, 10, 'amount', 'N', '2'),
        ( 99, 16, 'free_1', 'A'),
        (115, 40, 'concept', 'A'),
        (155,  8, 'free_2', 'A')
        )

FIRST_OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', 'N', '=56'),
        (  3,  2, 'data_code', 'N', '=81'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'A'),
        ( 17, 12, 'reference_code', 'A'),
        ( 29, 40, 'second_field_concept', 'A'),
        ( 69, 40, 'third_field_concept', 'A'),
        (109, 40, 'fourth_field_concept', 'A'),
        (149, 14, 'free', 'A'),
        )  # Annex 2. CSB 19 Norm.

SECOND_OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', 'N', '=56'),
        (  3,  2, 'data_code', 'N', '=82'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'A'),
        ( 17, 12, 'reference_code', 'A'),
        ( 29, 40, 'fifth_field_concept', 'A'),
        ( 69, 40, 'sixth_field_concept', 'A'),
        (109, 40, 'seventh_field_concept', 'A'),
        (149, 14, 'free', 'A'),
        )  # Annex 2. CSB 19 Norm.

THIRD_OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', 'N', '=56'),
        (  3,  2, 'data_code', 'N', '=83'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'A'),
        ( 17, 12, 'reference_code', 'A'),
        ( 29, 40, 'eighth_field_concept', 'A'),
        ( 69, 40, 'ninth_field_concept', 'A'),
        (109, 40, 'tenth_field_concept', 'A'),
        (149, 14, 'free', 'A'),
        )  # Annex 2. CSB 19 Norm.

FOURTH_OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', 'N', '=56'),
        (  3,  2, 'data_code', 'N', '=84'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'A'),
        ( 17, 12, 'reference_code', 'A'),
        ( 29, 40, 'eleventh_field_concept', 'A'),
        ( 69, 40, 'twelfth_field_concept', 'A'),
        (109, 40, 'thirteenth_field_concept', 'A'),
        (149, 14, 'free', 'A'),
        )  # Annex 2. CSB 19 Norm.

FIFTH_OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', 'N', '=56'),
        (  3,  2, 'data_code', 'N', '=85'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'A'),
        ( 17, 12, 'reference_code', 'A'),
        ( 29, 40, 'fourteenth_field_concept', 'A'),
        ( 69, 40, 'fifteenth_field_concept', 'A'),
        (109, 40, 'sixteenth_field_concept', 'A'),
        (149, 14, 'free', 'A'),
        )  # Annex 2. CSB 19 Norm.

SIXTH_OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', 'N', '=56'),
        (  3,  2, 'data_code', 'N', '=86'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'A'),
        ( 17, 12, 'reference_code', 'A'),
        ( 29, 40, 'name', 'A'),
        ( 69, 40, 'address', 'A'),
        (109, 35, 'city', 'A'),
        (144,  5, 'zip', 'A'),
        (149, 14, 'free', 'A'),
        )  # Annex 2. CSB 19 Norm.

OPTIONAL_RECORD = SIXTH_OPTIONAL_INDIVIDUAL_RECORD  # Annex 3. CSB 19 Norm.

ORDERING_FOOTER_RECORD = (
        (  1,  2, 'record_code', 'N', '=58'),
        (  3,  2, 'data_code', 'N', '=80'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'N'),
        ( 17, 12, 'free_1', 'A'),
        ( 29, 40, 'free_2', 'A'),
        ( 69, 20, 'free_3', 'A'),
        ( 89, 10, 'amount_sum', 'N', '2'), # Suma de los importes del ordenante
        ( 99,  6, 'free_4', 'A'),
        (105, 10, 'required_count', 'N'), # Número de domiciliaciones del ordenante
        (115, 10, 'record_count', 'N'), # Número total de registros del ordenante
        (125, 20, 'free_5', 'A'),
        (145, 18, 'free_6', 'A'),
        )

PRESENTER_FOOTER_RECORD = (
        (  1,  2, 'record_code', 'N', '=59'),
        (  3,  2, 'data_code', 'N', '=80'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'N'),
        ( 17, 12, 'free_1', 'A'),
        ( 29, 40, 'free_2', 'A'),
        ( 69,  4, 'ordering_count', 'N'), # Número de ordenantes
        ( 73, 16, 'free_3', 'A'),
        ( 89, 10, 'amount_sum', 'N', '2'), # Suma total de importes
        ( 99,  6, 'free_4', 'A'),
        (105, 10, 'required_count', 'N'), # Número total de domiciliaciones
        (115, 10, 'record_count', 'N'), # Número total de registros del soporte
        (125, 20, 'free_5', 'A'),
        (145, 18, 'free_6', 'A'),
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


def write(records):
    pass

def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(extract_record(current_line, PRESENTER_HEADER_RECORD))

    current_line = lines.pop(0)
    records.append(extract_record(current_line, ORDERING_HEADER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if valid_record(current_line, REQUIRED_INDIVIDUAL_RECORD):
            record = extract_record(current_line, REQUIRED_INDIVIDUAL_RECORD)
        elif valid_record(current_line, OPTIONAL_RECORD):
            record = extract_record(current_line, OPTIONAL_RECORD)
        elif valid_record(current_line, ORDERING_FOOTER_RECORD):
            record = extract_record(current_line, ORDERING_FOOTER_RECORD)
        elif valid_record(current_line, PRESENTER_FOOTER_RECORD):
            record = extract_record(current_line, PRESENTER_FOOTER_RECORD)
        else:
            raise Exception('Invalid record: %s' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records

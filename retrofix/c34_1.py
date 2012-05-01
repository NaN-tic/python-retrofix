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

# See lowlevel.py for record structures

ORDERING_HEADER_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=62'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'N', '=001'),
        (32,  6, 'send_date', 'D', '%d%m%y'),
        (38,  6, 'creation_date', 'D', '%d%m%y'),
        (44, 20, 'account', 'ACCOUNT'), # Complete account number
        (64,  1, 'charge_detail', 'A'),
        (65,  8, 'free_2', 'A'),
        )

ORDERING_HEADER_002_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'N', '=002'),
        (32, 36, 'name', 'A'),
        (68,  5, 'free_2', 'A'),
        )

ORDERING_HEADER_003_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'N', '=003'),
        (32, 36, 'address', 'A'),
        (68,  5, 'free_2', 'A'),
        )

ORDERING_HEADER_004_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'N', '=004'),
        (32, 36, 'city', 'A'),
        (68,  5, 'free_2', 'A'),
        )

ORDERING_HEADER_005_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'N', '=007'),
        (32, 36, 'zone', 'A'),
        (68,  5, 'free_2', 'A'),
        )

ORDERING_HEADER_006_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'N', '=008'),
        (32, 36, 'address', 'A'),
        (68,  5, 'free_2', 'A'),
        )

# Structure:
# Depth
#c34_file_structure = (
#    FIRST_RECORD
#)


def read(data):
    lines = data.splitlines()
    line_count = len(lines)

    current_line = lines.pop(0)
    if valid_record(current_line, FILE_HEADER_RECORD):
        current_line = lines.pop(0)

    records = []
    if not valid_record(current_line, ACCOUNT_HEADER_RECORD):
        assert False, 'Expected account header record at line %d' % (line_count - len(lines))

    record = extract_record(current_line, ACCOUNT_HEADER_RECORD)
    records.append(record)
    current_line = lines.pop(0)
    while lines:
        if valid_record(current_line, MOVE_RECORD):
            record = extract_record(current_line, MOVE_RECORD)
        elif valid_record(current_line, MOVE_CONCEPT_RECORD):
            record = extract_record(current_line, MOVE_CONCEPT_RECORD)
        elif valid_record(current_line, MOVE_AMOUNT_EQUIVALENCE_RECORD):
            record = extract_record(current_line, MOVE_AMOUNT_EQUIVALENCE_RECORD)
        elif valid_record(current_line, ACCOUNT_FOOTER_RECORD):
            record = extract_record(current_line, ACCOUNT_FOOTER_RECORD)
            records.append(record)
            break
        else:
            record = extract_record(current_line, MOVE_RECORD)
            assert False, 'Invalid data at line %d' % (line_count - len(lines))
        records.append(record)
        current_line = lines.pop(0)

    return records

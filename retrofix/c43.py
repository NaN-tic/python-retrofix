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

FILE_HEADER_RECORD = (
    ( 1,  2, 'record_code', 'N', '=00'), # 00
    ( 3,  4, 'bank_code', 'N'),
    ( 7,  6, 'date', 'N'),
    (13, 68, 'free', 'A'),
)

ACCOUNT_HEADER_RECORD = (
    ( 1,  2, 'record_code', 'N', '=11'), # 11
    ( 3,  4, 'bank_code', 'N'),
    ( 7,  4, 'bank_office', 'N'),
    (11, 10, 'account_number', 'N'),
    (21,  6, 'start_date', 'D', '%y%m%d'),
    (27,  6, 'end_date', 'D', '%y%m%d'),
    (33,  1, 'initial_balance_sign', 'N'),
    (34, 14, 'initial_balance', 'N', '2'),
    (48,  3, 'currency_code', 'N'),
    (51,  1, 'information_mode', 'N'),
    (52, 26, 'customer_name', 'A'),
    (78,  3, 'free', 'A'), # customer_code
)

MOVE_RECORD = (
    ( 1,  2, 'record_code', 'N', '=22'), # 22
    ( 3,  4, 'free', 'A'), # With space. Exceptionally will show bank code
    ( 7,  4, 'bank_office', 'N'),
    (11,  6, 'operation_date', 'D', '%y%m%d'),
    (17,  6, 'value_date', 'D', '%y%m%d'),
    (23,  2, 'common_concept_code', 'N'),
    (25,  3, 'bank_concept_code', 'N'), # Bank's own concept code
    (28,  1, 'amount_sign', 'N'), # 1=debit, 2=credit
    (29, 14, 'amount', 'N', '2'), # No decimal separator with 2 decimal places
    (43, 10, 'document_number', 'N'),
    (53, 12, 'reference_1', 'A'),
    (65, 16, 'reference_2', 'A'),
)

MOVE_CONCEPT_RECORD = (
    ( 1,  2, 'record_code', 'N', '=23'),
    ( 3,  2, 'data_code', 'N'),
    ( 5, 38, 'concept_1', 'A'),
    (43, 38, 'concept_2', 'A'),
)

MOVE_AMOUNT_EQUIVALENCE_RECORD = (
    ( 1,  2, 'record_code', 'N', '=24'), # Unknown
    ( 3,  2, 'data_code', 'N'), 
    ( 5,  3, 'source_currency_code', 'N'), 
    ( 8, 14, 'amount', 'N'), 
    (22, 59, 'free', 'A'), 
)

ACCOUNT_FOOTER_RECORD = (
    ( 1,  2, 'record_code', 'N', '=33'), # 33
    ( 3,  4, 'bank_code', 'N'),
    ( 7,  4, 'bank_office', 'N'),
    (11, 10, 'account_number', 'N'),
    (21,  5, 'debit_record_count', 'N'),
    (26, 14, 'debit_total', 'N', '2'),
    (40,  5, 'credit_record_count', 'N'),
    (45,  5, 'credit_total', 'N', '2'),
    (59,  1, 'final_balance_sign', 'N'), # 1 = Debit, 2 = Credit
    (60, 14, 'final_balance', 'N', '2'),
    (74,  3, 'currency_code', 'N'),
    (77,  4, 'free', 'A'),
)

FILE_FOOTER_RECORD = (
    ( 1,  2, 'record_code', 'N', '=88'), # 88
    ( 3, 18, 'nines', 'N'), # Filled with '9'*18
    (21,  6, 'record_count', 'N'), # Number of records in the file excluding itself and FILE_HEADER_RECORD (00).
    (27, 54, 'free', 'A'),
)

# Structure:
# Depth
#c43_file_structure = (
    #FILE_HEADER_RECORD,
    #ACCOUNT_HEADER_RECORD
    #MOVE_RECORD,
    #MOVE_CONCEPT_RECORD,
    #MOVE_AMOUNT_EQUIVALENCE_RECORD,
    #ACCOUNT_FOOTER_RECORD,
    #FILE_FOOTER_RECORD,
#)

def read(data):
    lines = data.splitlines()
    line_count = len(lines)

    current_line = lines.pop(0)
    if valid_record(current_line, FILE_HEADER_RECORD):
        current_line = lines.pop(0)

    records = []
    if not valid_record(current_line, ACCOUNT_HEADER_RECORD):
        raise BaseException('Expected account header record at line %d' % 
            (line_count - len(lines)))

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
            raise BaseException('Invalid data at line %d' % 
                (line_count - len(lines)))
        records.append(record)
        current_line = lines.pop(0)

    return records

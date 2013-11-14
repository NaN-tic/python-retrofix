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
from .fields import *

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

FILE_HEADER_RECORD = (
    ( 1,  2, 'record_code', Const('00')),
    ( 3,  4, 'bank_code', Number),
    ( 7,  6, 'date', Date('%y%m%d')),
    (13, 68, 'free', Char),
    )

ACCOUNT_HEADER_RECORD = (
    ( 1,  2, 'record_code', Const('11')),
    ( 3,  4, 'bank_code', Number),
    ( 7,  4, 'bank_office', Number),
    (11, 10, 'account_number', Number),
    (21,  6, 'start_date', Date('%y%m%d')),
    (27,  6, 'end_date', Date('%y%m%d')),
    (33, 15, 'initial_balance', Numeric(sign=SIGN_12)),
    (48,  3, 'currency_code', Number),
    (51,  1, 'information_mode', Number),
    (52, 26, 'customer_name', Char),
    (78,  3, 'free', Char), # customer_code
    )

MOVE_RECORD = (
    ( 1,  2, 'record_code', Const('22')),
    ( 3,  4, 'free', Char), # With space. Exceptionally will show bank code
    ( 7,  4, 'bank_office', Number),
    (11,  6, 'operation_date', Date('%y%m%d')),
    (17,  6, 'value_date', Date('%y%m%d')),
    (23,  2, 'common_concept_code', Number),
    (25,  3, 'bank_concept_code', Number), # Bank's own concept code
    (28, 15, 'amount', Numeric(sign=SIGN_12)),
    (43, 10, 'document_number', Number),
    (53, 12, 'reference_1', Char),
    (65, 16, 'reference_2', Char),
)

MOVE_CONCEPT_RECORD = (
    ( 1,  2, 'record_code', Const('23')),
    ( 3,  2, 'data_code', Number),
    ( 5, 38, 'concept_1', Char),
    (43, 38, 'concept_2', Char),
)

MOVE_AMOUNT_EQUIVALENCE_RECORD = (
    ( 1,  2, 'record_code', Const('24')), # Unknown
    ( 3,  2, 'data_code', Number),
    ( 5,  3, 'source_currency_code', Number),
    ( 8, 14, 'amount', Numeric),
    (22, 59, 'free', Char),
)

ACCOUNT_FOOTER_RECORD = (
    ( 1,  2, 'record_code', Const('33')),
    ( 3,  4, 'bank_code', Number),
    ( 7,  4, 'bank_office', Number),
    (11, 10, 'account_number', Number),
    (21,  5, 'debit_record_count', Integer),
    (26, 14, 'debit_total', Numeric),
    (40,  5, 'credit_record_count', Integer),
    (45, 14, 'credit_total', Numeric),
    (59, 15, 'final_balance', Numeric(sign=SIGN_12)),
    (74,  3, 'currency_code', Number),
    (77,  4, 'free', Char),
)

FILE_FOOTER_RECORD = (
    ( 1,  2, 'record_code', Const('88')),
    ( 3, 18, 'nines', Number), # Filled with '9'*18
    # Number of records in the file excluding itself and FILE_HEADER_RECORD (00).
    (21,  6, 'record_count', Integer),
    (27, 54, 'free', Char),
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
    if Record.valid(current_line, FILE_HEADER_RECORD):
        current_line = lines.pop(0)

    records = []
    if not Record.valid(current_line, ACCOUNT_HEADER_RECORD):
        raise BaseException('Expected account header record at line %d' %
            (line_count - len(lines)))

    record = Record.extract(current_line, ACCOUNT_HEADER_RECORD)
    records.append(record)
    current_line = lines.pop(0)
    while lines:
        if Record.valid(current_line, MOVE_RECORD):
            record = Record.extract(current_line, MOVE_RECORD)
        elif Record.valid(current_line, MOVE_CONCEPT_RECORD):
            record = Record.extract(current_line, MOVE_CONCEPT_RECORD)
        elif Record.valid(current_line, MOVE_AMOUNT_EQUIVALENCE_RECORD):
            record = Record.extract(current_line, MOVE_AMOUNT_EQUIVALENCE_RECORD)
        elif Record.valid(current_line, ACCOUNT_FOOTER_RECORD):
            record = Record.extract(current_line, ACCOUNT_FOOTER_RECORD)
            records.append(record)
            break
        else:
            raise BaseException('Invalid data at line %d' %
                (line_count - len(lines)))
        records.append(record)
        current_line = lines.pop(0)

    return records

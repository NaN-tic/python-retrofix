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
        ( 3,  2, 'data_code', 'N', '=62'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'N', '=001'),
        (32,  6, 'send_date', 'D', '%d%m%y'),
        (38,  6, 'creation_date', 'D', '%d%m%y'),
        (44, 20, 'account', 'ACCOUNT'),
        (64,  1, 'charge_detail', 'E', (
                ('0', 'false'),
                ('1', 'true')
                )),
        (65,  8, 'free_2', 'A'),
        )

ORDERING_HEADER_002_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  2, 'data_code', 'N', '=62'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'N', '=002'),
        (32, 36, 'name', 'A'),
        (68,  5, 'free_2', 'A'),
        )

ORDERING_HEADER_003_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  2, 'data_code', 'N', '=62'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'N', '=003'),
        (32, 36, 'address', 'A'),
        (68,  5, 'free_2', 'A'),
        )

ORDERING_HEADER_004_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  2, 'data_code', 'N', '=62'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'N', '=004'),
        (32,  6, 'zip', 'A'),
        (38, 30, 'city', 'A'),
        (68,  5, 'free_2', 'A'),
        )

NATIONAL_HEADER_RECORD = (
        ( 1,  2, 'record_code', 'N', '=04'), # 00
        ( 3,  2, 'data_code', 'N', '=56'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'A', '=   '),
        (32, 36, 'data', 'A'),
        (68,  5, 'free_2', 'A'),
        )

#'transfer': '56',
#'cheques': '57',
#'promissory_note': '58',
#'certified_payments': '59',

NATIONAL_TRANSFER_RECORD = (
        ( 1,  2, 'record_code', 'N', '=06'), # 00
        ( 3,  2, 'data_code', 'N', '=56'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'N', '=010'),
        (32, 12, 'amount', 'N', '2'),
        (44, 20, 'account', 'ACCOUNT'),
        (64,  1, 'cost', 'E', (
                ('1', 'payer'),
                ('2', 'recipient'),
                )),
        (65,  1, 'concept', 'E', (
                ('1', 'payroll'),
                ('8', 'pension'),
                ('9', 'other'),
                )),
        (66,  1, 'direct_payment', 'E', (
                ('1', 'true'),
                ('2', 'false'),
                )),
        (67,  6, 'free_2', 'A'),
        )

DETAIL_002_RECORD = (
        ( 1,  2, 'record_code', 'N', '=06'), # 00
        ( 3,  2, 'data_code', 'E', (
                ('56', 'transfer'),
                ('57', 'cheque'),
                ('58', 'promissory_note'),
                ('59', 'certified_payments'),
                )),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'recipient_nif', 'A'),
        (29,  3, 'data_number', 'N', '=011'),
        (32, 36, 'name', 'A'),
        (68,  5, 'free_1', 'A'),
        )

DETAIL_003_RECORD = (
        ( 1,  2, 'record_code', 'N', '=06'), # 00
        ( 3,  2, 'data_code', 'E', (
                ('56', 'transfer'),
                ('57', 'cheque'),
                ('58', 'promissory_note'),
                ('59', 'certified_payments'),
                )),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'recipient_nif', 'A'),
        (29,  3, 'data_number', 'N', '=012'),
        (32, 36, 'street', 'A'),
        (68,  5, 'free_1', 'A'),
        )

DETAIL_004_RECORD = (
        ( 1,  2, 'record_code', 'N', '=06'), # 00
        ( 3,  2, 'data_code', 'E', (
                ('56', 'transfer'),
                ('57', 'cheque'),
                ('58', 'promissory_note'),
                ('59', 'certified_payments'),
                )),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'recipient_nif', 'A'),
        (29,  3, 'data_number', 'N', '=013'),
        (32, 36, 'street2', 'A'),
        (68,  5, 'free_1', 'A'),
        )

DETAIL_005_RECORD = (
        ( 1,  2, 'record_code', 'N', '=06'), # 00
        ( 3,  2, 'data_code', 'E', (
                ('56', 'transfer'),
                ('57', 'cheque'),
                ('58', 'promissory_note'),
                ('59', 'certified_payments'),
                )),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'recipient_nif', 'A'),
        (29,  3, 'data_number', 'N', '=014'),
        (32,  6, 'zip', 'A'),
        (38, 30, 'city', 'A'),
        (68,  5, 'free_1', 'A'),
        )

DETAIL_006_RECORD = (
        ( 1,  2, 'record_code', 'N', '=06'), # 00
        ( 3,  2, 'data_code', 'E', (
                ('56', 'transfer'),
                ('57', 'cheque'),
                ('58', 'promissory_note'),
                ('59', 'certified_payments'),
                )),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'recipient_nif', 'A'),
        (29,  3, 'data_number', 'N', '=015'),
        (32,  2, 'country_code', 'A'),
        (34, 34, 'state', 'A'),
        (68,  5, 'free_1', 'A'),
        )

# Only for payrolls
# Only for cheques, promissory notes and certified payments
DETAIL_007_RECORD = ( 
        ( 1,  2, 'record_code', 'N', '=06'), # 00
        ( 3,  2, 'data_code', 'E', (
                ('57', 'cheque'),
                ('58', 'promissory_note'),
                ('59', 'certified_payments'),
                )),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'recipient_nif', 'A'),
        (29,  3, 'data_number', 'N', '=018'),
        (32, 36, 'beneficiary_nif', 'A'), # The same as recipient_nif
        (68,  5, 'free_1', 'A'),
        )

DETAIL_101_RECORD = ( 
        ( 1,  2, 'record_code', 'N', '=06'), # 00
        ( 3,  2, 'data_code', 'E', (
                ('57', 'cheque'),
                ('58', 'promissory_note'),
                ('59', 'certified_payments'),
                )),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'recipient_nif', 'A'),
        (29,  3, 'data_number', 'N', '=101'),
        (32, 36, 'message', 'A'), # Letter message
        (68,  5, 'free_1', 'A'),
        )

DETAIL_102_RECORD = ( 
        ( 1,  2, 'record_code', 'N', '=06'), # 00
        ( 3,  2, 'data_code', 'E', (
                ('57', 'cheque'),
                ('58', 'promissory_note'),
                ('59', 'certified_payments'),
                )),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'recipient_nif', 'A'),
        (29,  3, 'data_number', 'N', '=102'),
        (32, 36, 'message', 'A'), # Letter message
        (68,  5, 'free_1', 'A'),
        )

DETAIL_103_RECORD = ( 
        ( 1,  2, 'record_code', 'N', '=06'), # 00
        ( 3,  2, 'data_code', 'E', (
                ('57', 'cheque'),
                ('58', 'promissory_note'),
                ('59', 'certified_payments'),
                )),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'recipient_nif', 'A'),
        (29,  3, 'data_number', 'N', '=103'),
        (32, 36, 'message', 'A'), # Letter message
        (68,  5, 'free_1', 'A'),
        )

DETAIL_910_RECORD = ( 
        ( 1,  2, 'record_code', 'N', '=06'), # 00
        ( 3,  2, 'data_code', 'E', (
                ('57', 'cheque'),
                ('58', 'promissory_note'),
                ('59', 'certified_payments'),
                )),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'recipient_nif', 'A'),
        (29,  3, 'data_number', 'N', '=910'),
        (32, 36, 'message', 'A'), # Usually contains the date
        (68,  5, 'free_1', 'A'),
        )

NATIONAL_FOOTER_RECORD = (
        ( 1,  2, 'record_code', 'N', '=08'), # 00
        ( 3,  2, 'data_code', 'N', '=56'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'A', '=   '),
        (32, 12, 'amount', 'N', '2'),
        (44,  8, 'payment_line_count', 'N'),
        (52, 10, 'record_count', 'N'),
        (62,  6, 'free_2', 'A'),
        (68,  5, 'free_3', 'A'),
        )

ORDERING_FOOTER_RECORD = (
        ( 1,  2, 'record_code', 'N', '=09'), # 00
        ( 3,  2, 'data_code', 'N', '=62'),
        ( 5,  9, 'nif', 'A'),
        (14,  3, 'suffix', 'N'),
        (17, 12, 'free_1', 'A'),
        (29,  3, 'data_number', 'A', '=   '),
        (32, 12, 'amount', 'N', '2'),
        (44,  8, 'payment_line_count', 'N'),
        (64, 10, 'record_count', 'N'),
        (74,  6, 'free_2', 'A'),
        (80,  5, 'free_3', 'A'),
        )

def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(extract_record(current_line, ORDERING_HEADER_RECORD))

# Por cada registro de Transferencias o Nóminas se constituirán obligatoriamente
# los registros tipo de Dato 010, 011, 012, 014 y, opcionalmente, el 013, 016 y
# 017.

# Por cada registro de Cheques Bancarios, Pagarés o Pagos Certificados se
# constituirán obligatoriamente los registros tipos de Dato 010, 011 y,
# opcionalmente, 012, 013, 014, 015, 016, 017 y 018. Los registros tipo de Dato
# 012, 013, 014 y 015 serán obligatorios para emisiones con carta.


    current_line = lines.pop(0)
    while lines:
        if valid_record(current_line, ORDERING_HEADER_002_RECORD):
            record = extract_record(current_line, ORDERING_HEADER_002_RECORD)
        elif valid_record(current_line, ORDERING_HEADER_003_RECORD):
            record = extract_record(current_line, ORDERING_HEADER_003_RECORD)
        elif valid_record(current_line, ORDERING_HEADER_004_RECORD):
            record = extract_record(current_line, ORDERING_HEADER_004_RECORD)
        elif valid_record(current_line, NATIONAL_HEADER_RECORD):
            record = extract_record(current_line, NATIONAL_HEADER_RECORD)
        elif valid_record(current_line, NATIONAL_TRANSFER_RECORD):
            record = extract_record(current_line, NATIONAL_TRANSFER_RECORD)
        elif valid_record(current_line, DETAIL_002_RECORD):
            record = extract_record(current_line, DETAIL_002_RECORD)
        elif valid_record(current_line, DETAIL_003_RECORD):
            record = extract_record(current_line, DETAIL_003_RECORD)
        elif valid_record(current_line, DETAIL_004_RECORD):
            record = extract_record(current_line, DETAIL_004_RECORD)
        elif valid_record(current_line, DETAIL_005_RECORD):
            record = extract_record(current_line, DETAIL_005_RECORD)
        elif valid_record(current_line, DETAIL_006_RECORD):
            record = extract_record(current_line, DETAIL_006_RECORD)
        elif valid_record(current_line, DETAIL_007_RECORD):
            record = extract_record(current_line, DETAIL_007_RECORD)
        elif valid_record(current_line, DETAIL_101_RECORD):
            record = extract_record(current_line, DETAIL_101_RECORD)
        elif valid_record(current_line, DETAIL_102_RECORD):
            record = extract_record(current_line, DETAIL_102_RECORD)
        elif valid_record(current_line, DETAIL_103_RECORD):
            record = extract_record(current_line, DETAIL_103_RECORD)
        elif valid_record(current_line, DETAIL_910_RECORD):
            record = extract_record(current_line, DETAIL_910_RECORD)
        elif valid_record(current_line, NATIONAL_FOOTER_RECORD):
            record = extract_record(current_line, NATIONAL_FOOTER_RECORD)
        elif valid_record(current_line, ORDERING_FOOTER_RECORD):
            record = extract_record(current_line, ORDERING_FOOTER_RECORD)
        else:
            raise BaseException('Invalid record: "%s"' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records


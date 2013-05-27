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

HEADER_RECORD_TYPE_1 = (
    (1, 2, 'record_code', 'N', '=03'),
    (3, 2, 'operation_code', 'N', '=56'),
    (5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27, 3, 'data_number', 'N', '=001'),
    (30, 6, 'creation_date', 'D', '%d%m%y'),
    (36, 6, 'planned_date', 'D', '%d%m%y'),
    (42, 4, 'bank_code', 'N'),
    (46, 4, 'bank_office', 'N'),
    (50, 10, 'bank_account_num', 'N'),
    (60, 1, 'charge_detail', 'E', (
            ('0', 'only_one_account_move_line'),
            ('1', 'one_account_move_line_for_each_recipient'),
            )),
    (61, 3, 'free_2', 'A'),
    (64, 2, 'bank_account_dc', 'N'),
    (66, 7, 'free_3', 'A'),
    )

HEADER_RECORD_TYPE_2 = (
    (1, 2, 'record_code', 'N', '=03'),
    (3, 2, 'operation_code', 'N', '=56'),
    (5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27, 3, 'data_number', 'N', '=002'),
    (30, 36, 'name', 'A'),
    (66, 7, 'free_2', 'A'),
    )

HEADER_RECORD_TYPE_3 = (
    (1, 2, 'record_code', 'N', '=03'),
    (3, 2, 'operation_code', 'N', '=56'),
    (5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27, 3, 'data_number', 'N', '=003'),
    (30, 36, 'address', 'A'),
    (66, 7, 'free_2', 'A'),
    )

HEADER_RECORD_TYPE_4 = (
    (1, 2, 'record_code', 'N', '=03'),
    (3, 2, 'operation_code', 'N', '=56'),
    (5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27, 3, 'data_number', 'N', '=004'),
    (30, 36, 'city', 'A'),
    (66, 7, 'free_2', 'A'),
    )

HEADER_RECORD_TYPE_7 = (
    (1, 2, 'record_code', 'N', '=03'),
    (3, 2, 'operation_code', 'N', '=56'),
    (5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27, 3, 'data_number', 'N', '=007'),
    (30, 36, 'on_behalf_of', 'A'),
    (66, 7, 'free_2', 'A'),
    )

HEADER_RECORD_TYPE_8 = (
    (1, 2, 'record_code', 'N', '=03'),
    (3, 2, 'operation_code', 'N', '=56'),
    (5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27, 3, 'data_number', 'N', '=008'),
    (30, 36, 'address_on_behalf_of', 'A'),
    (66, 7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_010 = (
    (1, 2, 'record_code', 'N', '=06'),
    (3, 2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            )),
    (5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27, 3, 'data_number', 'N', '=010'),
    (30, 12, 'amount', 'N', '2'),
    (42, 4, 'bank_code', 'N'),
    (46, 4, 'bank_office', 'N'),
    (50, 10, 'bank_account_num', 'N'),
    (60, 1, 'cost', 'E', (
            ('1', 'payer'),
            ('2', 'recipient'),
            )),
    (61, 1, 'concept', 'E', (
            ('1', 'payroll'),
            ('8', 'pension'),
            ('9', 'other'),
            )),
    (62, 2, 'free_2', 'A'),
    (64, 2, 'bank_account_dc', 'N'),
    (66, 7, 'free_3', 'A'),
    )

RECIPIENT_RECORD_TYPE_011 = (
    (1, 2, 'record_code', 'N', '=06'),
    (3, 2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    (5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27, 3, 'data_number', 'N', '=011'),
    (30, 36, 'name', 'A'),
    (66, 7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_012 = (
    (1, 2, 'record_code', 'N', '=06'),
    (3, 2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    (5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27, 3, 'data_number', 'N', '=012'),
    (30, 36, 'street', 'A'),
    (66, 7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_013 = (
    (1, 2, 'record_code', 'N', '=06'),
    (3, 2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    (5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27, 3, 'data_number', 'N', '=013'),
    (30, 36, 'street2', 'A'),
    (66, 7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_014 = (
    (1, 2, 'record_code', 'N', '=06'),
    (3, 2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    (5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27, 3, 'data_number', 'N', '=014'),
    (30, 36, 'zip_city', 'A'),
    (66, 7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_015 = (
    (1, 2, 'record_code', 'N', '=06'),
    (3, 2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    (5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27, 3, 'data_number', 'N', '=015'),
    (30, 36, 'province', 'A'),
    (66, 7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_016 = (
    (1, 2, 'record_code', 'N', '=06'),
    (3, 2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    (5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27, 3, 'data_number', 'N', '=016'),
    (30, 36, 'concept', 'A'),
    (66, 7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_017 = (
    (1, 2, 'record_code', 'N', '=06'),
    (3, 2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    (5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27, 3, 'data_number', 'N', '=017'),
    (30, 36, 'concept2', 'A'),
    (66, 7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_018 = (
    (1, 2, 'record_code', 'N', '=06'),
    (3, 2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    (5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27, 3, 'data_number', 'N', '=018'),
    (30, 36, 'beneficiary_nif', 'A'),
    (66, 7, 'free_2', 'A'),
    )

RECORD_OF_TOTALS = (
    (1, 2, 'record_code', 'N', '=08'),
    (3, 2, 'operation_code', 'N', '=56'),
    (5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27, 3, 'free_2', 'A'),
    (30, 12, 'amount', 'N', '2'),
    (42, 8, 'payment_line_count', 'N'),
    (50, 10, 'record_count', 'N'),
    (60, 6, 'free_3', 'A'),
    (66, 7, 'free_4', 'A'),
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
        elif valid_record(current_line, DETAIL_001_RECORD):
            record = extract_record(current_line, DETAIL_001_RECORD)
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
#        elif valid_record(current_line, DETAIL_101_RECORD):
#            record = extract_record(current_line, DETAIL_101_RECORD)
#        elif valid_record(current_line, DETAIL_102_RECORD):
#            record = extract_record(current_line, DETAIL_102_RECORD)
#        elif valid_record(current_line, DETAIL_103_RECORD):
#            record = extract_record(current_line, DETAIL_103_RECORD)
#        elif valid_record(current_line, DETAIL_910_RECORD):
#            record = extract_record(current_line, DETAIL_910_RECORD)
        elif valid_record(current_line, NATIONAL_FOOTER_RECORD):
            record = extract_record(current_line, NATIONAL_FOOTER_RECORD)
        elif valid_record(current_line, ORDERING_FOOTER_RECORD):
            record = extract_record(current_line, ORDERING_FOOTER_RECORD)
        else:
            raise BaseException('Invalid record: "%s"' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records

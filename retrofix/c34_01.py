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
    ( 1,  2, 'record_code', 'N', '=03'),
    ( 3,  2, 'operation_code', 'N', '=56'),
    ( 5, 10, 'nif', 'A'),
    (15,  5, 'notebook_version', 'N', '=34016'),
    (20,  7, 'free_1', 'A'),
    (27,  3, 'data_number', 'N', '=001'),
    (30,  6, 'send_date', 'D', '%d%m%y'),
    (36,  6, 'creation_date', 'D', '%d%m%y'),
    (42,  4, 'bank_code', 'N'),
    (46,  4, 'bank_office', 'N'),
    (50, 10, 'bank_account_num', 'N'),
    (60,  1, 'charge_detail', 'E', (
            ('0', 'with_relationship'),
            ('1', 'without_relationship'),
            )),
    (61,  1, 'expenses', 'E', (
            ('1', 'expenses_by_payer'),
            ('2', 'expenses_by_recipient'),
            ('1', 'cost_sharing'),
            )),
    (62,  2, 'free_2', 'A'),
    (64,  2, 'bank_account_dc', 'N'),
    (66,  7, 'free_3', 'A'),
    )

HEADER_RECORD_TYPE_2 = (
    ( 1,  2, 'record_code', 'N', '=03'),
    ( 3,  2, 'operation_code', 'N', '=56'),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27,  3, 'data_number', 'N', '=002'),
    (30, 36, 'name', 'A'),
    (66,  7, 'free_2', 'A'),
    )

HEADER_RECORD_TYPE_3 = (
    ( 1,  2, 'record_code', 'N', '=03'),
    ( 3,  2, 'operation_code', 'N', '=56'),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27,  3, 'data_number', 'N', '=003'),
    (30, 36, 'address', 'A'),
    (66,  7, 'free_2', 'A'),
    )

HEADER_RECORD_TYPE_4 = (
    ( 1,  2, 'record_code', 'N', '=03'),
    ( 3,  2, 'operation_code', 'N', '=56'),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27,  3, 'data_number', 'N', '=004'),
    (30, 36, 'city', 'A'),
    (66,  7, 'free_2', 'A'),
    )

HEADER_RECORD_TYPE_5 = (
    ( 1,  2, 'record_code', 'N', '=03'),
    ( 3,  2, 'operation_code', 'N', '=56'),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27,  3, 'data_number', 'N', '=007'),
    (30, 36, 'on_behalf_of_another', 'A'),
    (66,  7, 'free_2', 'A'),
    )

HEADER_RECORD_TYPE_6 = (
    ( 1,  2, 'record_code', 'N', '=03'),
    ( 3,  2, 'operation_code', 'N', '=56'),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27,  3, 'data_number', 'N', '=008'),
    (30, 36, 'on_behalf_of_another_address', 'A'),
    (66,  7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_1 = (
    ( 1,  2, 'record_code', 'N', '=06'),
    ( 3,  2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27,  3, 'data_number', 'N', '=010'),
    (30, 12, 'amount', 'N', '2'),
    (42,  4, 'bank_code', 'N'),
    (46,  4, 'bank_office', 'N'),
    (50, 10, 'bank_account_num', 'N'),
    (60,  1, 'free_1', 'A'),
    (61,  1, 'concept', 'E', (
            ('1', 'payroll'),
            ('8', 'pension'),
            ('9', 'others'),
            )),
    (62,  2, 'free_2', 'A'),
    (64,  2, 'bank_account_dc', 'N'),
    (66,  7, 'free_3', 'A'),
    )

RECIPIENT_RECORD_TYPE_2 = (
    ( 1,  2, 'record_code', 'N', '=06'),
    ( 3,  2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27,  3, 'data_number', 'N', '=011'),
    (30, 36, 'name', 'A'),
    (66,  7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_3 = (
    ( 1,  2, 'record_code', 'N', '=06'),
    ( 3,  2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27,  3, 'data_number', 'N', '=012'),
    (30, 36, 'address', 'A'),
    (66,  7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_4 = (
    ( 1,  2, 'record_code', 'N', '=06'),
    ( 3,  2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27,  3, 'data_number', 'N', '=013'),
    (30, 36, 'address2', 'A'),
    (66,  7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_5 = (
    ( 1,  2, 'record_code', 'N', '=06'),
    ( 3,  2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27,  3, 'data_number', 'N', '=014'),
    (30, 36, 'zip_city', 'A'),
    (66,  7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_6 = (
    ( 1,  2, 'record_code', 'N', '=06'),
    ( 3,  2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27,  3, 'data_number', 'N', '=015'),
    (30, 36, 'province', 'A'),
    (66,  7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_7 = (
    ( 1,  2, 'record_code', 'N', '=06'),
    ( 3,  2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27,  3, 'data_number', 'N', '=016'),
    (30, 36, 'concept', 'A'),
    (66,  7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_8 = (
    ( 1,  2, 'record_code', 'N', '=06'),
    ( 3,  2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27,  3, 'data_number', 'N', '=017'),
    (30, 36, 'concept2', 'A'),
    (66,  7, 'free_2', 'A'),
    )

RECIPIENT_RECORD_TYPE_9 = (
    ( 1,  2, 'record_code', 'N', '=06'),
    ( 3,  2, 'operation_code', 'E', (
            ('56', 'transfer'),
            ('57', 'check'),
            )),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'recipient_nif', 'A'),
    (27,  3, 'data_number', 'N', '=017'),
    (30, 18, 'beneficiary_nif', 'A'),
    (48, 18, 'another_id_doc', 'A'),
    (66,  7, 'free_2', 'A'),
    )

RECORD_OF_TOTALS = (
    ( 1,  2, 'record_code', 'N', '=08'),
    ( 3,  2, 'operation_code', 'N', '=56'),
    ( 5, 10, 'nif', 'A'),
    (15, 12, 'free_1', 'A'),
    (27,  3, 'free_2', 'A'),
    (30, 12, 'amount', 'N', '2'),
    (42,  8, 'payment_line_count', 'N'),
    (50, 10, 'record_count', 'N'),
    (60,  6, 'free_3', 'A'),
    (66,  7, 'free_4', 'A'),
    )

def read(data):
    # TODO
    return

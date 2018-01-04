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

from .fields import Const, Char, Number, Date, Selection, Numeric, Integer

HEADER_RECORD_TYPE_1 = (
    ( 1,  2, 'record_code', Const('03')),
    ( 3,  2, 'operation_code', Const('56')),
    ( 5, 10, 'nif', Char),
    (15,  5, 'notebook_version', Const('34016')),
    (20,  7, 'free_1', Char),
    (27,  3, 'data_number', Const('001')),
    (30,  6, 'send_date', Date('%d%m%y')),
    (36,  6, 'creation_date', Date('%d%m%y')),
    (42,  4, 'bank_code', Number),
    (46,  4, 'bank_office', Number),
    (50, 10, 'bank_account_num', Number),
    (60,  1, 'charge_detail', Selection([
            ('0', 'with_relationship'),
            ('1', 'without_relationship'),
            ])),
    (61,  1, 'expenses', Selection([
            ('1', 'expenses_by_payer'),
            ('2', 'expenses_by_recipient'),
            ('3', 'cost_sharing'),
            ])),
    (62,  2, 'free_2', Char),
    (64,  2, 'bank_account_dc', Number),
    (66,  7, 'free_3', Char),
    )

HEADER_RECORD_TYPE_2 = (
    ( 1,  2, 'record_code', Const('03')),
    ( 3,  2, 'operation_code', Const('56')),
    ( 5, 10, 'nif', Char),
    (15, 12, 'free_1', Char),
    (27,  3, 'data_number', Const('002')),
    (30, 36, 'name', Char),
    (66,  7, 'free_2', Char),
    )

HEADER_RECORD_TYPE_3 = (
    ( 1,  2, 'record_code', Const('03')),
    ( 3,  2, 'operation_code', Const('56')),
    ( 5, 10, 'nif', Char),
    (15, 12, 'free_1', Char),
    (27,  3, 'data_number', Const('003')),
    (30, 36, 'address', Char),
    (66,  7, 'free_2', Char),
    )

HEADER_RECORD_TYPE_4 = (
    ( 1,  2, 'record_code', Const('03')),
    ( 3,  2, 'operation_code', Const('56')),
    ( 5, 10, 'nif', Char),
    (15, 12, 'free_1', Char),
    (27,  3, 'data_number', Const('004')),
    (30, 36, 'city', Char),
    (66,  7, 'free_2', Char),
    )

HEADER_RECORD_TYPE_5 = (
    ( 1,  2, 'record_code', Const('03')),
    ( 3,  2, 'operation_code', Const('56')),
    ( 5, 10, 'nif', Char),
    (15, 12, 'free_1', Char),
    (27,  3, 'data_number', Const('007')),
    (30, 36, 'on_behalf_of_another', Char),
    (66,  7, 'free_2', Char),
    )

HEADER_RECORD_TYPE_6 = (
    ( 1,  2, 'record_code', Const('03')),
    ( 3,  2, 'operation_code', Const('56')),
    ( 5, 10, 'nif', Char),
    (15, 12, 'free_1', Char),
    (27,  3, 'data_number', Const('008')),
    (30, 36, 'on_behalf_of_another_address', Char),
    (66,  7, 'free_2', Char),
    )

RECIPIENT_RECORD_TYPE_1 = (
    ( 1,  2, 'record_code', Const('06')),
    ( 3,  2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ])),
    ( 5, 10, 'nif', Char),
    (15, 12, 'recipient_nif', Char),
    (27,  3, 'data_number', Const('010')),
    (30, 12, 'amount', Numeric),
    (42,  4, 'bank_code', Number),
    (46,  4, 'bank_office', Number),
    (50, 10, 'bank_account_num', Number),
    (60,  1, 'free_1', Char),
    (61,  1, 'concept', Selection([
            ('1', 'payroll'),
            ('8', 'pension'),
            ('9', 'others'),
            ])),
    (62,  2, 'free_2', Char),
    (64,  2, 'bank_account_dc', Number),
    (66,  7, 'free_3', Char),
    )

RECIPIENT_RECORD_TYPE_2 = (
    ( 1,  2, 'record_code', Const('06')),
    ( 3,  2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ])),
    ( 5, 10, 'nif', Char),
    (15, 12, 'recipient_nif', Char),
    (27,  3, 'data_number', Const('011')),
    (30, 36, 'name', Char),
    (66,  7, 'free_2', Char),
    )

RECIPIENT_RECORD_TYPE_3 = (
    ( 1,  2, 'record_code', Const('06')),
    ( 3,  2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ])),
    ( 5, 10, 'nif', Char),
    (15, 12, 'recipient_nif', Char),
    (27,  3, 'data_number', Const('012')),
    (30, 36, 'address', Char),
    (66,  7, 'free_2', Char),
    )

RECIPIENT_RECORD_TYPE_4 = (
    ( 1,  2, 'record_code', Const('06')),
    ( 3,  2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ])),
    ( 5, 10, 'nif', Char),
    (15, 12, 'recipient_nif', Char),
    (27,  3, 'data_number', Const('013')),
    (30, 36, 'address2', Char),
    (66,  7, 'free_2', Char),
    )

RECIPIENT_RECORD_TYPE_5 = (
    ( 1,  2, 'record_code', Const('06')),
    ( 3,  2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ])),
    ( 5, 10, 'nif', Char),
    (15, 12, 'recipient_nif', Char),
    (27,  3, 'data_number', Const('014')),
    (30, 36, 'zip_city', Char),
    (66,  7, 'free_2', Char),
    )

RECIPIENT_RECORD_TYPE_6 = (
    ( 1,  2, 'record_code', Const('06')),
    ( 3,  2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ])),
    ( 5, 10, 'nif', Char),
    (15, 12, 'recipient_nif', Char),
    (27,  3, 'data_number', Const('015')),
    (30, 36, 'province', Char),
    (66,  7, 'free_2', Char),
    )

RECIPIENT_RECORD_TYPE_7 = (
    ( 1,  2, 'record_code', Const('06')),
    ( 3,  2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ])),
    ( 5, 10, 'nif', Char),
    (15, 12, 'recipient_nif', Char),
    (27,  3, 'data_number', Const('016')),
    (30, 36, 'concept', Char),
    (66,  7, 'free_2', Char),
    )

RECIPIENT_RECORD_TYPE_8 = (
    ( 1,  2, 'record_code', Const('06')),
    ( 3,  2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ])),
    ( 5, 10, 'nif', Char),
    (15, 12, 'recipient_nif', Char),
    (27,  3, 'data_number', Const('017')),
    (30, 36, 'concept2', Char),
    (66,  7, 'free_2', Char),
    )

RECIPIENT_RECORD_TYPE_9 = (
    ( 1,  2, 'record_code', Const('06')),
    ( 3,  2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ])),
    ( 5, 10, 'nif', Char),
    (15, 12, 'recipient_nif', Char),
    (27,  3, 'data_number', Const('017')),
    (30, 18, 'beneficiary_nif', Char),
    (48, 18, 'another_id_doc', Char),
    (66,  7, 'free_2', Char),
    )

RECORD_OF_TOTALS = (
    ( 1,  2, 'record_code', Const('08')),
    ( 3,  2, 'operation_code', Const('56')),
    ( 5, 10, 'nif', Char),
    (15, 12, 'free_1', Char),
    (27,  3, 'free_2', Char),
    (30, 12, 'amount', Numeric),
    (42,  8, 'payment_line_count', Integer),
    (50, 10, 'record_count', Integer),
    (60,  6, 'free_3', Char),
    (66,  7, 'free_4', Char),
    )

def read(data):
    # TODO
    return

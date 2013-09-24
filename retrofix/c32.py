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

FILE_HEADER_RECORD = (
        (  1,  2, 'record_code', Const('02')),
        (  3,  2, 'data_code', Const('65')),
        (  5,  2, 'free_01', Char),
        (  7,  6, 'file_date', Date('%d%m%y')),
        ( 13,  4, 'number', Char),
        ( 17,  6, 'free_02', Char),
        ( 23,  6, 'free_03', Char),
        ( 29, 15, 'free_04', Char),
        ( 44,  4, 'free_05', Char),
        ( 48,  4, 'free_06', Char),
        ( 52,  4, 'bank_code', Char),
        ( 56,  4, 'bank_office', Char),
        ( 60,  6, 'free_07', Char),
        ( 66, 61, 'free_08', Char),
        (127, 24, 'free_09', Char),
        )

# ORDER => REMESA
# GRANTOR => CEDENTE

# Note: For some reason, the OpenERP example we've got in a production
# environment with "La Caixa", move account_payment_1 (and the rest of the
# fields) 21 positions before. That is at position 44.

ORDER_HEADER_RECORD = (
        (  1,  2, 'record_code', Const('11')),
        (  3,  2, 'data_code', Const('65')),
        (  5,  2, 'free_01', Char),
        (  7,  6, 'file_date', Date('%d%m%y')),
        ( 13,  4, 'order_number', Char),
        ( 17,  6, 'free_02', Char),
        ( 23,  6, 'free_03', Char),
        ( 29, 15, 'grantor_identifier', Char),
        ( 44,  1, 'truncated', Number),
        ( 45,  6, 'free_04', Char),
        ( 51,  5, 'free_05', Char),
        ( 56,  4, 'free_06', Char),
        ( 60,  6, 'free_07', Char),
        ( 66, 20, 'account_payment_1', Account),
        ( 86, 20, 'account_payment_2', Account),
        (106, 20, 'account_payment_3', Account),
        (126,  1, 'free_08', Char),
        (127, 24, 'free_09', Char),
        )

INDIVIDUAL_1_RECORD = (
        (  1,  2, 'record_code', Const('25')),
        (  3,  2, 'data_code', Const('65')),
        (  5,  2, 'free_01', Char),
        (  7, 15, 'document_number', Char),
        ( 22,  6, 'file_date', Date('%d%m%y')),
        ( 28,  4, 'order_number', Char),
        ( 32,  2, 'province_code', Char),
        # Código I.N.E. Plaza de libramiento
        ( 34,  7, 'ine', Char),
        ( 41,  2, 'free_02', Char),
        ( 43, 20, 'city', Char),
        ( 63,  1, 'free_03', Char),
        ( 64, 15, 'free_04', Char),
        ( 79,  9, 'free_05', Char),
        ( 88,  9, 'amount', Numeric(sign=SIGN_12)),
        ( 97, 15, 'free_06', Char),
        (112,  6, 'date_due', Date('%d%m%y')),
        (118,  6, 'free_07', Char),
        (124,  6, 'free_08', Char),
        (130,  1, 'free_09', Char),
        (131,  4, 'free_10', Char),
        (135, 16, 'free_11', Char),
        )

INDIVIDUAL_2_RECORD = (
        (  1,  2, 'record_code', Const('26')),
        (  3,  2, 'data_code', Const('65')),
        (  5,  2, 'free_01', Char),
        (  7, 15, 'document_number', Char),
        ( 22,  2, 'free_02', Char),
        ( 24,  1, 'document_type', Number),
        ( 25,  6, 'send_date', Date('%d%m%y')),
        ( 31,  1, 'accept_code', Number),
        ( 32,  1, 'expenses_clause', Number),
        ( 33, 20, 'account', Account),
        ( 53, 34, 'sender_name', Char),
        ( 87, 34, 'receiver_name', Char),
        (121, 30, 'additional_information', Char),
        )

INDIVIDUAL_3_RECORD = (
        (  1,  2, 'record_code', Const('27')),
        (  3,  2, 'data_code', Const('65')),
        (  5,  2, 'free_01', Char),
        (  7, 15, 'document_number', Char),
        ( 22,  2, 'free_02', Char),
        ( 24, 34, 'receiver_address', Char), #Domicilio del librado
        ( 58,  5, 'receiver_zip', Char), # Código postal plaza librada
        ( 63, 20, 'receiver_city', Char), # Plaza librada
        ( 83,  2, 'receiver_province_code', Char), # Número provincia plaza librada
        ( 85,  7, 'receiver_ine', Number), # Código I.N.E. Plaza Librada
        ( 92,  9, 'receiver_nif', Char),
        (101, 50, 'free_03', Char),
        )

ORDER_FOOTER_RECORD = (
        (  1,  2, 'record_code', Const('71')),
        (  3,  2, 'data_code', Const('65')),
        (  5,  2, 'free_01', Char),
        (  7,  6, 'file_date', Date('%d%m%y')),
        ( 13,  4, 'order_number', Char),
        ( 17,  6, 'free_02', Char),
        ( 23,  6, 'free_03', Char),
        ( 29, 37, 'free_04', Char),
        ( 66, 10, 'free_05', Char),
        ( 76, 10, 'amount', Numeric(sign=SIGN_12)),
        ( 86, 10, 'free_06', Char),
        ( 96,  6, 'free_07', Char),
        (102,  7, 'free_08', Char),
        (109,  6, 'free_09', Char),
        (115,  6, 'free_10', Char),
        (121,  6, 'free_11', Char),
        (127,  5, 'free_12', Char),
        (132,  7, 'record_count', Integer),
        (139,  6, 'payment_count', Integer),
        (145,  6, 'free_13', Char),
        )

FILE_FOOTER_RECORD = (
        (  1,  2, 'record_code', Const('98')),
        (  3,  2, 'data_code', Const('65')),
        (  5,  2, 'free_01', Char),
        (  7, 22, 'free_02', Char),
        ( 29, 37, 'free_03', Char),
        ( 66, 10, 'free_04', Char),
        ( 76, 10, 'amount', Numeric(sign=SIGN_12)),
        ( 86, 10, 'free_05', Char),
        ( 96,  6, 'free_06', Char),
        (102,  7, 'free_07', Char),
        (109,  6, 'free_08', Char),
        (115,  6, 'free_09', Char),
        (121,  6, 'free_10', Char),
        (127,  5, 'order_count', Char),
        (132,  7, 'record_count', Integer),
        (139,  6, 'payment_count', Integer),
        (145,  6, 'free_11', Char),
        )


def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, FILE_HEADER_RECORD))

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, ORDER_HEADER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if Record.valid(current_line, INDIVIDUAL_1_RECORD):
            record = Record.extract(current_line, INDIVIDUAL_1_RECORD)
        elif Record.valid(current_line, INDIVIDUAL_2_RECORD):
            record = Record.extract(current_line, INDIVIDUAL_2_RECORD)
        elif Record.valid(current_line, INDIVIDUAL_3_RECORD):
            record = Record.extract(current_line, INDIVIDUAL_3_RECORD)
        elif Record.valid(current_line, ORDER_FOOTER_RECORD):
            record = Record.extract(current_line, ORDER_FOOTER_RECORD)
        elif Record.valid(current_line, FILE_FOOTER_RECORD):
            record = Record.extract(current_line, FILE_FOOTER_RECORD)
        else:
            record = Record.extract(current_line, INDIVIDUAL_2_RECORD)
            raise BaseException('Invalid record: "%s"' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records


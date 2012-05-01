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

FILE_HEADER_RECORD = (
        (  1,  2, 'record_code', 'N', '=02'),
        (  3,  2, 'data_code', 'N', '=65'),
        (  5,  2, 'free_01', 'A'),
        (  7,  6, 'file_date', 'D', '%d%m%y'),
        ( 13,  4, 'number', 'A'),
        ( 17,  6, 'free_02', 'A'),
        ( 23,  6, 'free_03', 'A'),
        ( 29, 15, 'free_04', 'A'),
        ( 44,  4, 'free_05', 'A'),
        ( 48,  4, 'free_06', 'A'),
        ( 52,  4, 'bank_code', 'A'),
        ( 56,  4, 'bank_office', 'A'),
        ( 60,  6, 'free_07', 'A'),
        ( 66, 61, 'free_08', 'A'),
        (127, 24, 'free_09', 'A'),
        )

# ORDER => REMESA
# GRANTOR => CEDENTE

# Note: For some reason, the OpenERP example we've got in a production 
# environment with "La Caixa", move account_payment_1 (and the rest of the 
# fields) 21 positions before. That is at position 44.

ORDER_HEADER_RECORD = (
        (  1,  2, 'record_code', 'N', '=11'),
        (  3,  2, 'data_code', 'N', '=65'),
        (  5,  2, 'free_01', 'A'),
        (  7,  6, 'file_date', 'D', '%d%m%y'),
        ( 13,  4, 'order_number', 'A'),
        ( 17,  6, 'free_02', 'A'),
        ( 23,  6, 'free_03', 'A'),
        ( 29, 15, 'grantor_identifier', 'A'),
        ( 44,  1, 'truncated', 'N'),
        ( 45,  6, 'free_04', 'A'),
        ( 51,  5, 'free_05', 'A'),
        ( 56,  4, 'free_06', 'A'),
        ( 60,  6, 'free_07', 'A'),
        ( 66, 20, 'account_payment_1', 'ACCOUNT'),
        ( 86, 20, 'account_payment_2', 'ACCOUNT'),
        (106, 20, 'account_payment_3', 'ACCOUNT'),
        (126,  1, 'free_08', 'A'),
        (127, 24, 'free_09', 'A'),
        )

INDIVIDUAL_1_RECORD = (
        (  1,  2, 'record_code', 'N', '=25'),
        (  3,  2, 'data_code', 'N', '=65'),
        (  5,  2, 'free_01', 'A'),
        (  7, 15, 'document_number', 'A'),
        ( 22,  6, 'file_date', 'D', '%d%m%y'),
        ( 28,  4, 'order_number', 'A'),
        ( 32,  2, 'province_code', 'A'),
        ( 34,  7, 'ine', 'A'), # Código I.N.E. Plaza de libramiento
        ( 41,  2, 'free_02', 'A'),
        ( 43, 20, 'city', 'A'),
        ( 63,  1, 'free_03', 'A'),
        ( 64, 15, 'free_04', 'A'),
        ( 79,  9, 'free_05', 'A'),
        ( 88,  9, 'amount', 'N', '2'),
        ( 97, 15, 'free_06', 'A'),
        (112,  6, 'date_due', 'D', '%d%m%y'),
        (118,  6, 'free_07', 'A'),
        (124,  6, 'free_08', 'A'),
        (130,  1, 'free_09', 'A'),
        (131,  4, 'free_10', 'A'),
        (135, 16, 'free_11', 'A'),
        )

INDIVIDUAL_2_RECORD = (
        (  1,  2, 'record_code', 'N', '=26'),
        (  3,  2, 'data_code', 'N', '=65'),
        (  5,  2, 'free_01', 'A'),
        (  7, 15, 'document_number', 'A'),
        ( 22,  2, 'free_02', 'A'),
        ( 24,  1, 'document_type', 'N'),
        ( 25,  6, 'send_date', 'D', '%d%m%y'),
        ( 31,  1, 'accept_code', 'N'),
        ( 33, 20, 'account', 'ACCOUNT'),
        ( 53, 34, 'sender_name', 'A'),
        ( 87, 34, 'receiver_name', 'A'),
        (121, 30, 'additional_information', 'A'),
        )

INDIVIDUAL_3_RECORD = (
        (  1,  2, 'record_code', 'N', '=27'),
        (  3,  2, 'data_code', 'N', '=65'),
        (  5,  2, 'free_01', 'A'),
        (  7, 15, 'document_number', 'A'),
        ( 22,  2, 'free_02', 'A'),
        ( 24, 34, 'receiver_address', 'A'), #Domicilio del librado
        ( 58,  5, 'receiver_zip', 'A'), # Código postal plaza librada
        ( 63, 20, 'receiver_city', 'A'), # Plaza librada
        ( 83,  2, 'receiver_province_code', 'A'), # Número provincia plaza librada
        ( 85,  7, 'receiver_ine', 'N'), # Código I.N.E. Plaza Librada
        ( 92,  9, 'receiver_nif', 'A'),
        (101, 50, 'free_03', 'A'),
        )

ORDER_FOOTER_RECORD = (
        (  1,  2, 'record_code', 'N', '=71'),
        (  3,  2, 'data_code', 'N', '=65'),
        (  5,  2, 'free_01', 'A'),
        (  7,  6, 'file_date', 'D', '%d%m%y'),
        ( 13,  4, 'order_number', 'A'),
        ( 17,  6, 'free_02', 'A'),
        ( 23,  6, 'free_03', 'A'),
        ( 29, 37, 'free_04', 'A'),
        ( 66, 10, 'free_05', 'A'),
        ( 76, 10, 'amount', 'A'),
        ( 86, 10, 'free_06', 'A'),
        ( 96,  6, 'free_07', 'A'),
        (102,  7, 'free_08', 'A'),
        (109,  6, 'free_09', 'A'),
        (115,  6, 'free_10', 'A'),
        (121,  6, 'free_11', 'A'),
        (127,  5, 'free_12', 'A'),
        (132,  7, 'record_count', 'N'),
        (139,  6, 'payment_count', 'N'),
        (145,  6, 'free_13', 'A'),
        )

FILE_FOOTER_RECORD = (
        (  1,  2, 'record_code', 'N', '=98'),
        (  3,  2, 'data_code', 'N', '=65'),
        (  5,  2, 'free_01', 'A'),
        (  7, 22, 'free_02', 'D', '%d%m%y'),
        ( 29, 37, 'free_03', 'A'),
        ( 66, 10, 'free_04', 'A'),
        ( 76, 10, 'amount', 'A'),
        ( 86, 10, 'free_05', 'A'),
        ( 96,  6, 'free_06', 'A'),
        (102,  7, 'free_07', 'A'),
        (109,  6, 'free_08', 'A'),
        (115,  6, 'free_09', 'A'),
        (121,  6, 'free_10', 'A'),
        (127,  5, 'order_count', 'A'),
        (132,  7, 'record_count', 'N'),
        (139,  6, 'payment_count', 'N'),
        (145,  6, 'free_11', 'A'),
        )


def read(data):
    lines = data.splitlines()
    line_count = len(lines)

    records = []

    current_line = lines.pop(0)
    records.append(extract_record(current_line, FILE_HEADER_RECORD))

    current_line = lines.pop(0)
    records.append(extract_record(current_line, ORDER_HEADER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if valid_record(current_line, INDIVIDUAL_1_RECORD):
            record = extract_record(current_line, INDIVIDUAL_1_RECORD)
        elif valid_record(current_line, INDIVIDUAL_2_RECORD):
            record = extract_record(current_line, INDIVIDUAL_2_RECORD)
        elif valid_record(current_line, INDIVIDUAL_3_RECORD):
            record = extract_record(current_line, INDIVIDUAL_3_RECORD)
        elif valid_record(current_line, ORDER_FOOTER_RECORD):
            record = extract_record(current_line, ORDER_FOOTER_RECORD)
        elif valid_record(current_line, FILE_FOOTER_RECORD):
            record = extract_record(current_line, FILE_FOOTER_RECORD)
        else:
            record = extract_record(current_line, INDIVIDUAL_2_RECORD)
            raise BaseException('Invalid record: "%s"' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records


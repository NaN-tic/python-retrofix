# encoding: utf8
##############################################################################
#
#    Copyright (C) 2013 NaN Projectes de Programari Lliure, S.L.
#                           http://www.NaN-tic.com
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


PRESENTER_HEADER_RECORD = (
    (  1,  1, 'record_code', Const('1')),
    (  2,  3, 'model', Const('340')),
    (  5,  4, 'fiscalyear', Number),
    (  9,  9, 'nif', Char),
    ( 18, 40, 'presenter_name', Char),
    ( 58,  1, 'support_type', Char),
    ( 59,  9, 'contact_phone', Number),
    ( 68, 40, 'contact_name', Char),
    (108, 13, 'declaration_number', Number),
    (121,  1, 'complementary', Char),
    (122,  1, 'replacement', Char),
    (123, 13, 'previous_declaration_number', Number),
    (136,  2, 'period', Char),
    (138,  9, 'record_count', Integer),
    (147, 18, 'total_base', Numeric(sign=SIGN_N)),
    (165, 18, 'total_tax', Numeric(sign=SIGN_N)),
    (183, 18, 'total', Numeric(sign=SIGN_N)),
    (391,  9, 'representative_nif', Char),
    (400, 16, 'digital_signature', Char),
    )

ISSUED_RECORD = (
    (  1,  1, 'record_code', Const('2')),
    (  2,  3, 'model', Const('340')),
    (  5,  4, 'fiscalyear', Number),
    (  9,  9, 'nif', Char),
    ( 18,  9, 'party_nif', Char),
    ( 27,  9, 'representative_nif', Char),
    ( 36, 40, 'party_name', Char),
    ( 76,  2, 'party_country', Char),
    ( 78,  1, 'party_identifier_type', Number),
    ( 79, 20, 'party_identifier', Char),
    ( 99,  1, 'book_key', Char),
    (100,  1, 'operation_key', Char),
    (101,  8, 'issue_date', Date('%Y%m%d')),
    (109,  8, 'operation_date', Date('%Y%m%d')),
    (117,  5, 'tax_rate', Numeric(sign=SIGN_N)),
    (122, 14, 'base', Numeric(sign=SIGN_N)),
    (136, 14, 'tax', Numeric(sign=SIGN_N)),
    (150, 14, 'total', Numeric(sign=SIGN_N)),
    (164, 14, 'cost', Numeric(sign=SIGN_N)),
    (178, 40, 'invoice_number', Char),
    (218, 18, 'record_number', Char),
    # Issued Invoices
    (236,  8, 'issued_invoice_count', Integer),
    (244,  2, 'record_count', Integer),
    (246, 40, 'first_invoice_number', Char),
    (286, 40, 'last_invoice_number', Char),
    (326, 40, 'corrective_invoice_number', Char),
    (366,  5, 'equivalence_tax_rate', Numeric(sign=SIGN_N)),
    (371, 14, 'equivalence_tax', Numeric(sign=SIGN_N)),
    (385,  1, 'property_state', Char),
    (386, 25, 'cadaster_number', Char),
    (411, 15, 'cash_amount', Numeric(sign=SIGN_N)),
    (426,  4, 'invoice_fiscalyear', Number),
    (430, 15, 'property_transfer_amount', Numeric(sign=SIGN_N)),
    )

RECEIVED_RECORD = (
    (  1,  1, 'record_code', Const('2')),
    (  2,  3, 'model', Const('340')),
    (  5,  4, 'fiscalyear', Number),
    (  9,  9, 'nif', Char),
    ( 18,  9, 'party_nif', Char),
    ( 27,  9, 'representative_nif', Char),
    ( 36, 40, 'party_name', Char),
    ( 76,  2, 'party_country', Char),
    ( 78,  1, 'party_identifier_type', Number),
    ( 79, 20, 'party_identifier', Char),
    ( 99,  1, 'book_key', Char),
    (100,  1, 'operation_key', Char),
    (101,  8, 'issue_date', Date('%Y%m%d')),
    (109,  8, 'operation_date', Date('%Y%m%d')),
    (117,  5, 'tax_rate', Numeric(sign=SIGN_N)),
    (122, 14, 'base', Numeric(sign=SIGN_N)),
    (136, 14, 'tax', Numeric(sign=SIGN_N)),
    (150, 14, 'total', Numeric(sign=SIGN_N)),
    (164, 14, 'cost', Numeric(sign=SIGN_N)),
    (178, 40, 'invoice_number', Char),
    (218, 18, 'record_number', Char),
    # Received Invoices
    (236, 18, 'received_invoice_count', Integer),
    (254,  2, 'record_count', Integer),
    (256, 40, 'first_invoice_number', Char),
    (296, 40, 'last_invoice_number', Char),
    (336, 14, 'deducible_amount', Numeric(sign=SIGN_N)),
    )

INVESTMENT_RECORD = (
    (  1,  1, 'record_code', Const('2')),
    (  2,  3, 'model', Const('340')),
    (  5,  4, 'fiscalyear', Number),
    (  9,  9, 'nif', Char),
    ( 18,  9, 'party_nif', Char),
    ( 27,  9, 'representative_nif', Char),
    ( 36, 40, 'party_name', Char),
    ( 76,  2, 'party_country', Char),
    ( 78,  1, 'party_identifier_type', Number),
    ( 79, 20, 'party_identifier', Char),
    ( 99,  1, 'book_key', Char),
    (100,  1, 'operation_key', Char),
    (101,  8, 'issue_date', Date('%Y%m%d')),
    (109,  8, 'operation_date', Date('%Y%m%d')),
    (117,  5, 'tax_rate', Numeric(sign=SIGN_N)),
    (122, 14, 'base', Numeric(sign=SIGN_N)),
    (136, 14, 'tax', Numeric(sign=SIGN_N)),
    (150, 14, 'total', Numeric(sign=SIGN_N)),
    (164, 14, 'cost', Numeric(sign=SIGN_N)),
    (178, 40, 'invoice_number', Char),
    (218, 18, 'record_number', Char),
    # Investment goods
    (236,  3, 'pro_rata', Integer),
    (239, 14, 'yearly_regularization', Numeric(sign=SIGN_N)),
    (253, 40, 'submission_number', Char),
    (293, 14, 'transmissions', Numeric(sign=SIGN_N)),
    (307,  8, 'usage_start_date', Date('%Y%m%d')),
    (315, 17, 'good_identifier', Char),
    )

INTRACOMMUNITY_RECORD = (
    (  1,  1, 'record_code', Const('2')),
    (  2,  3, 'model', Const('340')),
    (  5,  4, 'fiscalyear', Number),
    (  9,  9, 'nif', Char),
    ( 18,  9, 'party_nif', Char),
    ( 27,  9, 'representative_nif', Char),
    ( 36, 40, 'party_name', Char),
    ( 76,  2, 'party_country', Char),
    ( 78,  1, 'party_identifier_type', Number),
    ( 79, 20, 'party_identifier', Char),
    ( 99,  1, 'book_key', Char),
    (100,  1, 'operation_key', Char),
    (101,  8, 'issue_date', Date('%Y%m%d')),
    (109,  8, 'operation_date', Date('%Y%m%d')),
    (117,  5, 'tax_rate', Numeric(sign=SIGN_N)),
    (122, 14, 'base', Numeric(sign=SIGN_N)),
    (136, 14, 'tax', Numeric(sign=SIGN_N)),
    (150, 14, 'total', Numeric(sign=SIGN_N)),
    (164, 14, 'cost', Numeric(sign=SIGN_N)),
    (178, 40, 'invoice_number', Char),
    (218, 18, 'record_number', Char),
    # Intracommunity operations (certain)
    (236,  1, 'intracommunity_operation_type', Number),
    (237,  1, 'declaring_key', Char),
    (238,  2, 'intracommunity_country', Char),
    (240,  3, 'operation_term', Number),
    (243, 35, 'goods_description', Char),
    (278, 40, 'party_street', Char),
    (278, 22, 'party_city', Char),
    (278, 10, 'party_zip', Char),
    (350, 135, 'other_documentation', Char),
    )

def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, PRESENTER_HEADER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if Record.valid(current_line, DETAIL_RECORD):
            record = Record.extract(current_line, DETAIL_RECORD)
        else:
            raise Exception('Invalid record: %s' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records

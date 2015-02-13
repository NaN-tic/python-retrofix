# encoding: utf8
##############################################################################
#
#    Copyright (C) 2013 NaN Projectes de Programari Lliure, S.L.
#                           http://www.NaN-tic.com
#    Copyright (C) 2015 Zikzakmedia S.L.
#                           http://www.zikzakmedia.com
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
    (  2,  3, 'model', Const('347')),
    (  5,  4, 'fiscalyear', Number),
    (  9,  9, 'nif', Char),
    ( 18, 40, 'presenter_name', Char),
    ( 58,  1, 'support_type', Char),
    ( 59,  9, 'contact_phone', Number(align='right')),
    ( 68, 40, 'contact_name', Char),
    (108, 13, 'declaration_number', Number(align='right')),
    (121,  1, 'complementary', Char),
    (122,  1, 'replacement', Char),
    (123, 13, 'previous_declaration_number', Number(align='right')),
    (136,  9, 'party_count', Integer),
    (145, 16, 'party_amount', Numeric(sign=SIGN_N)),
    (161,  9, 'property_count', Integer),
    (170, 16, 'property_amount', Numeric(sign=SIGN_N)),
    (391,  9, 'representative_nif', Char),
    (488, 13, 'digital_signature', Char),
    )

PARTY_RECORD = (
    (  1,  1, 'record_code', Const('2')),
    (  2,  3, 'model', Const('347')),
    (  5,  4, 'fiscalyear', Number),
    (  9,  9, 'nif', Char),
    ( 18,  9, 'party_nif', Char),
    ( 27,  9, 'representative_nif', Char),
    ( 36, 40, 'party_name', Char),
    ( 76,  1, 'sheet_type', Const('D')),
    ( 77,  2, 'province_code', Number),
    ( 79,  2, 'country_code', Char),
    ( 82,  1, 'operation_key', Char),
    ( 83, 16, 'amount', Numeric(sign=SIGN_N)),
    ( 99,  1, 'insurance', Boolean(BOOLEAN_X)),
    (100,  1, 'business_premises_rent', Boolean(BOOLEAN_X)),
    (101, 15, 'cash_amount', Numeric),
    (116, 16, 'vat_liable_property_amount', Numeric(sign=SIGN_N)),
    (132,  4, 'fiscalyear_cash_operation', Number(align='right')),
    (136, 16, 'first_quarter_amount', Numeric(sign=SIGN_N)),
    (152, 16, 'first_quarter_property_amount', Numeric(sign=SIGN_N)),
    (168, 16, 'second_quarter_amount', Numeric(sign=SIGN_N)),
    (184, 16, 'second_quarter_property_amount', Numeric(sign=SIGN_N)),
    (200, 16, 'third_quarter_amount', Numeric(sign=SIGN_N)),
    (216, 16, 'third_quarter_property_amount', Numeric(sign=SIGN_N)),
    (232, 16, 'fourth_quarter_amount', Numeric(sign=SIGN_N)),
    (248, 16, 'fourth_quarter_property_amount', Numeric(sign=SIGN_N)),
    (264, 17, 'community_vat', Char),
    (281,  1, 'cash_vat_operation', Boolean(BOOLEAN_X)),
    (282,  1, 'tax_person_operation', Boolean(BOOLEAN_X)),
    (283,  1, 'related_goods_operation', Boolean(BOOLEAN_X)),
    (284, 16, 'cash_vat_criteria', Numeric(sign=SIGN_N)),
    (300, 201, 'blank', Char),
    )

PROPERTY_RECORD = (
    (  1,  1, 'record_code', Const('2')),
    (  2,  3, 'model', Const('347')),
    (  5,  4, 'fiscalyear', Number),
    (  9,  9, 'nif', Char),
    ( 18,  9, 'party_nif', Char),
    ( 27,  9, 'representative_nif', Char),
    ( 36, 40, 'party_name', Char),
    ( 76,  1, 'sheet_type', Const('I')),
    (100, 15, 'amount', Numeric(sign=SIGN_POSITIVE)),
    (115,  1, 'situation', Number),
    (116, 25, 'cadaster_number', Char),
    (141,  5, 'road_type', Char),
    (146, 50, 'street', Char),
    (196,  3, 'number_type', Char),
    (199,  5, 'number', Number),
    (204,  3, 'number_qualifier', Char),
    (207,  3, 'block', Char),
    (210,  3, 'doorway', Char),
    (213,  3, 'stair', Char),
    (216,  3, 'floor', Char),
    (219,  3, 'door', Char),
    (222, 40, 'complement', Char),
    (262, 30, 'city', Char),
    (292, 30, 'municipality', Char),
    (322,  5, 'municipality_code', Char),
    (327,  2, 'province_code', Number),
    (329,  5, 'zip', Number),
    (334, 167, 'blank', Char),
    )


def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, PRESENTER_HEADER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if Record.valid(current_line, PARTY_RECORD):
            record = Record.extract(current_line, PARTY_RECORD)
        if Record.valid(current_line, PROPERTY_RECORD):
            record = Record.extract(current_line, PROPERTY_RECORD)
        else:
            raise Exception('Invalid record: %s' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records

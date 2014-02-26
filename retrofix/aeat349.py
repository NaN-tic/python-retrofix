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
    (  2,  3, 'model', Const('349')),
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
    (136,  2, 'period', Char),
    (138,  9, 'operation_count', Integer),
    (147, 15, 'operation_amount', Numeric()),
    (162,  9, 'ammendment_count', Integer),
    (171, 15, 'ammendment_amount', Numeric()),
    (391,  9, 'representative_nif', Char),
    (488, 13, 'digital_signature', Char),
    )

OPERATOR_RECORD = (
    (  1,  1, 'record_code', Const('2')),
    (  2,  3, 'model', Const('349')),
    (  5,  4, 'fiscalyear', Number),
    (  9,  9, 'nif', Char),
    ( 76, 17, 'party_vat', Char),
    ( 93, 40, 'party_name', Char),
    (133,  1, 'operation_key', Char),
    (134, 13, 'base', Numeric()),
    (147, 354, '',Char),
    )

AMMENDMENT_RECORD = (
    (  1,  1, 'record_code', Const('2')),
    (  2,  3, 'model', Const('349')),
    (  5,  4, 'fiscalyear', Number),
    (  9,  9, 'nif', Char),
    ( 76, 17, 'party_vat', Char),
    ( 93, 40, 'party_name', Char),
    (133,  1, 'operation_key', Char),
    (147,  4, 'ammendment_fiscalyear', Number),
    (151,  2, 'ammendment_period', Char),
    (153, 13, 'base', Numeric()),
    (166, 13, 'original_base', Numeric()),
    (179, 322, '', Char),
    )


def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, PRESENTER_HEADER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if Record.valid(current_line, OPERATOR_RECORD):
            record = Record.extract(current_line, OPERATOR_RECORD)
        if Record.valid(current_line, AMMENDMENT_RECORD):
            record = Record.extract(current_line, AMMENDMENT_RECORD)
        else:
            raise Exception('Invalid record: %s' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records

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

from .record import Record
from .fields import Const, Date, Number, Numeric, Char, Boolean
from .fields import BOOLEAN_12, SIGN_POSITIVE, SIGN_N, BOOLEAN_X


# DR111500
HEADER_RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('115')),
    (   6,  1, 'first_constant', Const('0')),
    (   7,  4, 'year', Number),
    (  11,  2, 'period', Char),
    (  13,  5, 'model_end', Const('0000>')),
    (  18,  5, 'open_aux', Const('<AUX>')),
    (  23, 70, 'first_reserved_for_administration', Char),
    (  93,  4, 'program_version', Const('0300')),
    (  97,  4, 'second_reserved_for_administration', Char),
    ( 101,  9, 'development_company_vat', Char),
    ( 110,213, 'third_reserved_for_administration', Char),
    ( 323,  6, 'close_aux', Const('</AUX>')),
    )

# DR11501
RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('115')),
    (   6,  2, 'page', Const('01')),
    (   8,  4, 'model_end', Const('000>')),
    (  12,  1, 'additional_page_indicator', Char),
    (  13,  1, 'type', Char),
    (  14,  9, 'company_vat', Char),
    (  23, 60, 'company_surname', Char),
    (  83, 20, 'company_name', Char),
    ( 103,  4, 'year', Number),
    ( 107,  2, 'period', Char),
    ( 109, 15, 'parties', Number),
    ( 124, 17, 'withholdings_payments_base', Numeric(sign=SIGN_POSITIVE)),
    ( 141, 17, 'withholdings_payments_amount', Numeric(sign=SIGN_POSITIVE)),
    ( 158, 17, 'to_deduce', Numeric(sign=SIGN_N)),
    ( 175, 17, 'result', Numeric(sign=SIGN_POSITIVE)),
    ( 192,  1, 'complementary_declaration', Boolean(BOOLEAN_X)),
    ( 193, 13, 'previous_declaration_receipt', Char),
    ( 206, 34, 'bank_account', Char),
    ( 240,236, 'reserved_aeat', Char),
    ( 476, 13, 'reserved_aeat_electronic_stamp', Char),
    ( 489, 12, 'record_end_id', Const('</T11501000>')),
)

FOOTER_RECORD = (
    (   1,  3, 'model_close_start', Const('</T')),
    (   4,  3, 'model', Const('115')),
    (   7,  1, 'first_constant', Const('0')),
    (   8,  4, 'year', Number),
    (  12,  2, 'period', Char),
    (  14,  5, 'model_close_end', Const('0000>')),
    )


def read(data):
    lines = data.splitlines()
    records = []
    current_line = lines.pop(0)
    records.append(Record.extract(current_line, RECORD))
    return records

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


# M11100
HEADER_RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('111')),
    (   6,  1, 'first_constant', Const('0')),
    (   7,  4, 'year', Number),
    (  11,  2, 'period', Char),
    (  13,  5, 'model_end', Const('0000>')),
    (  18,  5, 'open_aux', Const('<AUX>')),
    (  23, 70, 'first_reserved_for_administration', Char),
    (  93,  4, 'program_version', Const('0302')),
    (  97,  4, 'second_reserved_for_administration', Char),
    ( 101,  9, 'development_company_vat', Char),
    ( 110,213, 'third_reserved_for_administration', Char),
    ( 323,  6, 'close_aux', Const('</AUX>')),
    )

# DRM11101
RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('111')),
    (   6,  2, 'page', Const('01')),
    (   8,  4, 'model_end', Const('000>')),
    (  12,  1, 'additional_page_indicator', Char),
    (  13,  1, 'type', Char),
    (  14,  9, 'company_vat', Char),
    (  23, 60, 'company_surname', Char),
    (  83, 20, 'company_name', Char),
    ( 103,  4, 'year', Number),
    ( 107,  2, 'period', Char),
    ( 109,  8, 'work_productivity_monetary_parties', Number),
    ( 117, 17, 'work_productivity_monetary_payments',
        Numeric(sign=SIGN_POSITIVE)),
    ( 134, 17, 'work_productivity_monetary_withholdings_amount',
        Numeric(sign=SIGN_POSITIVE)),
    ( 151,  8, 'work_productivity_in_kind_parties', Number),
    ( 159, 17, 'work_productivity_in_kind_value_benefits',
        Numeric(sign=SIGN_POSITIVE)),
    ( 176, 17, 'work_productivity_in_kind_payments_amount',
        Numeric(sign=SIGN_POSITIVE)),
    ( 193,  8, 'economic_activities_productivity_monetary_parties', Number),
    ( 201, 17, 'economic_activities_productivity_monetary_payments',
        Numeric(sign=SIGN_POSITIVE)),
    ( 218, 17, 'economic_activities_productivity_monetary_withholdings_amount',
        Numeric(sign=SIGN_POSITIVE)),
    ( 235,  8, 'economic_activities_productivity_in_kind_parties', Number),
    ( 243, 17, 'economic_activities_productivity_in_kind_value_benefits',
        Numeric(sign=SIGN_POSITIVE)),
    ( 260, 17, 'economic_activities_productivity_in_kind_payments_amount',
        Numeric(sign=SIGN_POSITIVE)),
    ( 277,  8, 'awards_monetary_parties', Number),
    ( 285, 17, 'awards_monetary_payments',
        Numeric(sign=SIGN_POSITIVE)),
    ( 302, 17, 'awards_monetary_withholdings_amount',
        Numeric(sign=SIGN_POSITIVE)),
    ( 319,  8, 'awards_in_kind_parties', Number),
    ( 327, 17, 'awards_in_kind_value_benefits',
        Numeric(sign=SIGN_POSITIVE)),
    ( 344, 17, 'awards_in_kind_payments_amount',
        Numeric(sign=SIGN_POSITIVE)),
    ( 361,  8, 'gains_forestry_exploitation_monetary_parties', Number),
    ( 369, 17, 'gains_forestry_exploitation_monetary_payments',
        Numeric(sign=SIGN_POSITIVE)),
    ( 386, 17, 'gains_forestry_exploitation_monetary_withholdings_amount',
        Numeric(sign=SIGN_POSITIVE)),
    ( 403,  8, 'gains_forestry_exploitation_in_kind_parties', Number),
    ( 411, 17, 'gains_forestry_exploitation_in_kind_value_benefits',
        Numeric(sign=SIGN_POSITIVE)),
    ( 428, 17, 'gains_forestry_exploitation_in_kind_payments_amount',
        Numeric(sign=SIGN_POSITIVE)),
    ( 445,  8, 'image_rights_parties', Number),
    ( 453, 17, 'image_rights_service_payments', Numeric(sign=SIGN_POSITIVE)),
    ( 470, 17, 'image_rights_payments_amount', Numeric(sign=SIGN_POSITIVE)),
    ( 487, 17, 'withholdings_payments_amount', Numeric(sign=SIGN_POSITIVE)),
    ( 504, 17, 'to_deduce', Numeric(sign=SIGN_N)),
    ( 521, 17, 'result', Numeric(sign=SIGN_POSITIVE)),
    ( 538,  1, 'complementary_declaration', Boolean(BOOLEAN_X)),
    ( 539, 13, 'previous_declaration_receipt', Char),
    ( 552,  1, 'reservet_aeat_private_school_declaration',
        Boolean(BOOLEAN_X)),
    ( 553, 34, 'bank_account', Char),
    ( 587,389, 'reserved_aeat', Char),
    ( 976, 13, 'reserved_aeat_electronic_stamp', Char),
    ( 989, 12, 'record_end_id', Const('</T11501000>')),
)

FOOTER_RECORD = (
    (   1,  3, 'model_close_start', Const('</T')),
    (   4,  3, 'model', Const('111')),
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

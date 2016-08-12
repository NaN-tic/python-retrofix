# encoding: utf8
##############################################################################
#
#    Copyright (C) 2016 Zikzakmedia S.L. http://www.zikzakmedia.com
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
from .fields import Char, Const, Integer, Number, Numeric
from .fields import SIGN_N


PRESENTER_RECORD = (
    (  1,  1, 'record_code', Const('1')),
    (  2,  3, 'model', Const('182')),
    (  5,  4, 'fiscalyear_code', Number(align='right')),
    (  9,  9, 'company_vat', Char),
    ( 18, 40, 'company_name', Char),
    ( 58,  1, 'support_type', Char),
    ( 59,  9, 'company_phone', Number(align='right')),
    ( 68, 40, 'contact_name', Char),
    (108, 13, 'declaration_number', Number(align='right')),
    (121,  1, 'complementary', Char),
    (122,  1, 'substitutive', Char),
    (123, 13, 'previous_number', Number(align='right')),
    (136,  9, 'total_number_of_donor_records', Integer),
    (145, 15, 'amount_of_donations', Numeric(sign=SIGN_N)),
    (160,  1, 'declarant_nature', Number(align='right')),
    (161,  9, 'protected_heritage_vat', Char),
    (170, 31, 'protected_heritage_name', Char),
    (238, 12, 'digital_signature', Char),
    )

PARTY_RECORD = (
    (  1,  1, 'record_code', Const('2')),
    (  2,  3, 'model', Const('182')),
    (  5,  4, 'fiscalyear_code', Number(align='right')),
    (  9,  9, 'company_vat', Char),
    ( 18,  9, 'party_vat', Char),
    ( 27,  9, 'representative_vat', Char),
    ( 36, 40, 'party_name', Char),
    ( 76,  2, 'party_subdivision_code', Number(align='right')),
    ( 78,  1, 'key', Char),
    ( 79,  5, 'percentage_deduction', Number(align='right')),
    ( 84, 13, 'amount', Numeric(sign=SIGN_N)),
    ( 97,  1, 'donation_in_kind', Char),
    ( 98,  2, 'deduction_autonomous_community', Number(align='right')),
    (100,  5, 'percentage_deduction_autonomous_community', Number(align='right')),
    (105,  1, 'nature', Char),
    (106,  1, 'revocation', Char),
    (107,  4, 'exercise_of_the_revoked_donation', Number(align='right')),
    (111,  1, 'type_of_good', Char),
    (112,138, 'identification_of_good', Char),
    )


def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, PRESENTER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if Record.valid(current_line, PARTY_RECORD):
            record = Record.extract(current_line, PARTY_RECORD)
        else:
            raise Exception('Invalid record: %s' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records

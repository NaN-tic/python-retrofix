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


RECORD = (
    (  1,  2, 'model_start', Const('<T')),
    (  3,  3, 'model', Const('303')),
    (  6,  2, 'page', Const('01')),
    (  8,  1, 'model_end', Const('>')),
    ( 10,  1, 'declaration_type', Char),
    ( 11,  9, 'nif', Char),
    ( 20, 30, 'company_name', Char),
    ( 50, 15, 'first_name', Char),
    ( 65,  1, 'monthly_return_subscription', Char),
    ( 66,  4, 'fiscalyear', Number),
    ( 70,  2, 'period', Char),
    ( 72, 17, 'accrued_vat_base_1', Numeric(sign=SIGN_N)),
    ( 89,  5, 'accrued_vat_percent_1', Numeric(sign=SIGN_N)),
    ( 94, 17, 'accrued_vat_tax_1', Numeric(sign=SIGN_N)),
    (111, 17, 'accrued_vat_base_2', Numeric(sign=SIGN_N)),
    (128,  5, 'accrued_vat_percent_2', Numeric(sign=SIGN_N)),
    (133, 17, 'accrued_vat_tax_2', Numeric(sign=SIGN_N)),
    (150, 17, 'accrued_vat_base_3', Numeric(sign=SIGN_N)),
    (167,  5, 'accrued_vat_percent_3', Numeric(sign=SIGN_N)),
    (172, 17, 'accrued_vat_tax_3', Numeric(sign=SIGN_N)),
    (189, 17, 'accrued_re_base_1', Numeric(sign=SIGN_N)),
    (206,  5, 'accrued_re_percent_1', Numeric(sign=SIGN_N)),
    (211, 17, 'accrued_re_tax_1', Numeric(sign=SIGN_N)),
    (228, 17, 'accrued_re_base_2', Numeric(sign=SIGN_N)),
    (245,  5, 'accrued_re_percent_2', Numeric(sign=SIGN_N)),
    (250, 17, 'accrued_re_tax_2', Numeric(sign=SIGN_N)),
    (267, 17, 'accrued_re_base_3', Numeric(sign=SIGN_N)),
    (284,  5, 'accrued_re_percent_3', Numeric(sign=SIGN_N)),
    (289, 17, 'accrued_re_tax_3', Numeric(sign=SIGN_N)),
    (306, 17, 'intracommunity_adquisitions_base', Numeric(sign=SIGN_N)),
    (323, 17, 'intracommunity_adquisitions_tax', Numeric(sign=SIGN_N)),
    (340, 17, 'accrued_total_tax', Numeric(sign=SIGN_N)),
    (357, 17, 'deductible_current_domestic_operations_base', Numeric(sign=SIGN_N)),
    (374, 17, 'deductible_current_domestic_operations_tax', Numeric(sign=SIGN_N)),
    (391, 17, 'deductible_investment_domestic_operations_base', Numeric(sign=SIGN_N)),
    (408, 17, 'deductible_investment_domestic_operations_tax', Numeric(sign=SIGN_N)),
    (425, 17, 'deductible_current_import_operations_base', Numeric(sign=SIGN_N)), # [26]
    (442, 17, 'deductible_current_import_operations_tax', Numeric(sign=SIGN_N)),
    (459, 17, 'deductible_investment_import_operations_base', Numeric(sign=SIGN_N)),
    (476, 17, 'deductible_investment_import_operations_tax', Numeric(sign=SIGN_N)),
    (493, 17, 'deductible_current_intracommunity_operations_base', Numeric(sign=SIGN_N)),
    (510, 17, 'deductible_current_intracommunity_operations_tax', Numeric(sign=SIGN_N)),
    (527, 17, 'deductible_investment_intracommunity_operations_base', Numeric(sign=SIGN_N)),
    (544, 17, 'deductible_investment_intracommunity_operations_tax', Numeric(sign=SIGN_N)),
    (561, 17, 'deductible_compensations', Numeric(sign=SIGN_N)),
    (578, 17, 'deductible_investment_regularization', Numeric(sign=SIGN_N)),
    (595, 17, 'deductible_pro_rata_regularization', Numeric(sign=SIGN_N)),
    (612, 17, 'deductible_total', Numeric(sign=SIGN_N)),
    (629, 17, 'difference', Numeric(sign=SIGN_N)), # [38]
    (646,  5, 'state_administration_percent', Numeric(sign=SIGN_N)),
    (651, 17, 'state_administration_amount', Numeric(sign=SIGN_N)),
    (668, 17, 'previous_period_amount_to_compensate', Numeric(sign=SIGN_N)),
    (685, 17, 'intracommunity_deliveries', Numeric(sign=SIGN_N)), # [42]
    (702, 17, 'exports', Numeric(sign=SIGN_N)), # [43]
    (719, 17, 'not_subject_or_reverse_charge', Numeric(sign=SIGN_N)), # [44]
    (736, 17, 'joint_taxation_state_provincial_councils', Numeric(sign=SIGN_N)), # [45]
    (753, 17, 'result', Numeric(sign=SIGN_N)), # [46]
    (770, 17, 'to_deduce', Numeric(sign=SIGN_N)), # [47]
    (787, 17, 'liquidation_result', Numeric(sign=SIGN_N)), # [48]
    (804, 17, 'amount_to_compensate', Numeric(sign=SIGN_N)), # [49]
    (821,  1, 'without_activity', Char),
    (822, 17, 'refund_amount', Numeric(sign=SIGN_N)), # [50]
    (839, 20, 'refund_bank_account', Numeric(sign=SIGN_N)),
    (859, 1, 'payment_type', Number),
    (860, 17, 'payment_amount', Numeric(sign=SIGN_N)),
    (877, 20, 'payment_bank_account', Char),
    (897, 1, 'complementary_autoliquidation', Number),
    (898, 13, 'previous_declaration_receipt', Number),
    (911, 1, 'joint_presentation_allowed', Char),
    (912, 1, 'auto_bankruptcy_declaration', Char),
    (913, 398, 'reserved', Char),
    (1311, 16, 'signature_city', Char),
    (1327,  2, 'signature_day', Char),
    (1329, 10, 'signature_month', Char),
    (1339,  4, 'signature_year', Char),
    (1343,  9, 'record_end_id', Const('</T30301>')),
    (1352,  2, 'record_end', Const('\r\n')),
    )


def read(data):
    lines = data.splitlines()
    records = []
    current_line = lines.pop(0)
    records.append(Record.extract(current_line, RECORD))
    return records

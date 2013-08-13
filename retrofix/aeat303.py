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

from lowlevel import extract_record, valid_record

# TODO: Implement numbers without the _sign field
RECORD = (
    (  1,  2, 'model_start', 'A', '=<T'),
    (  3,  3, 'model', 'N', '=303'),
    (  6,  2, 'page', 'N', '=01'),
    (  8,  1, 'model_end', 'A', '>'),
    ( 10,  1, 'declaration_type', 'A'),
    ( 11,  9, 'nif', 'A'),
    ( 20, 30, 'company_name', 'A'),
    ( 50, 15, 'first_name', 'A'),
    ( 65,  1, 'monthly_return_subscription', 'A'),
    ( 66,  4, 'fiscalyear', 'N'),
    ( 70,  2, 'period', 'A'),
    ( 72, 17, 'accrued_vat_base_1', 'N', '2'),
    ( 89,  5, 'accrued_vat_percent_1', 'N', '2'),
    ( 94, 17, 'accrued_vat_tax_1', 'N', '2'),
    (111, 17, 'accrued_vat_base_2', 'N', '2'),
    (128,  5, 'accrued_vat_percent_2', 'N', '2'),
    (133, 17, 'accrued_vat_tax_2', 'N', '2'),
    (150, 17, 'accrued_vat_base_3', 'N', '2'),
    (167,  5, 'accrued_vat_percent_3', 'N', '2'),
    (172, 17, 'accrued_vat_tax_3', 'N', '2'),
    (189, 17, 'accrued_re_base_1', 'N', '2'),
    (206,  5, 'accrued_re_percent_1', 'N', '2'),
    (211, 17, 'accrued_re_tax_1', 'N', '2'),
    (228, 17, 'accrued_re_base_2', 'N', '2'),
    (245,  5, 'accrued_re_percent_2', 'N', '2'),
    (250, 17, 'accrued_re_tax_2', 'N', '2'),
    (267, 17, 'accrued_re_base_3', 'N', '2'),
    (284,  5, 'accrued_re_percent_3', 'N', '2'),
    (289, 17, 'accrued_re_tax_3', 'N', '2'),
    (306, 17, 'intracommunity_adquisitions_base', 'N', '2'),
    (323, 17, 'intracommunity_adquisitions_tax', 'N', '2'),
    (340, 17, 'accrued_total_tax', 'N', '2'),
    (357, 17, 'deductible_current_domestic_operations_base', 'N', '2'),
    (374, 17, 'deductible_current_domestic_operations_tax', 'N', '2'),
    (391, 17, 'deductible_investment_domestic_operations_base', 'N', '2'),
    (408, 17, 'deductible_investment_domestic_operations_tax', 'N', '2'),
    (425, 17, 'deductible_current_import_operations_base', 'N', '2'), # [26]
    (442, 17, 'deductible_current_import_operations_tax', 'N', '2'),
    (459, 17, 'deductible_investment_import_operations_base', 'N', '2'),
    (476, 17, 'deductible_investment_import_operations_tax', 'N', '2'),
    (493, 17, 'deductible_current_intracommunity_operations_base', 'N', '2'),
    (510, 17, 'deductible_current_intracommunity_operations_tax', 'N', '2'),
    (527, 17, 'deductible_investment_intracommunity_operations_base', 'N', '2'),
    (544, 17, 'deductible_investment_intracommunity_operations_tax', 'N', '2'),
    (561, 17, 'deductible_compensations', 'N', '2'),
    (578, 17, 'deductible_investment_regularization', 'N', '2'),
    (595, 17, 'deductible_pro_rata_regularization', 'N', '2'),
    (612, 17, 'deductible_total', 'N', '2'),
    (629, 17, 'difference', 'N', '2'), # [38]
    (646,  5, 'state_administration_percent', 'N', '2'),
    (651, 17, 'state_administration_amount', 'N', '2'),
    (668, 17, 'previous_period_amount_to_compensate', 'N', '2'),
    (685, 17, 'intracommunity_deliveries', 'N', '2'), # [42]
    (702, 17, 'exports', 'N', '2'), # [43]
    (719, 17, 'not_subject_or_reverse_charge', 'N', '2'), # [44]
    (736, 17, 'joint_taxation_state_provincial_councils', 'N', '2'), # [45]
    (753, 17, 'result', 'N', '2'), # [46]
    (770, 17, 'to_deduce', 'N', '2'), # [47]
    (787, 17, 'liquidation_result', 'N', '2'), # [48]
    (804, 17, 'amount_to_compensate', 'N', '2'), # [49]
    (821,  1, 'without_activity', 'N', '2'),
    (822, 17, 'refund_amount', 'N', '2'), # [50]
    (839, 20, 'refund_bank_account', 'N', '2'),
    (859, 1, 'payment_type', 'N', '2'),
    (860, 17, 'payment_amount', 'N', '2'),
    (877, 20, 'payment_bank_account', 'A'),
    (897, 1, 'complementary_autoliquidation', 'N', '2'),
    (898, 17, 'previous_declaration_receipt', 'N', '2'),
    (911, 1, 'joint_presentation_allowed', 'N', '2'),
    (912, 1, 'auto_bankruptcy_declaration', 'N', '2'),
    (913, 398, 'reserved', 'N', '2'),
    (1311, 16, 'signature_city', 'N', '2'),
    (1327,  2, 'signature_day', 'A'),
    (1329, 10, 'signature_month', 'A'),
    (1339,  4, 'signature_year', 'A'),
    (1343,  9, 'record_end_id', 'A', '=</T30301>'),
    (1352,  2, 'record_end', 'A', '=\r\n'),
    )


def read(data):
    lines = data.splitlines()
    records = []
    current_line = lines.pop(0)
    records.append(extract_record(current_line, RECORD))
    return records

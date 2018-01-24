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


# DP30300
HEADER_RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  1, 'first_constant', Const('0')),
    (   7,  4, 'fiscalyear', Number),
    (  11,  2, 'period', Char),
    (  13,  5, 'model_end', Const('0000>')),
    (  18,  5, 'open_aux', Const('<AUX>')),
    (  23, 70, 'first_reserved_for_administration', Char),
    (  93,  4, 'program_version', Char),
    (  97,  4, 'second_reserved_for_administration', Char),
    ( 101,  9, 'development_company_vat', Char),
    ( 110,213, 'third_reserved_for_administration', Char),
    ( 323,  6, 'close_aux', Const('</AUX>')),
    )

FOOTER_RECORD = (
    (   1,  3, 'model_close_start', Const('</T')),
    (   4,  3, 'model', Const('303')),
    (   7,  1, 'first_constant', Const('0')),
    (   8,  4, 'fiscalyear', Number),
    (  12,  2, 'period', Char),
    (  14,  5, 'model_close_end', Const('0000>')),
    (  19,  2, 'record_end', Const('\r\n')),
    )

# DP30301
RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  5, 'page', Const('01000')),
    (  11,  1, 'model_end', Const('>')),
    (  12,  1, 'additional_page_indicator', Char),
    (  13,  1, 'type', Char),
    (  14,  9, 'company_vat', Char),
    (  23, 60, 'company_name', Char),
    (  83, 20, 'first_name', Char),
    ( 103,  4, 'fiscalyear', Number),
    ( 107,  2, 'period', Char),
    ( 109,  1, 'monthly_return_subscription', Boolean(BOOLEAN_12)),
    ( 110,  1, 'regime_type', Number),
    ( 111,  1, 'joint_liquidation', Boolean(BOOLEAN_12)),
    ( 112,  1, 'bankruptcy', Boolean(BOOLEAN_12)),
    ( 113,  8, 'auto_bankruptcy_date', Date('%Y%m%d')),
    ( 121,  1, 'auto_bankruptcy_declaration', Char),
    ( 122,  1, 'recc', Boolean(BOOLEAN_12)),
    ( 123,  1, 'recc_receiver', Boolean(BOOLEAN_12)),
    ( 124,  1, 'special_prorate', Boolean(BOOLEAN_12)),
    ( 125,  1, 'special_prorate_revocation', Boolean(BOOLEAN_12)),
    ( 126, 17, 'accrued_vat_base_1', Numeric(sign=SIGN_POSITIVE)),
    ( 143,  5, 'accrued_vat_percent_1', Numeric(sign=SIGN_POSITIVE)),
    ( 148, 17, 'accrued_vat_tax_1', Numeric(sign=SIGN_POSITIVE)),
    ( 165, 17, 'accrued_vat_base_2', Numeric(sign=SIGN_POSITIVE)),
    ( 182,  5, 'accrued_vat_percent_2', Numeric(sign=SIGN_POSITIVE)),
    ( 187, 17, 'accrued_vat_tax_2', Numeric(sign=SIGN_POSITIVE)),
    ( 204, 17, 'accrued_vat_base_3', Numeric(sign=SIGN_POSITIVE)),
    ( 221,  5, 'accrued_vat_percent_3', Numeric(sign=SIGN_POSITIVE)),
    ( 226, 17, 'accrued_vat_tax_3', Numeric(sign=SIGN_POSITIVE)),
    ( 243, 17, 'intracommunity_adquisitions_base', Numeric(sign=SIGN_POSITIVE)),
    ( 260, 17, 'intracommunity_adquisitions_tax', Numeric(sign=SIGN_POSITIVE)),
    ( 277, 17, 'other_passive_subject_base', Numeric(sign=SIGN_POSITIVE)),
    ( 294, 17, 'other_passive_subject_tax', Numeric(sign=SIGN_POSITIVE)),
    ( 311, 17, 'accrued_vat_base_modification', Numeric(sign=SIGN_N)),
    ( 328, 17, 'accrued_vat_tax_modification', Numeric(sign=SIGN_N)),
    ( 345, 17, 'accrued_re_base_1', Numeric(sign=SIGN_POSITIVE)),
    ( 362,  5, 'accrued_re_percent_1', Numeric(sign=SIGN_POSITIVE)),
    ( 367, 17, 'accrued_re_tax_1', Numeric(sign=SIGN_POSITIVE)),
    ( 384, 17, 'accrued_re_base_2', Numeric(sign=SIGN_POSITIVE)),
    ( 401,  5, 'accrued_re_percent_2', Numeric(sign=SIGN_POSITIVE)),
    ( 406, 17, 'accrued_re_tax_2', Numeric(sign=SIGN_POSITIVE)),
    ( 423, 17, 'accrued_re_base_3', Numeric(sign=SIGN_POSITIVE)),
    ( 440,  5, 'accrued_re_percent_3', Numeric(sign=SIGN_POSITIVE)),
    ( 445, 17, 'accrued_re_tax_3', Numeric(sign=SIGN_POSITIVE)),
    ( 462, 17, 'accrued_re_base_modification', Numeric(sign=SIGN_N)),
    ( 479, 17, 'accrued_re_tax_modification', Numeric(sign=SIGN_N)),
    ( 496, 17, 'accrued_total_tax', Numeric(sign=SIGN_N)),
    ( 513, 17, 'deductible_current_domestic_operations_base',
         Numeric(sign=SIGN_POSITIVE)),
    ( 530, 17, 'deductible_current_domestic_operations_tax',
         Numeric(sign=SIGN_POSITIVE)),
    ( 547, 17, 'deductible_investment_domestic_operations_base',
         Numeric(sign=SIGN_POSITIVE)),
    ( 564, 17, 'deductible_investment_domestic_operations_tax',
         Numeric(sign=SIGN_POSITIVE)),
    ( 581, 17, 'deductible_current_import_operations_base',
         Numeric(sign=SIGN_POSITIVE)),
    ( 598, 17, 'deductible_current_import_operations_tax',
         Numeric(sign=SIGN_POSITIVE)),
    ( 615, 17, 'deductible_investment_import_operations_base',
         Numeric(sign=SIGN_POSITIVE)),
    ( 632, 17, 'deductible_investment_import_operations_tax',
         Numeric(sign=SIGN_POSITIVE)),
    ( 649, 17, 'deductible_current_intracommunity_operations_base',
         Numeric(sign=SIGN_POSITIVE)),
    ( 666, 17, 'deductible_current_intracommunity_operations_tax',
         Numeric(sign=SIGN_POSITIVE)),
    ( 683, 17, 'deductible_investment_intracommunity_operations_base',
         Numeric(sign=SIGN_POSITIVE)),
    ( 700, 17, 'deductible_investment_intracommunity_operations_tax',
         Numeric(sign=SIGN_POSITIVE)),
    ( 717, 17, 'deductible_regularization_base', Numeric(sign=SIGN_N)),
    ( 734, 17, 'deductible_regularization_tax', Numeric(sign=SIGN_N)),
    ( 751, 17, 'deductible_compensations', Numeric(sign=SIGN_N)),
    ( 768, 17, 'deductible_investment_regularization', Numeric(sign=SIGN_N)),
    ( 785, 17, 'deductible_pro_rata_regularization', Numeric(sign=SIGN_N)),
    ( 802, 17, 'deductible_total', Numeric(sign=SIGN_N)),
    ( 819, 17, 'general_regime_result', Numeric(sign=SIGN_N)),
    ( 836,  1, 'exonerated_mod390', Number),
    ( 837,581, 'reserved_aeat', Char),
    (1418, 13, 'reserved_aeat_electronic_stamp', Char),
    (1431, 12, 'record_end_id', Const('</T30301000>')),
)

# This is used for the 'modulos'.
SIMPLIFIED_RECORD = ()

# DP30303
ADDITIONAL_RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  5, 'page', Const('03000')),
    (  11,  1, 'model_end', Const('>')),
    (  12, 17, 'intracommunity_deliveries', Numeric(sign=SIGN_N)),
    (  29, 17, 'exports', Numeric(sign=SIGN_N)),
    (  46, 17, 'not_subject_or_reverse_charge', Numeric(sign=SIGN_N)),
    (  63, 17, 'recc_deliveries_base', Numeric(sign=SIGN_N)),
    (  80, 17, 'recc_deliveries_tax', Numeric(sign=SIGN_N)),
    (  97, 17, 'recc_adquisitions_base', Numeric(sign=SIGN_N)),
    ( 114, 17, 'recc_adquisitions_tax', Numeric(sign=SIGN_N)),
    ( 131, 17, 'result_tax_regularitzation', Numeric(sign=SIGN_N)),
    ( 148, 17, 'sum_results', Numeric(sign=SIGN_N)),
    ( 165,  5, 'state_administration_percent', Numeric(decimals=2)),
    ( 170,  4, 'reserved_aeat', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 174, 17, 'state_administration_amount', Numeric(sign=SIGN_N)),
    ( 191, 17, 'aduana_tax_pending', Numeric(sign=SIGN_N)),
    ( 208, 17, 'previous_period_amount_to_compensate', Numeric(sign=SIGN_N)),
    ( 225, 17, 'joint_taxation_state_provincial_councils',
         Numeric(sign=SIGN_N)),
    ( 242, 17, 'result', Numeric(sign=SIGN_N)),
    ( 259, 17, 'to_deduce', Numeric(sign=SIGN_N)),
    ( 276, 17, 'liquidation_result', Numeric(sign=SIGN_N)),
    ( 293,  1, 'complementary_declaration', Boolean(BOOLEAN_X)),
    ( 294, 13, 'previous_declaration_receipt', Char),
    ( 307,  1, 'without_activity', Boolean(BOOLEAN_X)),
    ( 308, 11, 'swift_bank', Char),
    ( 319, 34, 'bank_account', Char),
    ( 353,  1, 'special_info_key_main', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 354,  4, 'special_info_section_iae_main', Char),
    ( 358,  1, 'special_info_key_others_1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 359,  4, 'special_info_section_iae_others_1', Char),
    ( 363,  1, 'special_info_key_others_2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 364,  4, 'special_info_section_iae_others_2', Char),
    ( 368,  1, 'special_info_key_others_3', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 369,  4, 'special_info_section_iae_others_3', Char),
    ( 373,  1, 'special_info_key_others_4', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 374,  4, 'special_info_section_iae_others_4', Char),
    ( 378,  1, 'special_info_key_others_5', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 379,  4, 'special_info_section_iae_others_5', Char),
    ( 383,  1, 'special_info_required_declare_third_party_operation', Boolean(BOOLEAN_X)),
    ( 384, 17, 'special_info_rg_operations', Numeric(sign=SIGN_N)),
    ( 401, 17, 'special_info_recc', Numeric(sign=SIGN_N)),
    ( 418, 17, 'special_info_export_intracomunitari_out_2bdeduced', Numeric(sign=SIGN_N)),
    ( 435, 17, 'special_info_exempt_op_wo_permission 2bdeduced', Numeric(sign=SIGN_N)),
    ( 452, 17, 'special_info_w_passive_subject', Numeric(sign=SIGN_N)),
    ( 469, 17, 'special_info_delivery_need_install_object_in_other_eu_country', Numeric(sign=SIGN_N)),
    ( 486, 17, 'special_info_operations_rs', Numeric(sign=SIGN_N)),
    ( 503, 17, 'special_info_financial_op_not_usual', Numeric(sign=SIGN_N)),
    ( 520, 17, 'special_info_total', Numeric(sign=SIGN_N)),
    ( 537,  1, 'reserved_aeat2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 538,  5, 'info_territory_alava', Numeric(decimals=2)),
    ( 543,  5, 'info_territory_guipuzcoa', Numeric(decimals=2)),
    ( 548,  5, 'info_territory_vizcaya', Numeric(decimals=2)),
    ( 553,  5, 'info_territory_navarra', Numeric(decimals=2)),
    ( 558, 17, 'special_info_exempt_op_2bdeduced', Numeric(sign=SIGN_N)),
    ( 575, 17, 'special_info_farming_cattleraising_fishing', Numeric(sign=SIGN_N)),
    ( 592, 17, 'special_info_passive_subject_re', Numeric(sign=SIGN_N)),
    ( 609, 17, 'special_info_art_antiques_collectibles', Numeric(sign=SIGN_N)),
    ( 626, 17, 'special_info_travel_agency', Numeric(sign=SIGN_N)),
    ( 643, 17, 'special_info_delivery_investment_domestic_operations', Numeric(sign=SIGN_N)),
    ( 660,468, 'reserved_aeat3', Char),
    (1128, 12, 'record_end_id', Const('</T30303000>')),
    )


def read(data):
    lines = data.splitlines()
    records = []
    current_line = lines.pop(0)
    records.append(Record.extract(current_line, RECORD))
    return records

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

# DP30301
RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  5, 'page', Const('01000')),
    (  11,  1, 'model_end', Const('>')),
    (  12,  1, 'additional_page_indicator', Char),
    (  13,  1, 'type', Char),
    (  14,  9, 'company_vat', Char),
    (  23, 80, 'company_name', Char),
    ( 103,  4, 'year', Number),
    ( 107,  2, 'period', Char),
    ( 109,  1, 'passive_subject_foral_administration', Number),
    ( 110,  1, 'monthly_return_subscription', Boolean(BOOLEAN_12)),
    ( 111,  1, 'regime_type', Number),
    ( 112,  1, 'joint_liquidation', Boolean(BOOLEAN_12)),
    ( 113,  1, 'recc', Boolean(BOOLEAN_12)),
    ( 114,  1, 'recc_receiver', Boolean(BOOLEAN_12)),
    ( 115,  1, 'special_prorate', Boolean(BOOLEAN_12)),
    ( 116,  1, 'special_prorate_revocation', Boolean(BOOLEAN_12)),
    ( 117,  1, 'bankruptcy', Boolean(BOOLEAN_12)),
    ( 118,  8, 'auto_bankruptcy_date', Date('%d%m%Y')),
    ( 126,  1, 'auto_bankruptcy_declaration', Char),
    ( 127,  1, 'passive_subject_voluntarily_sii', Number),
    ( 128,  1, 'exonerated_mod390', Number),
    ( 129,  1, 'annual_operation_volume', Number),
    ( 130, 17, 'accrued_vat_base_0', Numeric(sign=SIGN_POSITIVE)),
    ( 147,  5, 'accrued_vat_percent_0', Numeric(sign=SIGN_POSITIVE)),
    ( 152, 17, 'accrued_vat_tax_0', Numeric(sign=SIGN_POSITIVE)),
    ( 169, 17, 'accrued_vat_base_1', Numeric(sign=SIGN_POSITIVE)),
    ( 186,  5, 'accrued_vat_percent_1', Numeric(sign=SIGN_POSITIVE)),
    ( 191, 17, 'accrued_vat_tax_1', Numeric(sign=SIGN_POSITIVE)),
    ( 208, 17, 'accrued_vat_base_4', Numeric(sign=SIGN_POSITIVE)),
    ( 225,  5, 'accrued_vat_percent_4', Numeric(sign=SIGN_POSITIVE)),
    ( 230, 17, 'accrued_vat_tax_4', Numeric(sign=SIGN_POSITIVE)),
    ( 247, 17, 'accrued_vat_base_2', Numeric(sign=SIGN_POSITIVE)),
    ( 264,  5, 'accrued_vat_percent_2', Numeric(sign=SIGN_POSITIVE)),
    ( 269, 17, 'accrued_vat_tax_2', Numeric(sign=SIGN_POSITIVE)),
    ( 286, 17, 'accrued_vat_base_3', Numeric(sign=SIGN_POSITIVE)),
    ( 303,  5, 'accrued_vat_percent_3', Numeric(sign=SIGN_POSITIVE)),
    ( 308, 17, 'accrued_vat_tax_3', Numeric(sign=SIGN_POSITIVE)),
    ( 325, 17, 'intracommunity_adquisitions_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 342, 17, 'intracommunity_adquisitions_tax', Numeric(sign=SIGN_POSITIVE)),
    ( 359, 17, 'other_passive_subject_base', Numeric(sign=SIGN_POSITIVE)),
    ( 376, 17, 'other_passive_subject_tax', Numeric(sign=SIGN_POSITIVE)),
    ( 393, 17, 'accrued_vat_base_modification', Numeric(sign=SIGN_N)),
    ( 410, 17, 'accrued_vat_tax_modification', Numeric(sign=SIGN_N)),
    ( 427, 17, 'accrued_re_base_4', Numeric(sign=SIGN_POSITIVE)),
    ( 444,  5, 'accrued_re_percent_4', Numeric(sign=SIGN_POSITIVE)),
    ( 449, 17, 'accrued_re_tax_4', Numeric(sign=SIGN_POSITIVE)),
    ( 466, 17, 'accrued_re_base_1', Numeric(sign=SIGN_POSITIVE)),
    ( 483,  5, 'accrued_re_percent_1', Numeric(sign=SIGN_POSITIVE)),
    ( 488, 17, 'accrued_re_tax_1', Numeric(sign=SIGN_POSITIVE)),
    ( 505, 17, 'accrued_re_base_2', Numeric(sign=SIGN_POSITIVE)),
    ( 522,  5, 'accrued_re_percent_2', Numeric(sign=SIGN_POSITIVE)),
    ( 527, 17, 'accrued_re_tax_2', Numeric(sign=SIGN_POSITIVE)),
    ( 544, 17, 'accrued_re_base_3', Numeric(sign=SIGN_POSITIVE)),
    ( 561,  5, 'accrued_re_percent_3', Numeric(sign=SIGN_POSITIVE)),
    ( 566, 17, 'accrued_re_tax_3', Numeric(sign=SIGN_POSITIVE)),
    ( 583, 17, 'accrued_re_base_modification', Numeric(sign=SIGN_N)),
    ( 600, 17, 'accrued_re_tax_modification', Numeric(sign=SIGN_N)),
    ( 617, 17, 'accrued_total_tax', Numeric(sign=SIGN_N)),
    ( 634, 17, 'deductible_current_domestic_operations_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 651, 17, 'deductible_current_domestic_operations_tax',
        Numeric(sign=SIGN_POSITIVE)),
    ( 668, 17, 'deductible_investment_domestic_operations_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 685, 17, 'deductible_investment_domestic_operations_tax',
        Numeric(sign=SIGN_POSITIVE)),
    ( 702, 17, 'deductible_current_import_operations_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 719, 17, 'deductible_current_import_operations_tax',
        Numeric(sign=SIGN_POSITIVE)),
    ( 736, 17, 'deductible_investment_import_operations_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 753, 17, 'deductible_investment_import_operations_tax',
        Numeric(sign=SIGN_POSITIVE)),
    ( 770, 17, 'deductible_current_intracommunity_operations_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 787, 17, 'deductible_current_intracommunity_operations_tax',
        Numeric(sign=SIGN_POSITIVE)),
    ( 804, 17, 'deductible_investment_intracommunity_operations_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 821, 17, 'deductible_investment_intracommunity_operations_tax',
        Numeric(sign=SIGN_POSITIVE)),
    ( 838, 17, 'deductible_regularization_base', Numeric(sign=SIGN_N)),
    ( 855, 17, 'deductible_regularization_tax', Numeric(sign=SIGN_N)),
    ( 872, 17, 'deductible_compensations', Numeric(sign=SIGN_N)),
    ( 889, 17, 'deductible_investment_regularization', Numeric(sign=SIGN_N)),
    ( 906, 17, 'deductible_pro_rata_regularization', Numeric(sign=SIGN_N)),
    ( 923, 17, 'deductible_total', Numeric(sign=SIGN_N)),
    ( 940, 17, 'general_regime_result', Numeric(sign=SIGN_N)),
    ( 957,600, 'reserved_aeat', Char),
    (1557, 13, 'reserved_aeat_electronic_stamp', Char),
    (1570, 12, 'record_end_id', Const('</T30301000>')),
)

# DP30302 This is used for the 'Módulos' and it's not supported.
SIMPLIFIED_RECORD = ()

# DP30303
GENERAL_RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  5, 'page', Const('03000')),
    (  11,  1, 'model_end', Const('>')),
    (  12, 17, 'intracommunity_deliveries', Numeric(sign=SIGN_N)),
    (  29, 17, 'exports', Numeric(sign=SIGN_N)),
    (  46, 17, 'not_subject_localitzation_rules', Numeric(sign=SIGN_N)),
    (  63, 17, 'subject_operations_w_reverse_charge', Numeric(sign=SIGN_N)),
    (  80, 17, 'oss_not_subject_operations', Numeric(sign=SIGN_N)),
    (  97, 17, 'oss_subject_operations', Numeric(sign=SIGN_N)),
    # Additional information for Criterio de Caja
    ( 114, 17, 'recc_deliveries_base', Numeric(sign=SIGN_N)),
    ( 131, 17, 'recc_deliveries_tax', Numeric(sign=SIGN_N)),
    ( 148, 17, 'recc_adquisitions_base', Numeric(sign=SIGN_N)),
    ( 165, 17, 'recc_adquisitions_tax', Numeric(sign=SIGN_N)),
    ( 182, 17, 'result_tax_regularitzation', Numeric(sign=SIGN_N)),
    ( 199, 17, 'sum_results', Numeric(sign=SIGN_N)),
    ( 216,  5, 'state_administration_percent', Numeric(decimals=2)),
    ( 221, 17, 'state_administration_amount', Numeric(sign=SIGN_N)),
    ( 238, 17, 'aduana_tax_pending', Numeric(sign=SIGN_POSITIVE)),
    ( 255, 17, 'previous_period_pending_amount_to_compensate',
        Numeric(sign=SIGN_POSITIVE)),
    ( 272, 17, 'previous_period_amount_to_compensate', Numeric(
            sign=SIGN_POSITIVE)),
    ( 289, 17, 'result_previous_period_amount_to_compensate',
        Numeric(sign=SIGN_POSITIVE)),
    ( 306, 17, 'joint_taxation_state_provincial_councils',
        Numeric(sign=SIGN_N)),
    ( 323, 17, 'result', Numeric(sign=SIGN_N)),
    ( 340, 17, 'before_result', Numeric(sign=SIGN_POSITIVE)),
    ( 357, 17, 'to_deduce', Numeric(sign=SIGN_POSITIVE)),
    ( 374, 17, 'liquidation_result', Numeric(sign=SIGN_N)),
    ( 391,  1, 'without_activity', Boolean(BOOLEAN_X)),
    ( 392,  1, 'complementary_declaration', Boolean(BOOLEAN_X)),
    ( 393, 13, 'previous_declaration_receipt', Char),
    ( 406, 35, 'reserved_aeat', Char),
    ( 441, 52, 'reserved_aeat1', Char),
    ( 493,513, 'reserved_aeat2', Char),
    (1006, 12, 'record_end_id', Const('</T30303000>')),
    )

# DP30304
# Exclusively to be completed in the las period by those taxpayers who are
# exempted from the annual vat summery (Model 390). E.g., whose make SII
ANNUAL_RESUME_RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  5, 'page', Const('04000')),
    (  11,  1, 'model_end', Const('>')),
    (  12,  1, 'additional_page_indicator', Char),
    (  13,  3, 'special_info_key_main', Char),
    (  16,  4, 'special_info_section_iae_main', Char),
    (  20,  3, 'special_info_key_others_1', Char),
    (  23,  4, 'special_info_section_iae_others_1', Char),
    (  27,  3, 'special_info_key_others_2', Char),
    (  30,  4, 'special_info_section_iae_others_2', Char),
    (  34,  3, 'special_info_key_others_3', Char),
    (  37,  4, 'special_info_section_iae_others_3', Char),
    (  41,  3, 'special_info_key_others_4', Char),
    (  44,  4, 'special_info_section_iae_others_4', Char),
    (  48,  1, 'special_info_key_others_5', Char),
    (  51,  4, 'special_info_section_iae_others_5', Char),
    (  55,  1, 'special_info_required_declare_third_party_operation',
        Boolean(BOOLEAN_X)),
    (  56,  5, 'info_territory_alava', Numeric(decimals=2)),
    (  61,  5, 'info_territory_guipuzcoa', Numeric(decimals=2)),
    (  66,  5, 'info_territory_vizcaya', Numeric(decimals=2)),
    (  71,  5, 'info_territory_navarra', Numeric(decimals=2)),
    (  76,  5, 'information_taxation_reason_territory', Numeric(decimals=2)),
    (  81, 17, 'special_info_rg_operations', Numeric(sign=SIGN_N)),
    (  98, 17, 'special_info_recc', Numeric(sign=SIGN_N)),
    ( 115, 17, 'special_info_intracommunity_deliveries_2bdeduced',
        Numeric(sign=SIGN_N)),
    ( 132, 17, 'special_info_exempt_op_2bdeduced', Numeric(sign=SIGN_N)),
    ( 149, 17, 'special_info_exempt_op_wo_permission_2bdeduced',
        Numeric(sign=SIGN_N)),
    ( 166, 17, 'special_info_w_passive_subject', Numeric(sign=SIGN_N)),
    ( 183, 17, 'annual_subject_operations_w_reverse_charge',
        Numeric(sign=SIGN_N)),
    ( 200, 17, 'annual_oss_not_subject_operations', Numeric(sign=SIGN_N)),
    ( 217, 17, 'annual_oss_subject_operations', Numeric(sign=SIGN_N)),
    ( 234, 17, 'annual_intragroup_transaction', Numeric(sign=SIGN_N)),
    ( 251, 17, 'special_info_operations_rs', Numeric(sign=SIGN_N)),
    ( 268, 17, 'special_info_farming_cattleraising_fishing',
        Numeric(sign=SIGN_N)),
    ( 285, 17, 'special_info_passive_subject_re', Numeric(sign=SIGN_N)),
    ( 302, 17, 'special_info_art_antiques_collectibles', Numeric(sign=SIGN_N)),
    ( 319, 17, 'special_info_travel_agency', Numeric(sign=SIGN_N)),
    ( 336, 17, 'special_info_financial_op_not_usual', Numeric(sign=SIGN_N)),
    ( 353, 17, 'special_info_delivery_investment_domestic_operations',
        Numeric(sign=SIGN_N)),
    ( 370, 17, 'special_info_total', Numeric(sign=SIGN_N)),
    ( 387,600, 'reserved_aeat', Char),
    ( 987, 12, 'record_end_id', Const('</T30304000>')),
    )

# DP30305
# Apportionment (Prorrata)
# Exclusively to be completed in the las period by those taxpayers who are
# exempted to present the model 390 and apply the apportionment rules.
ANNUAL_RESUME_ADDITIONAL_RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  5, 'page', Const('05000')),
    (  11,  1, 'model_end', Const('>')),
    (  12,  1, 'additional_page_indicator', Char),
    (  13,  3, 'cnae1', Char),
    (  16, 17, 'operations_amount1', Numeric(sign=SIGN_N)),
    (  33, 17, 'operations_amount_w_deduction1', Numeric(sign=SIGN_N)),
    (  50,  1, 'prorrata_type1', Char),
    (  51,  5, 'prorrata_percent1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    (  56,  3, 'cnae2', Char),
    (  59, 17, 'operations_amount2', Numeric(sign=SIGN_N)),
    (  76, 17, 'operations_amount_w_deduction2', Numeric(sign=SIGN_N)),
    (  93,  1, 'prorrata_type2', Char),
    (  94,  5, 'prorrata_percent2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    (  99,  3, 'cnae3', Char),
    ( 102, 17, 'operations_amount3', Numeric(sign=SIGN_N)),
    ( 119, 17, 'operations_amount_w_deduction3', Numeric(sign=SIGN_N)),
    ( 136,  1, 'prorrata_type3', Char),
    ( 137,  5, 'prorrata_percent3', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 142,  3, 'cnae4', Char),
    ( 145, 17, 'operations_amount4', Numeric(sign=SIGN_N)),
    ( 162, 17, 'operations_amount_w_deduction4', Numeric(sign=SIGN_N)),
    ( 179,  1, 'prorrata_type4', Char),
    ( 180,  5, 'prorrata_percent4', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 185,  3, 'cnae5', Char),
    ( 188, 17, 'operations_amount5', Numeric(sign=SIGN_N)),
    ( 205, 17, 'operations_amount_w_deduction5', Numeric(sign=SIGN_N)),
    ( 222,  1, 'prorrata_type5', Char),
    ( 223,  5, 'prorrata_percent5', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 228, 17, 'deductible_current_domestic_operations_base1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 245, 17, 'deductible_current_domestic_operations_tax1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 262, 17, 'deductible_investment_domestic_operations_base1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 279, 17, 'deductible_investment_domestic_operations_tax1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 296, 17, 'deductible_current_import_operations_base1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 313, 17, 'deductible_current_import_operations_tax1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 330, 17, 'deductible_investment_import_operations_base1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 347, 17, 'deductible_investment_import_operations_tax1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 364, 17, 'deductible_current_intracommunity_operations_base1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 381, 17, 'deductible_current_intracommunity_operations_tax1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 398, 17, 'deductible_investment_intracommunity_operations_base1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 415, 17, 'deductible_investment_intracommunity_operations_tax1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 432, 17, 'deductible_compensations_base1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 449, 17, 'deductible_compensations_tax1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 466, 17, 'deductible_regularization_base1', Numeric(sign=SIGN_N)),
    ( 483, 17, 'deductible_regularization_tax1', Numeric(sign=SIGN_N)),
    ( 500, 17, 'deductible_investment_regularization1', Numeric(sign=SIGN_N)),
    ( 517, 17, 'deductible_total1', Numeric(sign=SIGN_N)),
    ( 534, 17, 'deductible_current_domestic_operations_base2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 551, 17, 'deductible_current_domestic_operations_tax2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 568, 17, 'deductible_investment_domestic_operations_base2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 585, 17, 'deductible_investment_domestic_operations_tax2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 602, 17, 'deductible_current_import_operations_base2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 619, 17, 'deductible_current_import_operations_tax2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 636, 17, 'deductible_investment_import_operations_base2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 653, 17, 'deductible_investment_import_operations_tax2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 670, 17, 'deductible_current_intracommunity_operations_base2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 687, 17, 'deductible_current_intracommunity_operations_tax2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 704, 17, 'deductible_investment_intracommunity_operations_base2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 721, 17, 'deductible_investment_intracommunity_operations_tax2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 738, 17, 'deductible_compensations_base2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 755, 17, 'deductible_compensations_tax2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 772, 17, 'deductible_regularization_base2', Numeric(sign=SIGN_N)),
    ( 789, 17, 'deductible_regularization_tax2', Numeric(sign=SIGN_N)),
    ( 806, 17, 'deductible_investment_regularization2', Numeric(sign=SIGN_N)),
    ( 823, 17, 'deductible_total2', Numeric(sign=SIGN_N)),
    ( 840,672, 'reserved_aeat', Char),
    (1512, 12, 'record_end_id', Const('</T30305000>')),
    )

# DP303DID
# For the return bank information
BANK_DATA_RECORD = (
    (   1,  2, 'model_close_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  5, 'first_constant', Const('DID00')),
    (  11,  1, 'model_close_end', Const('>')),
    (  12, 11, 'swift_bank', Char),
    (  23, 34, 'bank_account', Char),
    (  57, 70, 'return_bank_name', Char),
    ( 127, 35, 'return_bank_address', Char),
    ( 162, 30, 'return_bank_city', Char),
    ( 192,  2, 'return_bank_country_code', Char),
    ( 194,  1, 'return_sepa_check', Number),
    ( 195,617, 'reserved_aeat', Char),
    ( 812, 12, 'record_end_id', Const('</T303DID00>')),
    )

FOOTER_RECORD = (
    (   1,  3, 'model_close_start', Const('</T')),
    (   4,  3, 'model', Const('303')),
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

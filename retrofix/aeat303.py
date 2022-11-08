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
    (  93,  4, 'program_version', Const('0247')),
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
    ( 118,  8, 'auto_bankruptcy_date', Date('%Y%m%d')),
    ( 126,  1, 'auto_bankruptcy_declaration', Char),
    ( 127,  1, 'passive_subject_voluntarily_sii', Number),
    ( 128,  1, 'exonerated_mod390', Number),
    ( 129,  1, 'annual_operation_volume', Number),
    ( 130, 17, 'accrued_vat_base_1', Numeric(sign=SIGN_POSITIVE)),
    ( 147,  5, 'accrued_vat_percent_1', Numeric(sign=SIGN_POSITIVE)),
    ( 152, 17, 'accrued_vat_tax_1', Numeric(sign=SIGN_POSITIVE)),
    ( 169, 17, 'accrued_vat_base_2', Numeric(sign=SIGN_POSITIVE)),
    ( 186,  5, 'accrued_vat_percent_2', Numeric(sign=SIGN_POSITIVE)),
    ( 191, 17, 'accrued_vat_tax_2', Numeric(sign=SIGN_POSITIVE)),
    ( 208, 17, 'accrued_vat_base_3', Numeric(sign=SIGN_POSITIVE)),
    ( 225,  5, 'accrued_vat_percent_3', Numeric(sign=SIGN_POSITIVE)),
    ( 230, 17, 'accrued_vat_tax_3', Numeric(sign=SIGN_POSITIVE)),
    ( 247, 17, 'intracommunity_adquisitions_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 264, 17, 'intracommunity_adquisitions_tax', Numeric(sign=SIGN_POSITIVE)),
    ( 281, 17, 'other_passive_subject_base', Numeric(sign=SIGN_POSITIVE)),
    ( 298, 17, 'other_passive_subject_tax', Numeric(sign=SIGN_POSITIVE)),
    ( 315, 17, 'accrued_vat_base_modification', Numeric(sign=SIGN_N)),
    ( 332, 17, 'accrued_vat_tax_modification', Numeric(sign=SIGN_N)),
    ( 349, 17, 'accrued_re_base_1', Numeric(sign=SIGN_POSITIVE)),
    ( 366,  5, 'accrued_re_percent_1', Numeric(sign=SIGN_POSITIVE)),
    ( 371, 17, 'accrued_re_tax_1', Numeric(sign=SIGN_POSITIVE)),
    ( 388, 17, 'accrued_re_base_2', Numeric(sign=SIGN_POSITIVE)),
    ( 405,  5, 'accrued_re_percent_2', Numeric(sign=SIGN_POSITIVE)),
    ( 410, 17, 'accrued_re_tax_2', Numeric(sign=SIGN_POSITIVE)),
    ( 427, 17, 'accrued_re_base_3', Numeric(sign=SIGN_POSITIVE)),
    ( 444,  5, 'accrued_re_percent_3', Numeric(sign=SIGN_POSITIVE)),
    ( 449, 17, 'accrued_re_tax_3', Numeric(sign=SIGN_POSITIVE)),
    ( 466, 17, 'accrued_re_base_modification', Numeric(sign=SIGN_N)),
    ( 483, 17, 'accrued_re_tax_modification', Numeric(sign=SIGN_N)),
    ( 500, 17, 'accrued_total_tax', Numeric(sign=SIGN_N)),
    ( 517, 17, 'deductible_current_domestic_operations_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 534, 17, 'deductible_current_domestic_operations_tax',
        Numeric(sign=SIGN_POSITIVE)),
    ( 551, 17, 'deductible_investment_domestic_operations_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 568, 17, 'deductible_investment_domestic_operations_tax',
        Numeric(sign=SIGN_POSITIVE)),
    ( 585, 17, 'deductible_current_import_operations_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 602, 17, 'deductible_current_import_operations_tax',
        Numeric(sign=SIGN_POSITIVE)),
    ( 619, 17, 'deductible_investment_import_operations_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 636, 17, 'deductible_investment_import_operations_tax',
        Numeric(sign=SIGN_POSITIVE)),
    ( 653, 17, 'deductible_current_intracommunity_operations_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 670, 17, 'deductible_current_intracommunity_operations_tax',
        Numeric(sign=SIGN_POSITIVE)),
    ( 687, 17, 'deductible_investment_intracommunity_operations_base',
        Numeric(sign=SIGN_POSITIVE)),
    ( 704, 17, 'deductible_investment_intracommunity_operations_tax',
        Numeric(sign=SIGN_POSITIVE)),
    ( 721, 17, 'deductible_regularization_base', Numeric(sign=SIGN_N)),
    ( 738, 17, 'deductible_regularization_tax', Numeric(sign=SIGN_N)),
    ( 755, 17, 'deductible_compensations', Numeric(sign=SIGN_N)),
    ( 772, 17, 'deductible_investment_regularization', Numeric(sign=SIGN_N)),
    ( 789, 17, 'deductible_pro_rata_regularization', Numeric(sign=SIGN_N)),
    ( 806, 17, 'deductible_total', Numeric(sign=SIGN_N)),
    ( 823, 17, 'general_regime_result', Numeric(sign=SIGN_N)),
    ( 840,600, 'reserved_aeat', Char),
    (1440, 13, 'reserved_aeat_electronic_stamp', Char),
    (1453, 12, 'record_end_id', Const('</T30301000>')),
)

# DP30302 This is used for the 'Módulos'.
SIMPLIFIED_RECORD = ()

# DP30303
GENERAL_RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  5, 'page', Const('03000')),
    (  11,  1, 'model_end', Const('>')),
    (  12, 17, 'intracommunity_deliveries', Numeric(sign=SIGN_N)),
    (  29, 17, 'exports', Numeric(sign=SIGN_N)),
    (  46, 17, 'not_subject_localization_rules', Numeric(sign=SIGN_N)),
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
        Numeric(sign=SIGN_POSITIVE)),
    ( 323, 17, 'result', Numeric(sign=SIGN_N)),
    ( 340, 17, 'to_deduce', Numeric(sign=SIGN_N)),
    ( 357, 17, 'liquidation_result', Numeric(sign=SIGN_N)),
    ( 374,  1, 'complementary_declaration', Boolean(BOOLEAN_X)),
    ( 375, 13, 'previous_declaration_receipt', Char),
    ( 388,  1, 'without_activity', Boolean(BOOLEAN_X)),
    ( 389, 11, 'swift_bank', Char),
    ( 400, 34, 'bank_account', Char),
    ( 434, 17, 'reserved_aeat2', Char),
    ( 451, 70, 'return_bank_name', Char),
    ( 521, 35, 'return_bank_address', Char),
    ( 556, 30, 'return_bank_city', Char),
    ( 586,  2, 'return_bank_country_code', Char),
    ( 588,  1, 'return_sepa_check', Number),
    ( 589,600, 'reserved_aeat3', Char),
    (1189, 12, 'record_end_id', Const('</T30303000>')),
    )

# DP30304
ADDITIONAL_RECORD = (
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
    (  76,  5, 'information_taxation_reason_territory', Numeric(sign=SIGN_N)),
    (  81, 17, 'special_info_rg_operations', Numeric(sign=SIGN_N)),
    (  98, 17, 'special_info_recc', Numeric(sign=SIGN_N)),
    ( 115, 17, 'special_info_export_intracomunitari_out_2bdeduced',
        Numeric(sign=SIGN_N)),
    ( 132, 17, 'special_info_exempt_op_2bdeduced', Numeric(sign=SIGN_N)),
    ( 149, 17, 'special_info_exempt_op_wo_permission_2bdeduced',
        Numeric(sign=SIGN_N)),
    ( 166, 17, 'special_info_w_passive_subject', Numeric(sign=SIGN_N)),
    ( 183, 17, 'annual_subject_operations_w_reverse_charge',
        Numeric(sign=SIGN_N)),
    ( 200, 17, 'annual_oss_not_subject_operations', Numeric(sign=SIGN_N)),
    ( 217, 17, 'annual_oss_subject_operations', Numeric(sign=SIGN_N)),
    ( 234, 17, 'annual_intragrup_transaction', Numeric(sign=SIGN_N)),
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
    ( 387,600, 'reserved_aeat4', Char),
    ( 987, 12, 'record_end_id', Const('</T30304000>')),
    )

# DP30305 This is used on the last period for the companies that make SII.
ANNUAL_RESUME_RECORD = (
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

    ( 228, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 245, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 262, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 279, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 296, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 313, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 330, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 347, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 364, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 381, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 398, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 415, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 432, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 449, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 466, 17, '', Numeric(sign=SIGN_N)),
    ( 483, 17, '', Numeric(sign=SIGN_N)),
    ( 500, 17, '', Numeric(sign=SIGN_N)),
    ( 517, 17, '', Numeric(sign=SIGN_N)),

    ( 534, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 551, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 568, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 585, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 602, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 619, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 636, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 653, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 670, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 687, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 704, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 721, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 738, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 755, 17, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 772, 17, '', Numeric(sign=SIGN_N)),
    ( 789, 17, '', Numeric(sign=SIGN_N)),
    ( 806, 17, '', Numeric(sign=SIGN_N)),
    ( 823, 17, '', Numeric(sign=SIGN_N)),

    ( 840,672, 'reserved_aeat', Char),
    (1512, 12, 'record_end_id', Const('</T30305000>')),
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

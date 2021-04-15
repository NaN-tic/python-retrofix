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
    ( 103,  4, 'fiscalyear', Number),
    ( 107,  2, 'period', Char),
    ( 109,  1, 'passive_subject_foral_administration', Boolean(BOOLEAN_12)),
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
    ( 127,  1, 'taken_vat_book_to_aeat', Number),
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
    ( 247, 17, 'intracommunity_adquisitions_base', Numeric(sign=SIGN_POSITIVE)),
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

# DP30302 This is used for the 'modulos'.
SIMPLIFIED_RECORD = ()

# DP30303
GENERAL_RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  5, 'page', Const('03000')),
    (  11,  1, 'model_end', Const('>')),
    (  12, 17, 'intracommunity_deliveries', Numeric(sign=SIGN_N)),
    (  29, 17, 'exports', Numeric(sign=SIGN_N)),
    (  46, 17, 'not_subject_or_reverse_charge', Numeric(sign=SIGN_N)),
    (  63,  17, 'reserved_aeat1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    (  80,  17, 'reserved_aeat2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    (  97,  17, 'reserved_aeat3', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 114,  17, 'reserved_aeat4', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 131,  17, 'reserved_aeat5', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 148, 17, 'recc_deliveries_base', Numeric(sign=SIGN_N)),
    ( 165, 17, 'recc_deliveries_tax', Numeric(sign=SIGN_N)),
    ( 182, 17, 'recc_adquisitions_base', Numeric(sign=SIGN_N)),
    ( 199, 17, 'recc_adquisitions_tax', Numeric(sign=SIGN_N)),
    ( 216, 17, 'result_tax_regularitzation', Numeric(sign=SIGN_N)),
    ( 233, 17, 'sum_results', Numeric(sign=SIGN_N)),
    ( 250,  5, 'state_administration_percent', Numeric(decimals=2)),
    ( 255, 17, 'state_administration_amount', Numeric(sign=SIGN_N)),
    ( 272, 17, 'aduana_tax_pending', Numeric(sign=SIGN_N)),
    ( 289, 17, 'previous_period_pending_amount_to_compensate', Numeric(sign=SIGN_N)),
    ( 306, 17, 'previous_period_amount_to_compensate', Numeric(sign=SIGN_N)),
    ( 323, 17, 'result_previous_period_amount_to_compensate', Numeric(sign=SIGN_N)),
    ( 340, 17, 'joint_taxation_state_provincial_councils',
         Numeric(sign=SIGN_N)),
    ( 357, 17, 'result', Numeric(sign=SIGN_N)),
    ( 374, 17, 'to_deduce', Numeric(sign=SIGN_N)),
    ( 391, 17, 'liquidation_result', Numeric(sign=SIGN_N)),
    ( 408,  1, 'complementary_declaration', Boolean(BOOLEAN_X)),
    ( 409, 13, 'previous_declaration_receipt', Char),
    ( 422,  1, 'without_activity', Boolean(BOOLEAN_X)),
    ( 423, 11, 'swift_bank', Char),
    ( 434, 34, 'bank_account', Char),
    ( 468, 17, 'reserved_aeat6', Char),
    ( 485,583, 'reserved_aeat7', Char),
    (1068, 12, 'record_end_id', Const('</T30303000>')),
    )

# DP30304
ADDITIONAL_RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  5, 'page', Const('04000')),
    (  11,  1, 'model_end', Const('>')),
    (  12,  1, 'additional_page_indicator', Char),
    (  13,  1, 'special_info_key_main', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    (  14,  4, 'special_info_section_iae_main', Char),
    (  18,  1, 'special_info_key_others_1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    (  19,  4, 'special_info_section_iae_others_1', Char),
    (  23,  1, 'special_info_key_others_2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    (  24,  4, 'special_info_section_iae_others_2', Char),
    (  28,  1, 'special_info_key_others_3', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    (  29,  4, 'special_info_section_iae_others_3', Char),
    (  33,  1, 'special_info_key_others_4', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    (  34,  4, 'special_info_section_iae_others_4', Char),
    (  38,  1, 'special_info_key_others_5', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    (  39,  4, 'special_info_section_iae_others_5', Char),
    (  43,  1, 'special_info_required_declare_third_party_operation', Boolean(BOOLEAN_X)),
    (  44,  5, 'info_territory_alava', Numeric(decimals=2)),
    (  49,  5, 'info_territory_guipuzcoa', Numeric(decimals=2)),
    (  54,  5, 'info_territory_vizcaya', Numeric(decimals=2)),
    (  59,  5, 'info_territory_navarra', Numeric(decimals=2)),
    (  64,  5, 'information_taxation_reason_territory', Numeric(sign=SIGN_N)),
    (  69, 17, 'special_info_rg_operations', Numeric(sign=SIGN_N)),
    (  86, 17, 'special_info_recc', Numeric(sign=SIGN_N)),
    ( 103, 17, 'special_info_export_intracomunitari_out_2bdeduced', Numeric(sign=SIGN_N)),
    ( 120, 17, 'special_info_exempt_op_2bdeduced', Numeric(sign=SIGN_N)),
    ( 137, 17, 'special_info_exempt_op_wo_permission 2bdeduced', Numeric(sign=SIGN_N)),
    ( 154, 17, 'special_info_w_passive_subject', Numeric(sign=SIGN_N)),
    ( 171, 17, 'special_info_delivery_need_install_object_in_other_eu_country', Numeric(sign=SIGN_N)),
    ( 188, 17, 'reserved_aeat1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 205, 17, 'reserved_aeat2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 222, 17, 'reserved_aeat3', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 239, 17, 'special_info_operations_rs', Numeric(sign=SIGN_N)),
    ( 256, 17, 'special_info_farming_cattleraising_fishing', Numeric(sign=SIGN_N)),
    ( 273, 17, 'special_info_passive_subject_re', Numeric(sign=SIGN_N)),
    ( 290, 17, 'special_info_art_antiques_collectibles', Numeric(sign=SIGN_N)),
    ( 307, 17, 'special_info_travel_agency', Numeric(sign=SIGN_N)),
    ( 324, 17, 'special_info_financial_op_not_usual', Numeric(sign=SIGN_N)),
    ( 341, 17, 'special_info_delivery_investment_domestic_operations', Numeric(sign=SIGN_N)),
    ( 358, 17, 'special_info_total', Numeric(sign=SIGN_N)),
    ( 375,600, 'reserved_aeat4', Char),
    ( 975, 12, 'record_end_id', Const('</T30304000>')),
    )

# DP30305 This is used on the last period for the companies that make SII.
ANUAL_RESUM_RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  5, 'page', Const('05000')),
    (  11,  1, 'model_end', Const('>')),
    (  12,  1, 'additional_page_indicator', Char),

    (  13,  3, '', Char),
    (  16, 17, '', Numeric(sign=SIGN_N)),
    (  33, 17, '', Numeric(sign=SIGN_N)),
    (  50,  1, '', Char),
    (  51,  5, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),

    (  56,  3, '', Char),
    (  59, 17, '', Numeric(sign=SIGN_N)),
    (  76, 17, '', Numeric(sign=SIGN_N)),
    (  93,  1, '', Char),
    (  94,  5, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),

    (  99,  3, '', Char),
    ( 102, 17, '', Numeric(sign=SIGN_N)),
    ( 119, 17, '', Numeric(sign=SIGN_N)),
    ( 136,  1, '', Char),
    ( 137,  5, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),

    ( 142,  3, '', Char),
    ( 145, 17, '', Numeric(sign=SIGN_N)),
    ( 162, 17, '', Numeric(sign=SIGN_N)),
    ( 179,  1, '', Char),
    ( 180,  5, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),

    ( 185,  3, '', Char),
    ( 188, 17, '', Numeric(sign=SIGN_N)),
    ( 205, 17, '', Numeric(sign=SIGN_N)),
    ( 222,  1, '', Char),
    ( 223,  5, '', Numeric(decimals=0, sign=SIGN_POSITIVE)),

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
    (   8,  4, 'fiscalyear', Number),
    (  12,  2, 'period', Char),
    (  14,  5, 'model_close_end', Const('0000>')),
    )

def read(data):
    lines = data.splitlines()
    records = []
    current_line = lines.pop(0)
    records.append(Record.extract(current_line, RECORD))
    return records

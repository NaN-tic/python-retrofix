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

RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  2, 'page', Const('01')),
    (   8,  1, 'model_end', Const('>')),
    (   9,  1, 'type', Char),
    (  10,  9, 'company_vat', Char),
    (  19, 30, 'company_name', Char),
    (  49, 15, 'first_name', Char),
    (  64,  1, 'monthly_return_subscription', Boolean(BOOLEAN_12)),
    (  65,  1, 'regime_type', Number),
    (  66,  1, 'joint_liquidation', Boolean(BOOLEAN_12)),
    (  67,  1, 'bankruptcy', Boolean(BOOLEAN_12)),
    (  68,  8, 'auto_bankruptcy_date', Date('%Y%m%d')),
    (  76,  1, 'auto_bankruptcy_declaration', Char),
    (  77,  1, 'recc', Boolean(BOOLEAN_12)),
    (  78,  1, 'recc_receiver', Boolean(BOOLEAN_12)),
    (  79,  1, 'special_prorate', Boolean(BOOLEAN_12)),
    (  80,  1, 'special_prorate_revocation', Boolean(BOOLEAN_12)),
    (  81,  4, 'fiscalyear', Number),
    (  85,  2, 'period', Char),
    (  87, 17, 'accrued_vat_base_1', Numeric(sign=SIGN_POSITIVE)),
    ( 104,  5, 'accrued_vat_percent_1', Numeric(sign=SIGN_POSITIVE)),
    ( 109, 17, 'accrued_vat_tax_1', Numeric(sign=SIGN_POSITIVE)),
    ( 126, 17, 'accrued_vat_base_2', Numeric(sign=SIGN_POSITIVE)),
    ( 143,  5, 'accrued_vat_percent_2', Numeric(sign=SIGN_POSITIVE)),
    ( 148, 17, 'accrued_vat_tax_2', Numeric(sign=SIGN_POSITIVE)),
    ( 165, 17, 'accrued_vat_base_3', Numeric(sign=SIGN_POSITIVE)),
    ( 182,  5, 'accrued_vat_percent_3', Numeric(sign=SIGN_POSITIVE)),
    ( 187, 17, 'accrued_vat_tax_3', Numeric(sign=SIGN_POSITIVE)),
    ( 204, 17, 'intracommunity_adquisitions_base', Numeric(sign=SIGN_POSITIVE)),
    ( 221, 17, 'intracommunity_adquisitions_tax', Numeric(sign=SIGN_POSITIVE)),
    ( 238, 17, 'other_passive_subject_base', Numeric(sign=SIGN_POSITIVE)),
    ( 255, 17, 'other_passive_subject_tax', Numeric(sign=SIGN_POSITIVE)),
    ( 272, 17, 'accrued_vat_base_modification', Numeric(sign=SIGN_N)),
    ( 289, 17, 'accrued_vat_tax_modification', Numeric(sign=SIGN_N)),
    ( 306, 17, 'accrued_re_base_1', Numeric(sign=SIGN_POSITIVE)),
    ( 323,  5, 'accrued_re_percent_1', Numeric(sign=SIGN_POSITIVE)),
    ( 328, 17, 'accrued_re_tax_1', Numeric(sign=SIGN_POSITIVE)),
    ( 345, 17, 'accrued_re_base_2', Numeric(sign=SIGN_POSITIVE)),
    ( 362,  5, 'accrued_re_percent_2', Numeric(sign=SIGN_POSITIVE)),
    ( 367, 17, 'accrued_re_tax_2', Numeric(sign=SIGN_POSITIVE)),
    ( 384, 17, 'accrued_re_base_3', Numeric(sign=SIGN_POSITIVE)),
    ( 401,  5, 'accrued_re_percent_3', Numeric(sign=SIGN_POSITIVE)),
    ( 406, 17, 'accrued_re_tax_3', Numeric(sign=SIGN_POSITIVE)),
    ( 423, 17, 'accrued_re_base_modification', Numeric(sign=SIGN_N)),
    ( 440, 17, 'accrued_re_tax_modification', Numeric(sign=SIGN_N)),
    ( 457, 17, 'accrued_total_tax', Numeric(sign=SIGN_N)),
    ( 474, 17, 'deductible_current_domestic_operations_base',
         Numeric(sign=SIGN_POSITIVE)),
    ( 491, 17, 'deductible_current_domestic_operations_tax',
         Numeric(sign=SIGN_POSITIVE)),
    ( 508, 17, 'deductible_investment_domestic_operations_base',
         Numeric(sign=SIGN_POSITIVE)),
    ( 525, 17, 'deductible_investment_domestic_operations_tax',
         Numeric(sign=SIGN_POSITIVE)),
    ( 542, 17, 'deductible_current_import_operations_base',
         Numeric(sign=SIGN_POSITIVE)),
    ( 559, 17, 'deductible_current_import_operations_tax',
         Numeric(sign=SIGN_POSITIVE)),
    ( 576, 17, 'deductible_investment_import_operations_base',
         Numeric(sign=SIGN_POSITIVE)),
    ( 593, 17, 'deductible_investment_import_operations_tax',
         Numeric(sign=SIGN_POSITIVE)),
    ( 610, 17, 'deductible_current_intracommunity_operations_base',
         Numeric(sign=SIGN_POSITIVE)),
    ( 627, 17, 'deductible_current_intracommunity_operations_tax',
         Numeric(sign=SIGN_POSITIVE)),
    ( 644, 17, 'deductible_investment_intracommunity_operations_base',
         Numeric(sign=SIGN_POSITIVE)),
    ( 661, 17, 'deductible_investment_intracommunity_operations_tax',
         Numeric(sign=SIGN_POSITIVE)),
    ( 678, 17, 'deductible_regularization_base', Numeric(sign=SIGN_N)),
    ( 695, 17, 'deductible_regularization_tax', Numeric(sign=SIGN_N)),
    ( 712, 17, 'deductible_compensations', Numeric(sign=SIGN_N)),
    ( 729, 17, 'deductible_investment_regularization', Numeric(sign=SIGN_N)),
    ( 746, 17, 'deductible_pro_rata_regularization', Numeric(sign=SIGN_N)),
    ( 763, 17, 'deductible_total', Numeric(sign=SIGN_N)),
    ( 780, 17, 'difference', Numeric(sign=SIGN_N)),
    ( 797,582, 'reserved_aeat', Char),
    (1379, 13, 'reserved_aeat_electronic_stamp', Char),
    (1392,  9, 'record_end_id', Const('</T30301>')),
)

# This is used for the 'modulos'.
SIMPLIFIED_RECORD = ()

ADDITIONAL_RECORD = (
    (   1,  2, 'model_start', Const('<T')),
    (   3,  3, 'model', Const('303')),
    (   6,  2, 'page', Const('03')),
    (   8,  1, 'model_end', Const('>')),
    (   9, 17, 'intracommunity_deliveries', Numeric(sign=SIGN_N)),
    (  26, 17, 'exports', Numeric(sign=SIGN_N)),
    (  43, 17, 'not_subject_or_reverse_charge', Numeric(sign=SIGN_N)),
    #TODO: Modify is simplified records is needed as it must be added to
    # difference
    (  60, 17, 'difference', Numeric(sign=SIGN_N)),
    (  77,  5, 'state_administration_percent', Numeric()),
    (  82, 17, 'state_administration_amount', Numeric(sign=SIGN_N)),
    (  99, 17, 'previous_period_amount_to_compensate', Numeric(sign=SIGN_N)),
    ( 116, 17, 'joint_taxation_state_provincial_councils',
         Numeric(sign=SIGN_N)),
    ( 133, 17, 'result', Numeric(sign=SIGN_N)),
    ( 150, 17, 'to_deduce', Numeric(sign=SIGN_N)),
    ( 167, 17, 'liquidation_result', Numeric(sign=SIGN_N)),
    ( 184, 17, 'recc_deliveries_base', Numeric(sign=SIGN_N)),
    ( 201, 17, 'recc_deliveries_tax', Numeric(sign=SIGN_N)),
    ( 218, 17, 'recc_adquisitions_base', Numeric(sign=SIGN_N)),
    ( 235, 17, 'recc_adquisitions_tax', Numeric(sign=SIGN_N)),
    ( 252,  1, 'complementary_declaration', Boolean(BOOLEAN_X)),
    ( 253, 13, 'previous_declaration_receipt', Number),
    ( 266,  1, 'without_activity', Boolean(BOOLEAN_X)),
    ( 267, 34, 'bank_account', Char),
    ( 301,  1, 'special_info_key_main', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 302,  4, 'special_info_section_iae_main', Char),
    ( 306,  1, 'special_info_key_others_1', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 307,  4, 'special_info_section_iae_others_1', Char),
    ( 311,  1, 'special_info_key_others_2', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 312,  4, 'special_info_section_iae_others_2', Char),
    ( 316,  1, 'special_info_key_others_3', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 317,  4, 'special_info_section_iae_others_3', Char),
    ( 321,  1, 'special_info_key_others_4', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 322,  4, 'special_info_section_iae_others_4', Char),
    ( 326,  1, 'special_info_key_others_5', Numeric(decimals=0, sign=SIGN_POSITIVE)),
    ( 327,  4, 'special_info_section_iae_others_5', Char),
    ( 331,  1, 'special_info_required_declare_third_party_operation', Boolean(BOOLEAN_X)),
    ( 332, 17, 'special_info_rg_operations', Numeric(sign=SIGN_N)),
    ( 349, 17, 'special_info_recc', Numeric(sign=SIGN_N)),
    ( 366, 17, 'special_info_export_intracomunitari_out_2bdeduced', Numeric(sign=SIGN_N)),
    ( 383, 17, 'special_info_exempt_op_wo_permission 2bdeduced', Numeric(sign=SIGN_N)),
    ( 400, 17, 'special_info_w_passive_subject', Numeric(sign=SIGN_N)),
    ( 417, 17, 'special_info_delivery_need_install_object_in_other_eu_country', Numeric(sign=SIGN_N)),
    ( 434, 17, 'special_info_operations_rs', Numeric(sign=SIGN_N)),
    ( 451, 17, 'special_info_financial_op_not_usual', Numeric(sign=SIGN_N)),
    ( 468, 17, 'special_info_total', Numeric(sign=SIGN_N)),
    ( 485, 17, 'reserved_2014_model_result_tax_regulaitzation', Numeric(sign=SIGN_N)),
    ( 502, 17, 'reserved_2014_model_aduana_tax_pending', Numeric(sign=SIGN_N)),
    ( 519,573, 'reserved_aeat', Char),
    (1092,  9, 'record_end_id', Const('</T30303>')),
    )


def read(data):
    lines = data.splitlines()
    records = []
    current_line = lines.pop(0)
    records.append(Record.extract(current_line, RECORD))
    return records

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
PRESENTER_HEADER_RECORD = (
    (  1,  1, 'record_code', 'N', '=1'),
    (  2,  3, 'model', 'N', '=340'),
    (  5,  4, 'fiscalyear', 'N'),
    (  9,  9, 'nif', 'A'),
    ( 18, 40, 'presenter_name', 'A'),
    ( 58,  1, 'support_type', 'A'),
    ( 59,  9, 'contact_phone', 'N'),
    ( 68, 40, 'contact_name', 'A'),
    (108, 13, 'declaration_number', 'N'),
    (121,  1, 'complementary', 'A'),
    (122,  1, 'replacement', 'A'),
    (123, 13, 'previous_declaration_number', 'N'),
    (136,  2, 'period', 'A'),
    (138,  9, 'record_count', 'N'),
    (147,  1, 'total_base_sign', 'A'),
    (148, 17, 'total_base', 'N', '2'),
    (165,  1, 'total_tax_sign', 'A'),
    (166, 17, 'total_tax', 'N', '2'),
    (183,  1, 'total_sign', 'A'),
    (184, 17, 'total', 'N', '2'),
    (391,  9, 'representative_nif', 'A'),
    (400, 16, 'electronic_number', 'A'),
    )

DETAIL_RECORD = (
    (  1,  1, 'recod_code', 'N', '=2'),
    (  2,  3, 'model', 'N', '=340'),
    (  5,  4, 'fiscalyear', 'N'),
    (  9,  9, 'nif', 'A'),
    ( 18,  9, 'party_nif', 'A'),
    ( 27,  9, 'representative_nif', 'A'),
    ( 36, 40, 'party_name', 'A'),
    ( 76,  2, 'party_country', 'A'),
    ( 78,  1, 'party_identifier_type', 'N'),
    ( 79, 20, 'party_identifier', 'A'),
    ( 99,  1, 'book_key', 'A'),
    (100,  1, 'operation_key', 'A'),
    (101,  8, 'issue_date', 'D', '%Y%m%d'),
    (109,  8, 'operation_date', 'D', '%Y%m%d'),
    (117,  5, 'tax_rate', 'N', '2'),
    (122,  1, 'base_sign', 'A'),
    (123, 13, 'base', 'N', '2'),
    (136,  1, 'tax_sign', 'A'),
    (137, 13, 'tax', 'N', '2'),
    (150,  1, 'total_sign', 'A'),
    (151, 13, 'total', 'N', '2'),
    (164,  1, 'cost_sign', 'A'),
    (165, 13, 'cost', 'N', '2'),
    (178, 40, 'invoice_number', 'A'),
    (218, 18, 'record_number', 'A'),
    # Issued Invoices
    (236,  8, 'invoice_count', 'N'),
    (244,  2, 'record_count', 'N'),
    (246, 40, 'first_invoice_number', 'A'),
    (286, 40, 'last_invoice_number', 'A'),
    (326, 40, 'corrective_invoice_number', 'A'),
    (366,  5, 'equivalence_tax_rate', 'N', '2'),
    (371,  1, 'equivalence_tax_sign', 'A'),
    (372, 13, 'equivalence_tax', 'N', '2'),
    (385,  1, 'property_state', 'A'),
    (386, 25, 'cadaster_number', 'A'),
    (411, 15, 'cash_amount_sign', 'A'),
    (411, 15, 'cash_amount', 'N', '2'),
    (426,  4, 'fiscalyear', 'N'),
    (430, 15, 'property_transfer_amount', 'N', '2'),
    # Received Invoices
    (236, 18, 'invoice_count', 'N'),
    (254,  2, 'record_count', 'N'),
    (256, 40, 'first_invoice_number', 'A'),
    (296, 40, 'last_invoice_number', 'A'),
    (336, 14, 'deducible_amount_sign', 'A'),
    (336, 14, 'deducible_amount', 'N', '2'),
    # Investment goods
    (236,  3, 'pro_rata', 'N'),
    (239,  1, 'yearly_regularization_sign', 'A'),
    (240, 13, 'yearly_regularization', 'A'),
    (253, 40, 'submission_number', 'A'),
    (293,  1, 'transmissions_sign', 'A'),
    (294, 13, 'transmissions', 'N', '2'),
    (307,  8, 'usage_start_date', 'D', '%Y%m%d'),
    (315, 17, 'good_identifier', 'A'),
    # Intracommunity operations (certain)
    (236,  1, 'intracommunity_operation_type', 'N'),
    (237,  1, 'declaring_key', 'A'),
    (238,  2, 'intracommunity_country', 'A'),
    (240,  3, 'operation_term', 'N'),
    (243, 35, 'goods_description', 'A'),
    (278, 40, 'party_street', 'A'),
    (278, 22, 'party_city', 'A'),
    (278, 10, 'party_zip', 'A'),
    (350, 135, 'other_documentation', 'A'),
    )


def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(extract_record(current_line, PRESENTER_HEADER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if valid_record(current_line, DETAIL_RECORD):
            record = extract_record(current_line, DETAIL_RECORD)
        else:
            raise Exception('Invalid record: %s' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records

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
    (  2,  3, 'model', 'N', '=347'),
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
    (136,  9, 'party_count', 'N'),
    (145, 16, 'total', 'N', '2'),
    (161,  9, 'property_count', 'N'),
    (170, 15, 'lease_total', 'N', '2'),
    (391,  9, 'representative_nif', 'A'),
    (488, 13, 'digital_signature', 'A'),
    )

DECLARED_RECORD = (
    (  1,  1, 'record_code', 'N', '=2'),
    (  2,  3, 'model', 'N', '=347'),
    (  5,  4, 'fiscalyear', 'N'),
    (  9,  9, 'nif', 'A'),
    ( 18,  9, 'party_nif', 'A'),
    ( 27,  9, 'representative_nif', 'A'),
    ( 36, 40, 'party_name', 'A'),
    ( 76,  1, 'sheet_type', 'A', '=D'),
    ( 77,  2, 'province_code', 'N'),
    ( 79,  2, 'country_code', 'N'),
    ( 82,  1, 'operation_key', 'A'),
    ( 83, 16, 'operation_total', 'N', '2'),
    ( 99,  1, 'insurance', 'A'),
    (100,  1, 'business_premises_rent', 'A'),
    (101, 15, 'cash_amount', 'N', '2'),
    (116, 16, 'vat_liable_property_amount', 'N', '2'),
    (132,  4, 'fiscalyear_cash_operation', 'N'),
    (136, 16, 'first_quarter_amount', 'N', '2'),
    (152, 16, 'first_quarter_property_amount', 'N', '2'),
    (168, 16, 'second_quarter_amount', 'N', '2'),
    (184, 16, 'second_quarter_property_amount', 'N', '2'),
    (200, 16, 'third_quarter_amount', 'N', '2'),
    (216, 16, 'third_quarter_property_amount', 'N', '2'),
    (232, 16, 'fourth_quarter_amount', 'N', '2'),
    (248, 16, 'fourth_quarter_property_amount', 'N', '2'),
    )

# TODO: Doc says record_code is 2, but shouldn't it be 3?
PROPERTY_RECORD = (
    (  1,  1, 'record_code', 'N', '=2'),
    (  2,  3, 'model', 'N', '=347'),
    (  5,  4, 'fiscalyear', 'N'),
    (  9,  9, 'nif', 'A'),
    ( 18,  9, 'party_nif', 'A'),
    ( 27,  9, 'representative_nif', 'A'),
    ( 36, 40, 'party_name', 'A'),
    ( 76,  1, 'sheet_type', 'A', '=D'),
    (100, 15, 'total', 'A'),
    (115,  1, 'situation', 'N'),
    (116, 25, 'cadaster_number', 'A'),
    (141,  5, 'road_type', 'A'),
    (146, 50, 'street', 'A'),
    (196,  3, 'number_type', 'A'),
    (199,  5, 'number', 'N'),
    (204,  3, 'number_qualifier', 'A'),
    (207,  3, 'block', 'A'),
    (210,  3, 'doorway', 'A'),
    (213,  3, 'stair', 'A'),
    (216,  3, 'floor', 'A'),
    (219,  3, 'door', 'A'),
    (222, 40, 'complement', 'A'),
    (262, 30, 'city', 'A'),
    (292, 30, 'municipality', 'A'),
    (322,  5, 'municipality_code', 'A'),
    (327,  2, 'province_code', 'N'),
    (329,  5, 'zip', 'N'),
    )


def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(extract_record(current_line, PRESENTER_HEADER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if valid_record(current_line, DECLARED_RECORD):
            record = extract_record(current_line, DECLARED_RECORD)
        if valid_record(current_line, PROPERTY_RECORD):
            record = extract_record(current_line, PROPERTY_RECORD)
        else:
            raise Exception('Invalid record: %s' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records

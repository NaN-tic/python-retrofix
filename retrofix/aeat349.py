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
    (  2,  3, 'model', 'N', '=349'),
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
    (138,  9, 'intracommunity_operator_count', 'N'),
    (147, 15, 'intracommunity_amount', 'N', '2'),
    (162,  9, 'intracommunity_correction_count', 'N'),
    (171, 15, 'correction_amount', 'N', '2'),
    (391,  9, 'representative_nif', 'A'),
    (488, 13, 'digital_signature', 'A'),
    )

INTRACOMMUNITY_RECORD = (
    (  1,  1, 'record_code', 'N', '=2'),
    (  2,  3, 'model', 'N', '=349'),
    (  5,  4, 'fiscalyear', 'N'),
    (  9,  9, 'nif', 'A'),
    ( 76, 17, 'party_vat', 'A'),
    ( 93, 40, 'party_name', 'A'),
    (133,  1, 'operation_key', 'A'),
    (134, 13, 'base', 'N', '2'),
    )

AMMENDMENT_RECORD = (
    (  1,  1, 'record_code', 'N', '=2'),
    (  2,  3, 'model', 'N', '=349'),
    (  5,  4, 'fiscalyear', 'N'),
    (  9,  9, 'nif', 'A'),
    ( 76, 17, 'party_vat', 'A'),
    ( 93, 40, 'party_name', 'A'),
    (133,  1, 'operation_key', 'A'),
    (147,  4, 'ammendment_fiscalyear', 'N'),
    (151,  2, 'ammendment_period', 'A'),
    (153, 13, 'base', 'N', '2'),
    (166, 13, 'original_base', 'N', '2'),
    )


def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(extract_record(current_line, PRESENTER_HEADER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if valid_record(current_line, INTRACOMMUNITY_RECORD):
            record = extract_record(current_line, INTRACOMMUNITY_RECORD)
        if valid_record(current_line, AMMENDMENT_RECORD):
            record = extract_record(current_line, AMMENDMENT_RECORD)
        else:
            raise Exception('Invalid record: %s' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records

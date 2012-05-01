# encoding: utf8
##############################################################################
#
#    Copyright (C) 2011-2012 NaN Projectes de Programari Lliure, S.L.
#                            http://www.NaN-tic.com
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

# See lowlevel.py for record structures

PRESENTER_HEADER_RECORD = (
        (  1,  2, 'record_code', 'N', '=51'),
        (  3,  2, 'data_code', 'N', '=70'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'N'),
        ( 17,  6, 'creation_date', 'D', '%d%m%y'),
        ( 23,  6, 'free_1', 'A'),
        ( 29, 40, 'name', 'A'),
        ( 69, 20, 'free_2', 'A'),
        ( 89,  4, 'bank_code', 'N'),
        ( 93,  4, 'bank_office', 'N'),
        ( 97, 66, 'free_3', 'A'),
        )

ORDERING_HEADER_RECORD = (
        (  1,  2, 'record_code', 'N', '=53'),
        (  3,  2, 'data_code', 'N', '=70'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'N'),
        ( 17,  6, 'creation_date', 'D', '%d%m%y'),
        ( 23,  6, 'free_1', 'A'),
        ( 29, 40, 'name', 'A'),
        ( 69, 20, 'account', 'ACCOUNT'),
        ( 89,  8, 'free_2', 'A'),
        ( 97,  2, 'procedure', 'N', '=06'),
        ( 99, 52, 'free_3', 'A'),
        (151,  9, 'ine', 'A'),
        (160,  3, 'free_4', 'A'),
        )

REQUIRED_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', 'N', '=56'),
        (  3,  2, 'data_code', 'N', '=70'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'N'),
        ( 17, 12, 'reference', 'A'), # Código de referencia
        ( 29, 40, 'name', 'A'),
        ( 69, 20, 'account', 'ACCOUNT'),
        ( 89, 10, 'amount', 'N', '2'),
        ( 99,  6, 'return_code', 'A'), # Código para devoluciones
        (105, 10, 'internal_code', 'A'), # Código de referencia interna
        (115, 40, 'concept', 'A'), # Primer campo de concepto
        (155,  6, 'due_date', 'D', '%d%m%y'),
        (161,  2, 'free', 'A'),
        )

OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', 'N', '=56'),
        (  3,  2, 'data_code', 'N', '=70'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'N'),
        ( 17, 12, 'reference', 'A'), # Código de referencia
        ( 29, 40, 'concept_2', 'A'), # Segundo campo de concepto
        ( 69, 40, 'concept_3', 'A'), # Tercer campo de concepto
        (109, 10, 'concept_4', 'A'), # Cuarto campo de concepto
        (149, 14, 'free', 'A'),
        )

ADDRESS_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', 'N', '=56'),
        (  3,  2, 'data_code', 'N', '=76'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'N'),
        ( 17, 12, 'reference', 'A'), # Código de referencia
        ( 29, 40, 'payer_address', 'A'),
        ( 69, 35, 'payer_city', 'A'),
        (104,  5, 'payer_zip', 'A'),
        (109, 38, 'ordering_city', 'A'), # Localidad del ordenante
        (147,  2, 'province_code', 'A'), # Código de provincia
        (149,  6, 'origin_date', 'D', '%d%m%y'),
        (155,  8, 'free', 'A'),
        )

ORDERING_FOOTER_RECORD = (
        (  1,  2, 'record_code', 'N', '=58'),
        (  3,  2, 'data_code', 'N', '=70'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'N'),
        ( 17, 12, 'free_1', 'A'), # Código de referencia
        ( 29, 40, 'free_2', 'A'),
        ( 69, 20, 'free_3', 'A'),
        ( 89, 10, 'amount', 'N'), # Suma de importes del ordenante
        ( 99,  6, 'free_4', 'A'),
        (105, 10, 'payment_line_count', 'N'), # Número de créditos del ordenante
        (115, 10, 'record_count', 'N'), # Número registros del ordenante
        (125, 20, 'free_5', 'A'),
        (145, 18, 'free_6', 'A'),
        )

PRESENTER_FOOTER_RECORD = (
        (  1,  2, 'record_code', 'N', '=59'),
        (  3,  2, 'data_code', 'N', '=70'),
        (  5,  9, 'nif', 'A'),
        ( 14,  3, 'suffix', 'N'),
        ( 17, 12, 'free_1', 'A'), # Código de referencia
        ( 29, 40, 'free_2', 'A'),
        ( 69,  4, 'ordering_count', 'N'),
        ( 73, 16, 'free_4', 'A'),
        ( 89, 10, 'amount', 'N'), # Suma total de importes
        ( 99,  6, 'free_5', 'A'),
        (105, 10, 'payment_line_count', 'N'), # Número total de créditos
        (115, 10, 'record_count', 'N'), # Número total de registros de fichero
        (125, 20, 'free_6', 'A'),
        (145, 18, 'free_7', 'A'),
        )


def read(data):
    lines = data.splitlines()
    line_count = len(lines)

    records = []

    current_line = lines.pop(0)
    records.append(extract_record(current_line, PRESENTER_HEADER_RECORD))

    current_line = lines.pop(0)
    records.append(extract_record(current_line, ORDERING_HEADER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if valid_record(current_line, REQUIRED_INDIVIDUAL_RECORD):
            record = extract_record(current_line, REQUIRED_INDIVIDUAL_RECORD)
        elif valid_record(current_line, OPTIONAL_INDIVIDUAL_RECORD):
            record = extract_record(current_line, OPTIONAL_INDIVIDUAL_RECORD)
        elif valid_record(current_line, ADDRESS_INDIVIDUAL_RECORD):
            record = extract_record(current_line, ADDRESS_INDIVIDUAL_RECORD)
        elif valid_record(current_line, ORDERING_FOOTER_RECORD):
            record = extract_record(current_line, ORDERING_FOOTER_RECORD)
        elif valid_record(current_line, PRESENTER_FOOTER_RECORD):
            record = extract_record(current_line, PRESENTER_FOOTER_RECORD)
        else:
            raise BaseException('Invalid record: "%s"' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records


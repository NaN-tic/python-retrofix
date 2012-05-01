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

HEADER_001_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'), # Referencia de beneficiario
        (27,  3, 'data_code', 'N', '=001'),
        (30,  6, 'creation_date', 'D', '%d%m%y'), # Fecha de generación del soporte
        (36,  6, 'emission_date', 'D', '%d%m%y'), # Fecha de emisión de las órdenes
        (42,  4, 'bank_code', 'N'), # Entidad de destino del soporte
        (46,  4, 'bank_office', 'N'),  # Número de sucursal de la cuenta de cargo
        (50, 10, 'account_number', 'N'), # Número de la cuenta de cargo
        (60,  1, 'account_move_flag', 'A'), # Detalle del cargo: 0 = Un sólo apunte contable, 1 = Un apunte contable por Beneficiario
        (61,  3, 'free_2', 'A'),
        (64,  2, 'account_dc', 'N'),
        (66,  7, 'free_3', 'A'),
        )

HEADER_002_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=002'),
        (30, 36, 'name', 'A'), # Nombre del ordenante
        (66,  7, 'free_2', 'A'),
        )

HEADER_003_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'),
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=003'),
        (30, 36, 'address', 'A'), # Domicilio del ordenante
        (66,  7, 'free_2', 'A'),
        )

HEADER_004_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'),
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=004'),
        (30, 36, 'city', 'A'), # Plaza (localidad) del ordenante
        (66,  7, 'free_2', 'A'),
        )

HEADER_005_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=005'),
        (30, 12, 'referencia_12', 'A'), # Referencia 12 y 
        (42, 16, 'referencia_16', 'A'), # 16 de la remesa para apunte Total
        (58,  8, 'free_2', 'A'),
        (66,  7, 'free_3', 'A'),
        )

HEADER_007_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=007'),
        (30, 36, 'name', 'A'), # Por cuenta de
        (66,  7, 'free_2', 'A'),
        )

HEADER_008_RECORD = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=008'),
        (30, 36, 'address', 'A'), # Domicilio de Por cuenta de
        (66,  7, 'free_2', 'A'),
        )

RECORD_010 = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=010'),
        (30, 12, 'amount', 'N', '2'),
        (42, 18, 'spaces', 'A'),
        (60,  1, 'expenses'),
        (61,  1, 'concept'),
        (62,  1, 'sign'),
        (63,  2, 'unused', 'A'), # DC = (No se usa)
        (65,  1, 'free_2', 'A'),
        (66,  6, 'due_date', 'D', '%d%m%y'),
        (72,  1, 'free_3', 'A'),
        )

RECORD_011 = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=011'),
        (30, 36, 'name'), # Nombre del beneficiario
        (66,  6, 'cheque_date', 'D', '%d%m%y'), # Fecha del cheque
        (72,  1, 'free_2', 'A'),
        )

RECORD_012 = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=012'),
        (30, 36, 'address'), # Domicilio del beneficiario
        (72,  7, 'free_2', 'A'),
        )

RECORD_013 = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=013'),
        (30, 36, 'address'), # Continuación del domicilio del beneficiario
        (72,  7, 'free_2', 'A'),
        )

RECORD_014 = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=014'),
        (30,  5, 'zip'),  # Código postal
        (35, 31, 'city'), # y plaza del beneficiario
        (72,  7, 'free_2', 'A'),
        )

RECORD_015 = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=015'),
        (30, 36, 'province'),  # Provincia
        (72,  7, 'free_2', 'A'),
        )

# TODO: Translate 'concepto' to 'description' EVERYWHERE

RECORD_016 = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=016'),
        (30, 36, 'concept'),  # Concepto del documento / orden
        (72,  7, 'free_2', 'A'),
        )

RECORD_017 = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=017'),
        (30, 36, 'concept'),  # Continuación del concepto del documento
        (72,  7, 'free_2', 'A'),
        )

RECORD_018 = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=017'),
        (30, 18, 'dni', 'A'),  # DNI para los Cheques Nómina más un identificativo del beneficiario a continuación
        (48, 18, 'beneficiary_identifier', 'A'),
        (72,  7, 'free_2', 'A'),
        )

RECORD_019 = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=017'),
        (30, 12, 'referencia_12'),
        (42, 16, 'referencia_16'),
        (58,  8, 'free_2', 'A'), 
        (72,  7, 'free_3', 'A'),
        )

RECORD_018 = (
        ( 1,  2, 'record_code', 'N', '=03'), # 00
        ( 3,  4, 'operation_code', 'N', '=56'),
        ( 5, 10, 'ordering_code'),
        (15, 12, 'free_1', 'A'),
        (27,  3, 'data_code', 'N', '=017'),
        (30, 18, 'dni', 'A'),  # DNI para los Cheques Nómina más un identificativo del beneficiario a continuación
        (48, 18, 'beneficiary_identifier', 'A'),
        (72,  7, 'free_2', 'A'),
        )

# Structure:
# Depth
#c34_file_structure = (
#    FIRST_RECORD
#)


def read(data):
    lines = data.splitlines()
    line_count = len(lines)

    current_line = lines.pop(0)
    if valid_record(current_line, FILE_HEADER_RECORD):
        current_line = lines.pop(0)

    records = []
    if not valid_record(current_line, ACCOUNT_HEADER_RECORD):
        assert False, 'Expected account header record at line %d' % (line_count - len(lines))

    record = extract_record(current_line, ACCOUNT_HEADER_RECORD)
    records.append(record)
    current_line = lines.pop(0)
    while lines:
        if valid_record(current_line, MOVE_RECORD):
            record = extract_record(current_line, MOVE_RECORD)
        elif valid_record(current_line, MOVE_CONCEPT_RECORD):
            record = extract_record(current_line, MOVE_CONCEPT_RECORD)
        elif valid_record(current_line, MOVE_AMOUNT_EQUIVALENCE_RECORD):
            record = extract_record(current_line, MOVE_AMOUNT_EQUIVALENCE_RECORD)
        elif valid_record(current_line, ACCOUNT_FOOTER_RECORD):
            record = extract_record(current_line, ACCOUNT_FOOTER_RECORD)
            records.append(record)
            break
        else:
            record = extract_record(current_line, MOVE_RECORD)
            assert False, 'Invalid data at line %d' % (line_count - len(lines))
        records.append(record)
        current_line = lines.pop(0)

    return records

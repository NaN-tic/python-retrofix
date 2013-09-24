# encoding: utf8
##############################################################################
#
#    Copyright (C) 2011-2013 NaN Projectes de Programari Lliure, S.L.
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

from record import Record
from .fields import *

PRESENTER_HEADER_RECORD = (
        (  1,  2, 'record_code', Const('51')),
        (  3,  2, 'data_code', Const('70')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Number),
        ( 17,  6, 'creation_date', Date('%d%m%y')),
        ( 23,  6, 'free_1', Char),
        ( 29, 40, 'name', Char),
        ( 69, 20, 'free_2', Char),
        ( 89,  4, 'bank_code', Number),
        ( 93,  4, 'bank_office', Number),
        ( 97, 66, 'free_3', Char),
        )

ORDERING_HEADER_RECORD = (
        (  1,  2, 'record_code', Const('53')),
        (  3,  2, 'data_code', Const('70')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Number),
        ( 17,  6, 'creation_date', Date('%d%m%y')),
        ( 23,  6, 'free_1', Char),
        ( 29, 40, 'name', Char),
        ( 69, 20, 'account', Account),
        ( 89,  8, 'free_2', Char),
        ( 97,  2, 'procedure', Const('06')),
        ( 99, 52, 'free_3', Char),
        (151,  9, 'ine', Char),
        (160,  3, 'free_4', Char),
        )

REQUIRED_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', Const('56')),
        (  3,  2, 'data_code', Const('70')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Number),
        ( 17, 12, 'reference', Char), # Código de referencia
        ( 29, 40, 'name', Char),
        ( 69, 20, 'account', Account),
        ( 89, 10, 'amount', Numeric),
        ( 99,  6, 'return_code', Char), # Código para devoluciones
        (105, 10, 'internal_code', Char), # Código de referencia interna
        (115, 40, 'concept', Char), # Primer campo de concepto
        (155,  6, 'due_date', Date('%d%m%y')),
        (161,  2, 'free', Char),
        )

OPTIONAL_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', Const('56')),
        (  3,  2, 'data_code', Const('71')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Number),
        ( 17, 12, 'reference', Char), # Código de referencia
        ( 29, 40, 'concept_2', Char), # Segundo campo de concepto
        ( 69, 40, 'concept_3', Char), # Tercer campo de concepto
        (109, 10, 'concept_4', Char), # Cuarto campo de concepto
        (149, 14, 'free', Char),
        )

ADDRESS_INDIVIDUAL_RECORD = (
        (  1,  2, 'record_code', Const('56')),
        (  3,  2, 'data_code', Const('76')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Number),
        ( 17, 12, 'reference', Char), # Código de referencia
        ( 29, 40, 'payer_address', Char),
        ( 69, 35, 'payer_city', Char),
        (104,  5, 'payer_zip', Char),
        (109, 38, 'ordering_city', Char), # Localidad del ordenante
        (147,  2, 'province_code', Char), # Código de provincia
        (149,  6, 'origin_date', Date('%d%m%y')),
        (155,  8, 'free', Char),
        )

ORDERING_FOOTER_RECORD = (
        (  1,  2, 'record_code', Const('58')),
        (  3,  2, 'data_code', Const('70')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Number),
        ( 17, 12, 'free_1', Char), # Código de referencia
        ( 29, 40, 'free_2', Char),
        ( 69, 20, 'free_3', Char),
        ( 89, 10, 'amount', Numeric), # Suma de importes del ordenante
        ( 99,  6, 'free_4', Char),
        (105, 10, 'payment_line_count', Integer), # Número de créditos del ordenante
        (115, 10, 'record_count', Integer), # Número registros del ordenante
        (125, 20, 'free_5', Char),
        (145, 18, 'free_6', Char),
        )

PRESENTER_FOOTER_RECORD = (
        (  1,  2, 'record_code', Const('59')),
        (  3,  2, 'data_code', Const('70')),
        (  5,  9, 'nif', Char),
        ( 14,  3, 'suffix', Number),
        ( 17, 12, 'free_1', Char), # Código de referencia
        ( 29, 40, 'free_2', Char),
        ( 69,  4, 'ordering_count', Integer),
        ( 73, 16, 'free_4', Char),
        ( 89, 10, 'amount', Numeric), # Suma total de importes
        ( 99,  6, 'free_5', Char),
        (105, 10, 'payment_line_count', Integer), # Número total de créditos
        (115, 10, 'record_count', Integer), # Número total de registros de fichero
        (125, 20, 'free_6', Char),
        (145, 18, 'free_7', Char),
        )


def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, PRESENTER_HEADER_RECORD))

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, ORDERING_HEADER_RECORD))

    current_line = lines.pop(0)
    while lines:
        if Record.valid(current_line, REQUIRED_INDIVIDUAL_RECORD):
            record = Record.extract(current_line, REQUIRED_INDIVIDUAL_RECORD)
        elif Record.valid(current_line, OPTIONAL_INDIVIDUAL_RECORD):
            record = Record.extract(current_line, OPTIONAL_INDIVIDUAL_RECORD)
        elif Record.valid(current_line, ADDRESS_INDIVIDUAL_RECORD):
            record = Record.extract(current_line, ADDRESS_INDIVIDUAL_RECORD)
        elif Record.valid(current_line, ORDERING_FOOTER_RECORD):
            record = Record.extract(current_line, ORDERING_FOOTER_RECORD)
        elif Record.valid(current_line, PRESENTER_FOOTER_RECORD):
            record = Record.extract(current_line, PRESENTER_FOOTER_RECORD)
        else:
            raise BaseException('Invalid record: "%s"' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records


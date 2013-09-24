# encoding: utf8
##############################################################################
#
#    Copyright (C) 2011-2013 NaN Projectes de Programari Lliure, S.L.
#                            http://www.NaN-tic.com
#    Copyright (c) 2013 Zikzakmedia S.L. (http://zikzakmedia.com)
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

ORDERING_HEADER_RECORD = (
    (1, 2, 'record_code', Const('03')),
    (3, 2, 'operation_code', Const('62')),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'free_1', Char),
    (29, 3, 'data_number', Const('001')),
    (32, 6, 'send_date', Date('%d%m%y')),
    (38, 6, 'creation_date', Date('%d%m%y')),
    (44, 20, 'account', Account),
    (64, 1, 'charge_detail', Selection([
            ('0', 'false'),
            ('1', 'true')
            ])),
    (65, 8, 'free_2', Char),
    )

ORDERING_HEADER_002_RECORD = (
    (1, 2, 'record_code', Const('03')),
    (3, 2, 'operation_code', Const('62')),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'free_1', Char),
    (29, 3, 'data_number', Const('002')),
    (32, 36, 'name', Char),
    (68, 5, 'free_2', Char),
    )

ORDERING_HEADER_003_RECORD = (
    (1, 2, 'record_code', Const('03')),
    (3, 2, 'operation_code', Const('62')),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'free_1', Char),
    (29, 3, 'data_number', Const('003')),
    (32, 36, 'address', Char),
    (68, 5, 'free_2', Char),
    )

ORDERING_HEADER_004_RECORD = (
    (1, 2, 'record_code', Const('03')),
    (3, 2, 'operation_code', Const('62')),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'free_1', Char),
    (29, 3, 'data_number', Const('004')),
    (32, 36, 'city', Char),
    (68, 5, 'free_2', Char),
    )

ORDERING_HEADER_007_RECORD = (
    (1, 2, 'record_code', Const('03')),
    (3, 2, 'operation_code', Const('62')),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'free_1', Char),
    (29, 3, 'data_number', Const('007')),
    (32, 36, 'on_behalf_of', Char),
    (68, 5, 'free_2', Char),
    )

ORDERING_HEADER_008_RECORD = (
    (1, 2, 'record_code', Const('03')),
    (3, 2, 'operation_code', Const('62')),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'free_1', Char),
    (29, 3, 'data_number', Const('008')),
    (32, 36, 'address_on_behalf_of', Char),
    (68, 5, 'free_2', Char),
    )

NATIONAL_HEADER_RECORD = (
    (1, 2, 'record_code', Const('04')),
    (3, 2, 'operation_code', Const('56')),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'free_1', Char),
    (29, 3, 'free_2', Char),
    (32, 41, 'free_3', Char),
    )

# Required
DETAIL_001_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('010')),
    (32, 12, 'amount', Numeric),
    (44, 20, 'bank_account', Number),
    (64, 1, 'cost', Selection([
            ('1', 'payer'),
            ('2', 'recipient'),
            ])),
    (65, 1, 'concept', Selection([
            ('1', 'payroll'),
            ('8', 'pension'),
            ('9', 'other'),
            ])),
    (66, 1, 'direct_payment', Selection([
            ('1', 'true'),
            ('2', 'false'),
            ])),
    (67, 6, 'free_2', Char),
    )

# Required
DETAIL_002_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('011')),
    (32, 36, 'name', Char),
    (68, 5, 'free_1', Char),
    )

# Required for checks and promissory notes sent by mail to the recipient
DETAIL_003_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('012')),
    (32, 36, 'street', Char),
    (68, 5, 'free_1', Char),
    )

# Not required
DETAIL_004_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('013')),
    (32, 36, 'street2', Char),
    (68, 5, 'free_1', Char),
    )

# Required for checks and promissory notes sent by mail to the recipient
DETAIL_005_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('014')),
    (32, 36, 'zip_city', Char),
    (68, 5, 'free_1', Char),
    )

# Required for checks and promissory notes sent by mail to the recipient
DETAIL_006_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('015')),
    (32, 2, 'country_code', Char),
    # Code ISO of the target country
    # Case of target country will be Spain, set it to ES plus the name of the
    # province
    (34, 34, 'state', Char),
    (68, 5, 'free_1', Char),
    )

# Not required
DETAIL_007_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('016')),
    (32, 36, 'concept', Char),  # The same as recipient_nif
    (68, 5, 'free_1', Char),
    )

# Not required
DETAIL_008_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('017')),
    (32, 36, 'concept2', Char),  # The same as recipient_nif
    (68, 5, 'free_1', Char),
    )

# Not required
DETAIL_009_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('56', 'transfer'),
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('018')),
    (32, 36, 'beneficiary_nif', Char),  # The same as recipient_nif
    (68, 5, 'free_1', Char),
    )

# Not required
DETAIL_101_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('101')),
    (32, 36, 'message', Char),  # Letter message
    (68, 5, 'free_1', Char),
    )

DETAIL_102_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('102')),
    (32, 36, 'message', Char),  # Letter message
    (68, 5, 'free_1', Char),
    )

DETAIL_103_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('103')),
    (32, 36, 'message', Char),  # Letter message
    (68, 5, 'free_1', Char),
    )

# Required in promissory notes
DETAIL_910_RECORD = (
    (1, 2, 'record_code', Const('06')),
    (3, 2, 'operation_code', Selection([
            ('57', 'check'),
            ('58', 'promissory_note'),
            ('59', 'certified_payment'),
            ])),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'recipient_nif', Char),
    (29, 3, 'data_number', Const('910')),
    (32, 36, 'message', Char),  # Usually contains the date
    (68, 5, 'free_1', Char),
    )

NATIONAL_FOOTER_RECORD = (
    (1, 2, 'record_code', Const('08')),
    (3, 2, 'operation_code', Const('56')),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'free_1', Char),
    (29, 3, 'free_2', Char),
    (32, 12, 'amount', Numeric),
    (44, 8, 'payment_line_count', Integer),
    (52, 10, 'record_count', Integer),
    (62, 6, 'free_3', Char),
    (68, 5, 'free_4', Char),
    )

ORDERING_FOOTER_RECORD = (
    (1, 2, 'record_code', Const('09')),
    (3, 2, 'operation_code', Const('62')),
    (5, 9, 'nif', Char),
    (14, 3, 'suffix', Char),
    (17, 12, 'free_1', Char),
    (29, 3, 'free_2', Char),
    (32, 12, 'amount', Numeric),
    (44, 8, 'payment_line_count', Integer),
    (52, 10, 'record_count', Integer),
    (62, 6, 'free_3', Char),
    (68, 5, 'free_4', Char),
    )


def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, ORDERING_HEADER_RECORD))

# Por cada registro de Transferencias o Nóminas se constituirán
# obligatoriamente los registros tipo de Dato 010, 011, 012, 014 y,
# opcionalmente, el 013, 016 y 017.

# Por cada registro de Cheques Bancarios, Pagarés o Pagos Certificados se
# constituirán obligatoriamente los registros tipos de Dato 010, 011 y,
# opcionalmente, 012, 013, 014, 015, 016, 017 y 018. Los registros tipo de Dato
# 012, 013, 014 y 015 serán obligatorios para emisiones con carta.

    current_line = lines.pop(0)
    while lines:
        if Record.valid(current_line, ORDERING_HEADER_002_RECORD):
            record = Record.extract(current_line, ORDERING_HEADER_002_RECORD)
        elif Record.valid(current_line, ORDERING_HEADER_003_RECORD):
            record = Record.extract(current_line, ORDERING_HEADER_003_RECORD)
        elif Record.valid(current_line, ORDERING_HEADER_004_RECORD):
            record = Record.extract(current_line, ORDERING_HEADER_004_RECORD)
        elif Record.valid(current_line, NATIONAL_HEADER_RECORD):
            record = Record.extract(current_line, NATIONAL_HEADER_RECORD)
        elif Record.valid(current_line, DETAIL_001_RECORD):
            record = Record.extract(current_line, DETAIL_001_RECORD)
        elif Record.valid(current_line, DETAIL_002_RECORD):
            record = Record.extract(current_line, DETAIL_002_RECORD)
        elif Record.valid(current_line, DETAIL_003_RECORD):
            record = Record.extract(current_line, DETAIL_003_RECORD)
        elif Record.valid(current_line, DETAIL_004_RECORD):
            record = Record.extract(current_line, DETAIL_004_RECORD)
        elif Record.valid(current_line, DETAIL_005_RECORD):
            record = Record.extract(current_line, DETAIL_005_RECORD)
        elif Record.valid(current_line, DETAIL_006_RECORD):
            record = Record.extract(current_line, DETAIL_006_RECORD)
        elif Record.valid(current_line, DETAIL_007_RECORD):
            record = Record.extract(current_line, DETAIL_007_RECORD)
        elif Record.valid(current_line, DETAIL_101_RECORD):
            record = Record.extract(current_line, DETAIL_101_RECORD)
        elif Record.valid(current_line, DETAIL_102_RECORD):
            record = Record.extract(current_line, DETAIL_102_RECORD)
        elif Record.valid(current_line, DETAIL_103_RECORD):
            record = Record.extract(current_line, DETAIL_103_RECORD)
        elif Record.valid(current_line, DETAIL_910_RECORD):
            record = Record.extract(current_line, DETAIL_910_RECORD)
        elif Record.valid(current_line, NATIONAL_FOOTER_RECORD):
            record = Record.extract(current_line, NATIONAL_FOOTER_RECORD)
        elif Record.valid(current_line, ORDERING_FOOTER_RECORD):
            record = Record.extract(current_line, ORDERING_FOOTER_RECORD)
        else:
            record = Record.extract(current_line, DETAIL_001_RECORD)
            raise BaseException('Invalid record: "%s"' % current_line)
        records.append(record)
        current_line = lines.pop(0)
    return records

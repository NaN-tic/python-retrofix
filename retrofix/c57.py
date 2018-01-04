# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .exception import RetrofixException
from .fields import Const, Char, Number, Date, Numeric, Selection, Boolean
from .fields import BOOLEAN_W1
from .record import Record


FILE_HEADER = (
    (1, 2, 'record_code', Const('01')),
    (3, 2, 'operation_code', Const('70')),
    (5, 6, 'free_C', Char),
    (11, 8, 'sender_number', Number),
    (19, 3, 'free_D2', Char),
    (22, 1, 'free_D3', Char),
    (23, 4, 'entity_number', Number),
    (27, 10, 'free_E2', Char),
    (37, 6, 'presentation_date', Date('%d%m%y')),
    (43, 6, 'free_F2', Char),
    (49, 6, 'free_G', Char),
    (55, 20, 'free_H', Char),
    (75, 1, 'free_I', Char),
    (76, 14, 'free_J', Char),
    (90, 11, 'free_K', Char)
)


SENDER_HEADER = (
    (1, 2, 'record_code', Const('02')),
    (3, 2, 'operation_code', Const('70')),
    (5, 6, 'free_C', Char),
    (11, 8, 'sender_number', Char),
    (19, 3, 'sufix', Char),
    (22, 1, 'free_D3', Char),
    (23, 4, 'entity_number', Char),
    (27, 10, 'free_E2', Char),
    (37, 6, 'presentation_date', Date('%d%m%y')),
    (43, 6, 'free_F2', Char),
    (49, 6, 'free_G', Char),
    (55, 20, 'free_H', Char),
    (75, 1, 'free_I', Char),
    (76, 14, 'free_J', Char),
    (90, 11, 'free_K', Char)
)


INDIVIDUAL_RECORD = (
    (1, 2, 'record_code', Const('60')),
    (3, 2, 'operation_code', Const('70')),
    (5, 6, 'free_C', Char),
    (11, 8, 'sender_number', Char),
    (19, 3, 'sufix', Char),
    (22, 1, 'payment_channel', Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    ])),
    (23, 4, 'entity_number', Char),
    (27, 4, 'office_number', Char),
    (31, 6, 'date', Date('%d%m%y')),
    (37, 12, 'amount', Numeric),
    (49, 6, 'payment_identification', Date('%d%m%y')),
    (55, 4, 'bank_code', Char),
    (59, 4, 'bank_office', Char),
    (63, 2, 'bank_account_dc', Char),
    (65, 10, 'bank_account', Char),
    (75, 1, 'debit', Selection([
        (' ', 'No recurrent'),
        ('D', 'Recurrent')
    ])),
    (76, 1, 'cancel_code', Boolean(BOOLEAN_W1)),
    (77, 13, 'reference', Char),
    (90, 11, 'free_K', Char)
)

SENDER_FOOTER = (
    (1, 2, 'record_code', Const('80')),
    (3, 2, 'operation_code', Const('70')),
    (5, 6, 'free_C', Char),
    (11, 8, 'sender_number', Char),
    (19, 3, 'sufix', Char),
    (22, 1, 'free_D3', Char),
    (23, 6, 'number_of_records', Numeric(decimals=0)),
    (29, 8, 'free_E2', Char),
    (37, 12, 'total_amount', Numeric),
    (49, 6, 'free_G', Char),
    (55, 20, 'free_H', Char),
    (75, 1, 'free_I', Char),
    (76, 1, 'negative', Boolean(BOOLEAN_W1)),
    (77, 13, 'free_J2', Char),
    (90, 11, 'free_K', Char)
)

FILE_FOOTER = (
    (1, 2, 'record_code', Const('90')),
    (3, 2, 'operation_code', Const('70')),
    (5, 6, 'free_C', Char),
    (11, 8, 'sender_number', Char),
    (19, 3, 'free_D2', Char),
    (22, 1, 'free_D3', Char),
    (23, 6, 'number_of_records', Numeric(decimals=0)),
    (29, 8, 'free_E2', Char),
    (37, 12, 'total_amount', Numeric),
    (49, 6, 'free_G', Char),
    (55, 20, 'free_H', Char),
    (75, 1, 'free_I', Char),
    (76, 1, 'negative', Boolean(BOOLEAN_W1)),
    (77, 13, 'free_J2', Char),
    (90, 11, 'free_K', Char)
)


def read(data):
    lines = data.splitlines()
    records = []

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, FILE_HEADER))

    while len(lines) > 1:
        current_line = lines.pop(0)
        if Record.valid(current_line, SENDER_HEADER):
            record = Record.extract(current_line, SENDER_HEADER)
        elif Record.valid(current_line, INDIVIDUAL_RECORD):
            record = Record.extract(current_line, INDIVIDUAL_RECORD)
        elif Record.valid(current_line, SENDER_FOOTER):
            record = Record.extract(current_line, SENDER_FOOTER)
        else:
            raise RetrofixException('Invalid record: "%s"' % current_line)
        records.append(record)

    current_line = lines.pop(0)
    records.append(Record.extract(current_line, FILE_FOOTER))

    return records

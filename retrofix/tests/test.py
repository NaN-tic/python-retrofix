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

import os
import unittest
import datetime
from decimal import Decimal
import codecs

from retrofix.record import Record
from retrofix.fields import Char, Account, Number, Numeric, Integer, Date,\
    Boolean
from retrofix.exception import RetrofixException
from retrofix import c19
from retrofix import c32
from retrofix import c34_1_la_caixa as c34
from retrofix import c43
from retrofix import c58
from retrofix import c57
# Import them to test that have a valid definition
from retrofix import aeat182, aeat303, aeat340, aeat347, aeat349


def read_flat(file_name):
    file_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        file_name
    )
    return codecs.open(file_path, 'r', encoding='latin1').read()


class C19TestCase(unittest.TestCase):
    def setUp(self):
        self.data = read_flat('c19.txt')
        self.data = self.data.upper()
        # Presenter Header
        record = Record(c19.PRESENTER_HEADER_RECORD)
        record.record_code = '51'
        record.data_code = '80'
        record.nif = 'B65247983'
        record.suffix = '701'
        record.creation_date = datetime.datetime(2012, 2, 24)
        record.name = 'NAN PROJECTES DE PROGRAMARI LLIURE, S.L.'
        record.bank_code = '2059'
        record.bank_office = '0060'
        self.presenter_header = record

    def test0000_c19_read(self):
        records = c19.read(self.data)
        self.assertEqual(records[0], self.presenter_header)

    def test0001_c19_write(self):
        data = self.presenter_header.write()
        self.assert_(self.data.startswith(data))


class C32TestCase(unittest.TestCase):
    def setUp(self):
        self.data = read_flat('c32.txt')
        self.data = self.data.upper()
        # Presenter Header
        record = Record(c32.FILE_HEADER_RECORD)
        record.record_code = '02'
        record.data_code = '65'
        record.file_date = datetime.datetime(2011, 7, 4)
        record.number = '1280'
        record.bank_code = '2959'
        record.bank_office = '0912'
        self.file_header = record

    def test0000_c32_read(self):
        records = c32.read(self.data)
        self.assertEqual(records[0], self.file_header)

    def test0001_c32_write(self):
        data = self.file_header.write()
        self.assert_(self.data.startswith(data))


class C34TestCase(unittest.TestCase):
    def setUp(self):
        self.data = read_flat('c34.txt')
        self.data = self.data.upper()
        # Presenter Header
        record = Record(c34.ORDERING_HEADER_RECORD)
        record.record_code = '03'
        record.operation_code = '62'
        record.nif = 'B17616756'
        record.suffix = '000'
        record.data_number = '001'
        record.send_date = datetime.datetime(2012, 2, 24)
        record.creation_date = datetime.datetime(2012, 2, 24)
        record.account = '20594887510123456789'
        record.charge_detail = 'false'
        self.ordering_header = record

    def test0000_c34_read(self):
        records = c34.read(self.data)
        self.assertEqual(records[0], self.ordering_header)

    def test0001_c34_write(self):
        data = self.ordering_header.write()
        self.assert_(self.data.startswith(data))


class C43TestCase(unittest.TestCase):
    def setUp(self):
        self.data = read_flat('c43.txt')
        self.data = self.data.upper()
        # Account Header
        record = Record(c43.ACCOUNT_HEADER_RECORD)
        record.record_code = '11'
        record.bank_code = '2059'
        record.bank_office = '0060'
        record.account_number = '8000314221'
        record.start_date = datetime.datetime(2011, 11, 11)
        record.end_date = datetime.datetime(2011, 11, 20)
        record.initial_balance = Decimal('52530.44')
        record.currency_code = '978'
        record.information_mode = '2'
        record.customer_name = ''
        self.account_header = record

    def test0000_c43_read(self):
        records = c43.read(self.data)
        self.assertEqual(records[0], self.account_header)

    def test0001_c43_write(self):
        data = self.account_header.write()
        self.assertEqual(self.data[:len(data)], data)


class C58TestCase(unittest.TestCase):
    def setUp(self):
        self.data = read_flat('c58.txt')
        self.data = self.data.upper()
        # Presenter Header
        record = Record(c58.PRESENTER_HEADER_RECORD)
        record.record_code = '51'
        record.data_code = '70'
        record.nif = 'B65247983'
        record.suffix = '000'
        record.creation_date = datetime.datetime(2012, 2, 24)
        record.name = 'NAN PROJECTES DE PROGRAMARI LLIURE, S.L.'
        record.bank_code = '0075'
        record.bank_office = '1454'
        self.presenter_header = record

    def test0000_c58_read(self):
        records = c58.read(self.data)
        self.assertEqual(records[0], self.presenter_header)

    def test0001_c58_write(self):
        data = self.presenter_header.write()
        self.assert_(self.data.startswith(data))


class C57TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = read_flat('c57.txt')
        cls.data = cls.data.upper()

    def test_file_header(self):
        header_record = Record(c57.FILE_HEADER)
        header_record.record_code = '01'
        header_record.operation_code = '70'
        header_record.free_C = '57013 '
        header_record.sender_number = '22350466'
        header_record.entity_number = '0182'
        header_record.presentation_date = datetime.datetime(2015, 6, 26)

        records = c57.read(self.data)
        self.assertEqual(records[0], header_record)

    def test_sender_header(self):
        record = Record(c57.SENDER_HEADER)
        record.record_code = '02'
        record.operation_code = '70'
        record.sender_number = '22350466'
        record.sufix = '501'
        record.entity_number = '0182'
        record.presentation_date = datetime.datetime(2015, 6, 26)

        records = c57.read(self.data)
        self.assertEqual(records[1], record)

    def test_individual_records(self):
        record = Record(c57.INDIVIDUAL_RECORD)
        record.record_code = '60'
        record.operation_code = '70'
        record.sender_number = '22350466'
        record.sufix = '501'
        record.payment_channel = '2'
        record.entity_number = '0182'
        record.office_number = '0756'
        record.date = datetime.datetime(2015, 6, 26)
        record.amount = Decimal('23.39')
        record.payment_identification = datetime.datetime(2015, 6, 29)
        record.reference = '0000102109676'

        records = c57.read(self.data)
        self.assertEqual(records[2], record)

    def test_sender_footer(self):
        record = Record(c57.SENDER_FOOTER)
        record.record_code = '80'
        record.operation_code = '70'
        record.sender_number = '22350466'
        record.sufix = '501'
        record.number_of_records = 11
        record.total_amount = Decimal('1293.51')

        records = c57.read(self.data)
        self.assertEqual(records[11], record)

    def test_file_footer(self):
        record = Record(c57.FILE_FOOTER)
        record.record_code = '90'
        record.operation_code = '70'
        record.sender_number = '22350466'
        record.number_of_records = 13
        record.total_amount = Decimal('1293.51')

        records = c57.read(self.data)
        self.assertEqual(records[12], record)


class GenericTestCase(unittest.TestCase):

    def test_none_fields(self):
        'Test setting none values on fields'
        TEST_RECORD = (
            (1,  1, 'char', Char),
            (2, 22, 'account', Account),
            (22, 26, 'number', Number),
            (26, 30, 'numeric', Numeric),
            (30, 40, 'integer', Integer),
            (40, 48, 'date', Date('YYYYMMDD')),
            (48, 50, 'boolean', Boolean),
            )
        record = Record(TEST_RECORD)
        record.char = None
        record.account = None
        record.number = None
        with self.assertRaises(RetrofixException):
            record.numeric = None
        with self.assertRaises(RetrofixException):
            record.integer = None
        record.date = None
        record.boolean = None
        self.assertEqual(record.char, '')
        self.assertEqual(record.account, '')
        self.assertEqual(record.number, '')
        self.assertEqual(record.date, None)
        self.assertEqual(record.boolean, False)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(C19TestCase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(C32TestCase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(C34TestCase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(C43TestCase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(C58TestCase))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

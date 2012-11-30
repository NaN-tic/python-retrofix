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

import sys, os
DIR = os.path.abspath(os.path.normpath(os.path.join(__file__,
    '..', '..')))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))

import unittest
import datetime
import pprint
from decimal import Decimal
import codecs

from retrofix import lowlevel
from retrofix import c19
from retrofix import c32
from retrofix import c34_oe as c34
from retrofix import c43
from retrofix import c58

class C19TestCase(unittest.TestCase):
    def setUp(self):
        self.data = codecs.open('c19.txt', 'r', encoding='latin1').read().upper()
        # Presenter Header
        record = lowlevel.Record(c19.PRESENTER_HEADER_RECORD)
        record.record_code = '51'
        record.data_code = '80'
        record.nif = 'B65247983'
        record.suffix = '701'
        record.creation_date = datetime.datetime(2012, 2, 24)
        record.free = ''
        record.name = 'NaN Projectes de Programari Lliure, S.L.'
        record.free_1 = ''
        record.bank_code = '2059'
        record.bank_office = '0060'
        record.free_2 = ''
        record.free_3 = ''
        record.free_4 = ''
        self.presenter_header = record
        
    def test0000_c19_read(self):
        records = c19.read(self.data)
        self.assertEqual(records[0], self.presenter_header)

    def test0001_c19_write(self):
        data = lowlevel.write_record(self.presenter_header)
        self.assert_(self.data.startswith(data))


class C32TestCase(unittest.TestCase):
    def setUp(self):
        self.data = codecs.open('c32.txt', 'r', encoding='latin1').read().upper()
        # Presenter Header
        record = lowlevel.Record(c32.FILE_HEADER_RECORD)
        record.record_code = '02'
        record.data_code = '65'
        record.file_date = datetime.datetime(2011, 07, 04)
        record.number = '1280'
        record.bank_code = '2959'
        record.bank_office = '0912'
        self.file_header = record
        
    def test0000_c32_read(self):
        records = c32.read(self.data)
        self.assertEqual(records[0], self.file_header)

    def test0001_c32_write(self):
        data = lowlevel.write_record(self.file_header)
        self.assert_(self.data.startswith(data))


class C34TestCase(unittest.TestCase):
    def setUp(self):
        self.data = codecs.open('c34.txt', 'r', encoding='latin1').read().upper()
        # Presenter Header
        record = lowlevel.Record(c34.ORDERING_HEADER_RECORD)
        record.record_code = '03'
        #record.free_1 = ''
        record.data_code = '62'
        #record.free_2 = ''
        record.nif = 'B17616756'
        record.suffix = '000'
        record.data_number = '001'
        record.send_date = datetime.datetime(2012, 2, 24)
        record.creation_date = datetime.datetime(2012, 2, 24)
        record.account = '20150024519202333478'
        record.charge_detail = 'false'
        self.ordering_header = record
        
    def test0000_c34_read(self):
        records = c34.read(self.data)
        self.assertEqual(records[0], self.ordering_header)

    def test0001_c34_write(self):
        data = lowlevel.write_record(self.ordering_header)
        self.assert_(self.data.startswith(data))

class C43TestCase(unittest.TestCase):
    def setUp(self):
        self.data = codecs.open('c43.txt', 'r', encoding='latin1').read().upper()
        # Account Header
        record = lowlevel.Record(c43.ACCOUNT_HEADER_RECORD)
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
        record.free = ''
        self.account_header = record
        
    def test0000_c43_read(self):
        records = c43.read(self.data)
        self.assertEqual(records[0], self.account_header)

    def test0001_c43_write(self):
        data = lowlevel.write_record(self.account_header)
        self.assertEqual(self.data[:len(data)], data)

class C58TestCase(unittest.TestCase):
    def setUp(self):
        self.data = codecs.open('c58.txt', 'r', encoding='latin1').read().upper()
        # Presenter Header
        record = lowlevel.Record(c58.PRESENTER_HEADER_RECORD)
        record.record_code = '51'
        record.data_code = '70'
        record.nif = 'B65247983'
        record.suffix = '000'
        record.creation_date = datetime.datetime(2012, 2, 24)
        record.name = 'NaN Projectes de Programari Lliure, S.L.'
        record.bank_code = '0075'
        record.bank_office = '1454'
        self.presenter_header = record
        
    def test0000_c58_read(self):
        records = c58.read(self.data)
        self.assertEqual(records[0], self.presenter_header)

    def test0001_c58_write(self):
        data = lowlevel.write_record(self.presenter_header)
        self.assert_(self.data.startswith(data))


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

RetroFix documentation
======================

RetroFix is a python library for reading and writing fixed-size field text file
and more specifically for managing files from Spanish banks and public
institutions, including:

- CSB 19, 32, 34 (several versions), 43 & 58
- AEAT 303, 340, 347 & 349

Defining record structures
--------------------------

RetroFix allows an easy way to define the structure of fixed size records by
creating a tuple which contains a tuple of size 4 for each field, containing:
start position, length, name and type.

Start position and length are numeric fields which define where the field is
located in a given record. The name is the internal name of the field and type
is a class or instance of a class inheriting retrofix.fields.Field.

RetroFix provides the following field types (new ones can also be created):

Char
  This is the simplest one and stores the content in a string.

Const
  This one inherits Char but ensures that the record contains the exact
  characters defined as parameter of the constructor.

Account
  Inherits Char but checks that the value of the field is a valid bank account
  number as defined by Spanish bank number format.

Numeric
  Used for numeric fields. You can get and set the value using Decimals.

Integer
  Just like Numeric but with integers.

Date
  Ensures the field matches the date format supplied to the constructor.

Selection
  Only allows a given set of string values supplied to the constructor.

Boolean
  Similar to selection but only two values are accepted (supplied to the
  constructor) and you can set and get the values using a boolean.

Take a look at the following example:

::

   from retrofix import record
   from retrofix.fields import *

   RECORD = (
       (  1,  2, 'record_type', Const('XX')),
       (  3, 10, 'name', Char),
       ( 33, 15, 'amount', Number(sign=SIGN_N)),
       ( 38, 17, 'date', Date('%d%m%y')),
       )

   def read(data):
       lines = data.splitlines()
       records = []
       current_line = lines.pop(0)
       records.append(record.Record.extract(current_line, RECORD))
       return records

   lines = read(open('myfile.txt', 'r').read())
   f = open('newfile.txt')
   try:
       f.write(record.write(lines))
   finally:
       f.close()

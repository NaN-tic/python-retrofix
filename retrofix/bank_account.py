# Copyright (c) 2011-2012 NaN Projectes de Programari Lliure, S.L.  
#                         All Rights Reserved
#                         http://www.NaN-tic.com
# Copyright (c) 2009 Zikzakmedia S.L. (http://zikzakmedia.com) All Rights Reserved.
#                    Jordi Esteve <jesteve@zikzakmedia.com>

def crc(number):
    """
    Calculation of CRC of a 10 digit number
    left aligned filled in with zeros.

    param: number: string of size 10 with digit characters only
    return: Single digit integer with the result of the CRC calculation
    """

    assert len(number) == 10

    factor = (1,2,4,8,5,10,9,7,3,6)

    # CRC calculation
    value = 0
    for n in range(10):
        value += int(number[n]) * factor[n]

    # Reduction of CRC to a single digit
    result = 11 - value % 11
    if result == 10:
        result = 1
    elif result == 11: 
        result = 0
    return result

def bank_account_crc(bank, office, account):
    """Calculates CRC for a bank account"""

    number = '00%04d%04d' % (int(bank), int(office))
    assert len(number) == 10
    dc1 = crc(number)

    number = '%010d' % long(account)
    assert len(number) == 10
    dc2 = crc(number)

    result = '%d%d' % (dc1, dc2)
    assert len(result) == 2
    return result

def check_bank_account(account):
    number = ""
    for i in account:
        if i.isdigit():
            number += i
    if len(number) != 20:
        return 'invalid-size'

    bank = number[:4]
    office = number[4:8]
    dc = number[8:10]
    account = number[10:20]
    if dc != bank_account_crc(bank, office, account):
        return 'invalid-dc'

    return (bank, office, dc, account)

def valid_bank_account(account):
    if isinstance(check_bank_account(account), tuple):
        return True
    else:
        return False


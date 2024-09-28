import itertools
from itertools import count
import hashlib

key = 'wtnhxymk'
new_key = key
psw = ['-']*8
str_psw = ''
for digit in count(0):
        str_digit = str(digit)
        new_key += str_digit
        res_object = hashlib.md5(new_key.encode())  # Encode the string to bytes
        res = res_object.hexdigest()
        if res[:5] == '00000':
            if '-' in psw:
                if res[5].isdigit() and int(res[5]) < 9 and psw[int(res[5])] == '-':
                    psw[int(res[5])] = res[6]
                    str_psw = ''.join(psw)
                    print(str_psw)
            else:
                break
        new_key = key

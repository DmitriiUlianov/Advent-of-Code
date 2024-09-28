import itertools
from itertools import count
import hashlib

key = 'wtnhxymk'
new_key = key
psw = ''
for digit in count(0):
        str_digit = str(digit)
        new_key += str_digit
        res_object = hashlib.md5(new_key.encode())  # Encode the string to bytes
        res = res_object.hexdigest()
        if res[:5] == '00000':
            if len(psw) < 8:
                psw += res[5]
            else:
                print(psw)
                break
        new_key = key

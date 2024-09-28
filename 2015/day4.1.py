import hashlib

key = 'iwrupvqb'
new_key = key
digit = 0
while True:
        str_digit = str(digit)
        new_key += str_digit
        res_object = hashlib.md5(new_key.encode())  # Encode the string to bytes
        res = res_object.hexdigest()
        if res[:5] == '00000':
            print(digit)
            print(res)
            break
        digit += 1
        new_key = key

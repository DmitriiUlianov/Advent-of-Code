Str = "3113322113"
n = 0
while n < 50:
    new_Str = ""
    length = len(Str)
    idx = 0
    count = 1
    while idx < length:
        if idx < length - 1 and Str[idx] == Str[idx + 1]:
            count += 1    
        else:
            new_Str += str(count)
            new_Str += Str[idx]
            count = 1
        idx += 1 
    Str = new_Str
    n += 1
print(len(Str))

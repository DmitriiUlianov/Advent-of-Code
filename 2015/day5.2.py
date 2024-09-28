with open("input.txt", "r") as file:
    cont = [line.strip() for line in file]

nice_str = 0

for Str in cont:
    length = len(Str)

    check1 = 0
    for idx, i in enumerate(Str):
        if idx + 3 < length:
            j = Str[idx + 1]
        while idx + 3 < length:
            if i == Str[idx + 2]:
                if j == Str[idx + 3]:
                    check1 += 1
                    break
            idx += 1
        if check1 == 1:
            break

    check2 = 0
    for idx, i in enumerate(Str):
        if idx + 2 < length:
            if i == Str[idx + 2]:
                check2 += 1
                break

    if check1 + check2 == 2:
        nice_str += 1
    
print(nice_str)

with open("input.txt", "r") as file:
    cont = [line.strip() for line in file]

nice_str = 0

for Str in cont:
    length = len(Str)

    check1 = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_vowels = 0
    for i in Str:
        if i in vowels:
            count_vowels += 1
        if count_vowels == 3:
            check1 += 1 
            break
    
    check2 = 0
    for idx, i in enumerate(Str):
        if idx < length - 1 and i == Str[idx + 1]:
            check2 += 1
            break

    check3 = 0
    #unwanted = ['ab', 'cd', 'pq', 'xy']
    unwanted = 0
    for idx, i in enumerate(Str):
        if i == 'a':
            if idx < length - 1 and Str[idx + 1] == 'b':
                unwanted += 1
                break
        if i == 'c':
            if idx < length - 1 and Str[idx + 1] == 'd':
                unwanted += 1
                break
        if i == 'p':
            if idx < length - 1 and Str[idx + 1] == 'q':
                unwanted += 1
                break
        if i == 'x':
            if idx < length - 1 and Str[idx + 1] == 'y':
                unwanted += 1
                break
    if unwanted == 0:
        check3 += 1

    if check1 + check2 + check3 == 3:
        nice_str += 1
    
print(nice_str)

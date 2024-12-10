from itertools import combinations_with_replacement

with open("input.txt", "r") as file:
    cont = []
    for line in file:
        cont.append(line.split())

def evaluate(equation):
    result = equation[0] + equation[2] if equation[1] == '+' else equation[0]*equation[2]
    new_equation = equation[3:].copy()
    for idx, i in enumerate(new_equation):
        if isinstance(i, str):
            if i == '+':
                result += new_equation[idx + 1]
            else:
                result *= new_equation[idx + 1]       
    return result

total = 0
for item in cont:
    res = int(item[0][:len(item[0]) - 1])
    nums = item[1:].copy()
    digits = [int(i) for i in nums]
    signs = ['+','*','+','*','+','*','+','*','+','*']
    digits_len = len(digits)

    comb = set((combinations_with_replacement(signs, digits_len - 1)))
    for string in comb:
        equat = []
        string_len = len(string)
        for idx, i in enumerate(digits):
            equat.append(digits[idx])
            if idx < string_len:
                equat.append(string[idx])
        if evaluate(equat) == res:
            total += res 
            break

print(total)

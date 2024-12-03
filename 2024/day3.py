with open("input.txt", "r") as file:
    cont = file.read()

cont = cont.split('mul(')

res = 0
for line in cont:
        num1 = 0
        num2 = 0
        if ',' in line and ')' in line:
            part1 = line.split(',')
            if part1[0].isdigit():
                num1 = int(part1[0])
                if ')' in part1[1]:
                    part2 = part1[1].split(')')
                    if part2[0].isdigit():
                        num2 = int(part2[0])
                        res += num1*num2
print(res)   

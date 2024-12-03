with open("input.txt", "r") as file:
    cont = file.read()

cont = cont.split('do()')

res = 0
for line1 in cont:
    num1 = 0
    num2 = 0
    line2 = line1.split('don\'t')
    if 'mul(' in line2[0]:
        line3 = line2[0].split('mul(')
        for line4 in line3:
            if ',' in line4 and ')' in line4:
                part1 = line4.split(',')
                if part1[0].isdigit():
                    num1 = int(part1[0])
                    if ')' in part1[1]:
                        part2 = part1[1].split(')')
                        if part2[0].isdigit():
                            num2 = int(part2[0])
                            res += num1*num2
print(res) 

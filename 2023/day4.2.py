import fileinput 
import re
res = [0]*200

def func(my_line):
    parts = re.split(r':|\|', my_line)
    card = parts[0].split()
    part1 = parts[1].split()
    part2 = parts[2].split()
    card_num = int(card[1])
    res[card_num] += 1
    card_value = res[card_num]
    print(card_num)
    print(res)
    for j in part2:
        if j in part1:
            card_num += 1
            print(card_num)
            res[card_num] += card_value
            print(res)
            
my_in = []
for line in fileinput.input(files ='input'):
    my_in.append(line.strip())
print(my_in)
    
for i in my_in:
    func(i)
    print("xxx")
    
print(res)
print(sum(res))

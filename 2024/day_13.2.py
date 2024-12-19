import re
import numpy as np

with open("input.txt", "r") as file:
    comb = []
    res = []
    n = 0
    for line in file:
        parts = re.split(' |, |\n', line)
        for item in parts:
            if '+' in item or '=' in item:
                if '+' in item:
                    item = item.split('+')
                elif '=' in item:
                    item = item.split('=')
                
                n += 1
                if n <= 6:
                    res.append(int(item[1]))
                if n == 6:
                    comb.append(res)
                    res = []
                    n = 0

total = 0
n = str(10000000000000)
for nums in comb:
    a = np.array([[nums[0], nums[2]], [nums[1], nums[3]]])
    b = np.array([ int(n + str(nums[4])), int(n + str(nums[5])) ])
    x = np.linalg.solve(a, b)
    print(x)
    print(x[0])
    print(x[1])
    print(round(x[0],1))
    print(round(x[1],1))
    if (round(x[0],1) - round(x[0])) == 0 and (round(x[1],1) - round(x[1])) == 0:
        total += 3*round(x[0]) + round(x[1])
        print(1)
    else:
        print(0)
        
print(total) # 4199821452475189258 too high

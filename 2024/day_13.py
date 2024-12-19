import re
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
print(comb)

import numpy as np
total = 0
for nums in comb:
    a = np.array([[nums[0], nums[2]], [nums[1], nums[3]]])
    b = np.array([nums[4], nums[5]])
    x = np.linalg.solve(a, b)
    print(x)
    print(x[0])
    print(x[1])
    if int(x[0]) <= 100 and int(x[1]) <= 100 and (round(x[0],1) - int(x[0])) == 0 and (round(x[1],1) - int(x[1])) == 0:
        total += 3*int(x[0]) + int(x[1])
        
print(total) #21571 too low

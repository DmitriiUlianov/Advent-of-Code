import re
import numpy as np
lights = np.zeros((1000,1000))

f = open ("input.txt", "r")
my_in = []
for line in f:
    my_in.append(line.strip())
#print(my_in)

for line in my_in:
    items = []
    items = re.split(" |,", line)
    #print(items)
    if items[1] == "on":
        x1 = int(items[2])
        x2 = int(items[5])
        y1 = int(items[3])
        y2 = int(items[6])
        while y1 <= y2:
            while x1 <= x2:
                lights[x1][y1] = 1
                x1 += 1
            y1 += 1
            x1 = int(items[2])
    elif items[1] == "off":
        x1 = int(items[2])
        x2 = int(items[5])
        y1 = int(items[3])
        y2 = int(items[6])
        while y1 <= y2:
            while x1 <= x2:
                lights[x1][y1] = 0
                x1 += 1
            y1 += 1
            x1 = int(items[2])
    else:
        x1 = int(items[1])
        x2 = int(items[4])
        y1 = int(items[2])
        y2 = int(items[5])
        while y1 <= y2:
            while x1 <= x2:
                if lights[x1][y1] == 0:
                    lights[x1][y1] = 1
                else:
                    lights[x1][y1] = 0
                x1 += 1
            y1 += 1
            x1 = int(items[1])

print(lights)
print(lights.sum())

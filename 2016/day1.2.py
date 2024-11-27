import sys

with open("input.txt", "r") as file:
    cont = file.read()

cont = cont.split(", ")
x = int(cont[0][1])
y = 0
flag = 1
coord = list(zip(range(0,(x + 1)), [0]*(x + 1)))
new_coord = []
for idx, i in enumerate(cont[1:]):
    dir = i[0]
    dist = int(i[1:])
    if idx % 2 != 0:
        if dir == 'L' and flag == 1 or dir == 'R' and flag == -1:
            new_coord = list(zip(range((x - dist), x), [y]*dist))
            x -= dist
            flag = -1
        else:
            new_coord = list(zip(range((x + 1),(x + 1 + dist)), [y]*dist))
            x += dist
            flag = 1
    else:
        if dir == 'R' and flag == 1 or dir == 'L' and flag == -1:
            new_coord = list(zip([x]*dist, range((y - dist), y)))
            y -= dist
            flag = -1
        else:
            new_coord = list(zip([x]*dist, range((y + 1),(y + 1 + dist))))
            y += dist
            flag = 1
    
    for i in new_coord:
        if i in coord:
            print(abs(i[0]) + abs(i[1]))
            sys.exit()
        else:
            coord.append(i)
            
    print(coord)

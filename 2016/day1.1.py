with open("input.txt", "r") as file:
    cont = file.read()

cont = cont.split(", ")
x = int(cont[0][1])
y = 0
flag = 1
for idx, i in enumerate(cont[1:]):
    dir = i[0]
    dist = int(i[1:])
    if idx % 2 != 0:
        if dir == 'L' and flag == 1 or dir == 'R' and flag == -1:
            x -= dist
            flag = -1
        else:
            x += dist
            flag = 1
    else:
        if dir == 'R' and flag == 1 or dir == 'L' and flag == -1:
            y -= dist
            flag = -1
        else:
            y += dist
            flag = 1

print(abs(x) + abs(y))

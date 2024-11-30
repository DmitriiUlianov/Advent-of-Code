with open("input.txt", "r") as file:
    cont = file.read()

cont = cont.split("\n")

nums = {
    (0,0): 1,
    (1,0): 2,
    (2,0): 3,
    (0,1): 4,
    (1,1): 5,
    (2,1): 6,
    (0,2): 7,
    (1,2): 8,
    (2,2): 9
}
x = 1
y = 1
code = []
for line in cont:
    for i in line:
        if i == 'U' and y > 0:
            y -= 1
        elif i == 'D' and y < 2:
            y += 1
        elif i == 'R' and x < 2:
            x += 1
        elif i == 'L' and x > 0:
            x -= 1
    code.append(nums[(x,y)])

print(code)

with open("input.txt", "r") as file:
    cont = file.read()

cont = cont.split("\n")

nums = {
    (0,0): 2,
    (1,0): 3,
    (2,0): 4,
    (0,1): 6,
    (1,1): 7,
    (2,1): 8,
    (0,2): 'A',
    (1,2): 'B',
    (2,2): 'C',

    (1,-1): 1,
    (1,3): 'D',
    (-1,1): 5,
    (3,1): 9
}
x = -1
y = 1
code = []
for line in cont:
    for i in line:
        if i == 'U' and ((y > 0 and (x == 0 or x == 2)) or (y > -1 and x == 1)):
            y -= 1
        elif i == 'D' and ((y < 2 and (x == 0 or x == 2)) or (y < 3 and x == 1)):
            y += 1
        elif i == 'R' and ((x < 2 and (y == 0 or y == 2)) or (x < 3 and y == 1)):
            x += 1
        elif i == 'L' and ((x > 0 and (y == 0 or y == 2)) or (x > -1 and y == 1)):
            x -= 1
  
    code.append(nums[(x,y)])

print(code)

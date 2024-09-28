f = open ("in", "r")
my_in = ""
santa = ""
robo_santa = ""
houses = [[0,0]]
for i in f:
    my_in += i
for index, i in enumerate(my_in):
    if index%2 == 0:
        santa += i
    else:
        robo_santa += i
        
def func(my_string):  
    x = 0
    y = 0
    for i in my_string:
        if i == "^":
            y += 1
        elif i == "v":
            y -= 1
        elif i == ">":
            x += 1
        elif i == "<":
            x -= 1
        house_coord = [x, y]    
        if house_coord not in houses:
            houses.append(house_coord)

func(santa)
func(robo_santa)

print(houses)
print(len(houses))

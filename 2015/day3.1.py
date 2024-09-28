f = open ("in", "r")
my_in = ""
x = 0
y = 0
houses = [[0,0]]
house_coord = [x, y]
for i in f:
    my_in += i
   
for i in my_in:
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
  
print(houses)
print(len(houses))

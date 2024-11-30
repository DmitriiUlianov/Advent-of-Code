'''
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
'''

# with plot
import sys
import matplotlib.pyplot as plt

with open("input.txt", "r") as file:
    cont = file.read()

cont = cont.split(", ")
x = int(cont[0][1])
y = 0
flag = 1
coord = list(zip(range(0,(x + 1)), [0]*(x + 1)))
new_coord = []


# Create the plot
plt.ion()  # Enable interactive mode
    
# Create the initial plot
fig, ax = plt.subplots()

# Optional: add labels or title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Easter Bunny Headquarters')

# Plot initial point
ax.scatter(*zip(*coord), color = 'red', s = 100) # dots
ax.plot(*zip(*coord), color = 'red', linewidth = 8) # line

# Pause briefly to update the plot
plt.pause(1)
    


for idx, i in enumerate(cont[1:]):
    dir = i[0]
    dist = int(i[1:])
    if idx % 2 != 0:
        if dir == 'L' and flag == 1 or dir == 'R' and flag == -1:
            new_coord = list(zip(range((x - dist), x), [y]*dist))
            new_coord.sort(reverse = True)
            x -= dist
            flag = -1
        else:
            new_coord = list(zip(range((x + 1),(x + 1 + dist)), [y]*dist))
            x += dist
            flag = 1
    else:
        if dir == 'R' and flag == 1 or dir == 'L' and flag == -1:
            new_coord = list(zip([x]*dist, range((y - dist), y)))
            new_coord.sort(reverse = True)
            y -= dist
            flag = -1
        else:
            new_coord = list(zip([x]*dist, range((y + 1),(y + 1 + dist))))
            y += dist
            flag = 1

    
    for i in new_coord:
        if i in coord:
            print(abs(i[0]) + abs(i[1]))
            ax.scatter(i[0], i[1], color = 'red', s = 200) # dots
        else:
            coord.append(i)

    # Update the scatter plot by adding the new point
    ax.scatter(*zip(*coord), color = 'blue')  
    ax.plot(*zip(*coord), color = 'blue') 

    # Pause briefly to update the plot
    plt.pause(0.5)

# Keep the plot displayed after the loop ends
plt.show(block=True)

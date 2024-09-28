import sys
with open("input.txt", "r") as file:
    line = file.read()
length = len(line)
res = 0
i = 0
pos = 0
while i < length:
    pos += 1
    if line[i] == "(":
        res += 1
    elif line[i] == ")":
        res -= 1
        if res == -1:
            print(pos)
            sys.exit()
    i += 1
print(res)
 

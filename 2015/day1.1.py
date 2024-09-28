with open("input.txt", "r") as file:
    line = file.read()
length = len(line)
res = 0
i = 0
while i < length:
    if line[i] == "(":
        res += 1
    elif line[i] == ")":
        res -= 1
    i += 1
print(res)

with open("input.txt", "r") as file:
    cont = file.read()

cont = cont.split()
cont = [int(i) for i in cont]
length = len(cont)
l = []
idx = 0
res = 0
while idx < length:
    l.extend([cont[idx], cont[idx + 1], cont[idx + 2]])
    l.sort()
    if l[0] + l[1] > l[2]:
        res += 1
    idx += 3
    l = []

print(res)

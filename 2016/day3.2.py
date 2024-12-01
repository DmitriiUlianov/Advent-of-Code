with open("input.txt", "r") as file:
    cont = file.read()

cont = cont.split()
cont = [int(i) for i in cont]
length = len(cont)
l = []
idx = 0
count = 0
res = 0
while idx < length:
    l.extend([cont[idx], cont[idx + 3], cont[idx + 6]])
    l.sort()
    if l[0] + l[1] > l[2]:
        res += 1
    l = []
    count += 1 
    if count < 3:
        idx += 1
    else:
        idx += 7
        count = 0

print(res)

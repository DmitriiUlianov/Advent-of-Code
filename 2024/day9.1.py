with open("input.txt", "r") as file:
    cont = file.read()
nums = []
nums += cont
nums = [int(i) for i in nums]
print(nums)

data = []
k = 0
for idx, i in enumerate(nums):
    if idx % 2 == 0:
        while i > 0:
            data.append(k)
            i -= 1
        k += 1
    else:
        while i > 0:
            data.append('.')
            i -= 1

while '.' in data:
    idx = data.index('.')
    data[idx],data[-1] = data[-1],data[idx]
    data.pop(-1)
    l = len(data)
    while data[-1] == '.':
        data.pop(-1)
        l -= 1
        
res = 0
for idx, i in enumerate(data):
    res += i*idx
print(res)

with open("input.txt", "r") as file:
    cont = file.read()
nums = []
nums += cont
nums = [int(i) for i in nums]
#print(nums)

data = ''
k = 0
for idx, i in enumerate(nums):
    if idx % 2 == 0:
        data += str(k)*i
        k += 1
    else:
        data += '.'*i
#print(data)

while '.' in data:
    idx = data.index('.')
    l = len(data)
    while data[-1] == '.':
        data = data[:l-1]
        l -= 1
    string = ''
    string += data[0:idx] + data[l - 1] + data[idx + 1:l - 1]
    data = string
    #print(data)
#print(data)
res = 0
for idx, i in enumerate(data):
    res += int(data[idx])*idx
print(res) #91381988682 to low

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
print(data)


while '.' in data:
    idx = data.index('.')
    l = len(data)
    while data[-1] == '.':
        #data = data[:l-1]
        data.pop(-1)
        l -= 1
    '''   
    new_data = []
    new_data.append(data[0:idx])
    new_data.append(data[l - 1])
    new_data.append(data[idx + 1:l - 1])
    data = new_data.copy()
    '''
    #print(data[idx])
    #print(data[-1])
    if '.' in data:
        data[idx],data[-1] = data[-1],data[idx]
        data.pop(-1)
        print(data)
print(data)

res = 0
for idx, i in enumerate(data):
    res += int(i)*idx
print(res) #91381988682 to low

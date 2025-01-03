with open("input.txt", "r") as file:
    cont = file.read()
nums = []
nums += cont
nums = [int(i) for i in nums]

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

#print(data)

j = len(data) - 1
length = j
first_dot = data.index('.')
while j > first_dot:
    #print(length)
    #print(j)
    numbers = 1
    end = j
    
    while data[j] == data[j - 1]:
        j -= 1
        numbers += 1
    j -= 1
    
    while data[j] == '.':
        j -= 1
    
    i = 0
    while i < j:
        if data[i] == '.':
            space = 0
            start = i

            while data[i] == '.':
                i += 1
                space += 1
            #print(space)
            #print(numbers)
            if space >= numbers:
                while numbers > 0:
                    #print(data[end])
                    #print('data[end]', data[end])
                    data[start],data[end] = data[end],data[start]
                    start += 1
                    end -= 1
                    numbers -= 1
                #print(data)
                #print('j', j)
                break
            #print('j', j)

        i += 1

#print(data)
res = 0
for idx, i in enumerate(data):
    if i != '.':
        res += i*idx
print(res) # 6467290913294 too high

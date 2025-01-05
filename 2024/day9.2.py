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

j = len(data) - 1
length = j
first_dot = data.index('.')
while j > first_dot:
    numbers = 1
    end = j
    
    while data[j] == data[j - 1]:
        j -= 1
        numbers += 1
    j -= 1
    
    i = 0
    while i < j:
        if data[i] == '.':
            space = 0
            start = i

            while data[i] == '.':
                i += 1
                space += 1
            if space >= numbers:
                while numbers > 0:
                    data[start],data[end] = data[end],data[start]
                    start += 1
                    end -= 1
                    numbers -= 1
                break
        i += 1
        
    while data[j] == '.':
        j -= 1

res = 0
for idx, i in enumerate(data):
    if i != '.':
        res += i*idx
print(res)

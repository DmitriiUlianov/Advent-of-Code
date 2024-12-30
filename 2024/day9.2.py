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

i = 0
j = len(data) - 1
while i != j:
    #for m in data:
        space = 0
        numbers = 1
        start = i
        end = j
        if data[i] == '.':
            print(i)
            print(data)

            while data[i] == '.':
                i += 1
                space += 1
            if data[j] == data[j - 1]:
                while data[j] == data[j - 1]:
                    #print('data[j]', data[j])
                    #print('data[j-1]',data[j - 1])
                    j -= 1
                    numbers += 1
                j -= 1
                #print('1', data[j])
                #print('1', data[j-1])
                if data[j] == '.':
                    #print(data[j - 1])
                    while data[j] == '.':
                        j -= 1
                    
                
            #print(space)
            #print(numbers)
            print(space >= numbers)
            if space >= numbers:
                while numbers > 0:
                    
                    data[start],data[end] = data[end],data[start]
                    start += 1
                    end -= 1
                    numbers -= 1
        
        i += 1
                
'''           
res = 0
for idx, i in enumerate(data):
    res += i*idx
print(res)
'''

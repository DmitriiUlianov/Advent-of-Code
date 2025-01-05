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
first_dot = data.index('.')
while j > first_dot:
    count_numbers = 1
    end_of_digit = j
    
    while data[j] == data[j - 1]:
        j -= 1
        count_numbers += 1
    j -= 1
    
    i = 0
    while i <= j:
        if data[i] == '.':
            count_space = 0
            start_of_space = i

            while data[i] == '.':
                i += 1
                count_space += 1
                
            if count_space >= count_numbers:
                while count_numbers > 0:
                    data[start_of_space],data[end_of_digit] = data[end_of_digit],data[start_of_space]
                    start_of_space += 1
                    end_of_digit -= 1
                    count_numbers -= 1
                break
        i += 1
        
    while data[j] == '.':
        j -= 1

res = 0
for idx, i in enumerate(data):
    if i != '.':
        res += i*idx
print(res)

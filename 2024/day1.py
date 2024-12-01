with open("input.txt", "r") as file:
    cont = file.read()

cont = cont.split()

even_nums = []
odd_nums = []
count = 0
for i in cont:
    if count % 2 == 0:
        even_nums.append(int(i))
    else:
        odd_nums.append(int(i))
    count += 1

res = 0
similarity = 0

for i in even_nums:
    similarity += i*odd_nums.count(i)
    
while len(even_nums) > 0:
    res += abs(min(odd_nums) - min(even_nums))
    even_nums.remove(min(even_nums))
    odd_nums.remove(min(odd_nums))

print(res) # part 1
print(similarity) # part 2

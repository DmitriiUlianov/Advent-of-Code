with open("input.txt", "r") as file:
    cont = [line.strip() for line in file]
rules = []
for i in cont:
    pairs = i.split("|")
    pairs = [int(i) for i in pairs]
    rules.append(pairs)

with open("input2.txt", "r") as file:
    cont = [line.strip() for line in file]
update = []
for i in cont:
    nums = i.split(",")
    nums = [int(i) for i in nums]
    update.append(nums)

valid = []
modif = []
for nums in update:
    l = len(nums)
    error = 0
    temp = nums.copy()
    for idx, i in enumerate(nums[:l - 1]):
        j = idx + 1
        while j < l:
            pair = []
            pair.append(nums[idx])
            pair.append(nums[j])
            if pair not in rules:
                temp[idx], temp[j] = temp[j], temp[idx]
                error = 1
            nums = temp.copy()
            j += 1
                              
    if error == 0:
        valid.append(nums)
    else:
        modif.append(temp)

res_valid = 0
for idx, i in enumerate(valid):
    res_valid += valid[idx][len(i)//2]
print(res_valid) # part 1

res_modif = 0
for idx, i in enumerate(modif):
    res_modif += modif[idx][len(i)//2]
print(res_modif) # part 2

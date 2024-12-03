with open("input.txt", "r") as file:
    cont = file.read()

cont = cont.split("\n")

count = 0
for line in cont:
    nums = line.split()
    nums = [int(i) for i in nums]

    l = len(nums)

    idx = 0
    safe = 0
    if nums[0] > nums[1]:
        for i in range(l - 1):
            if 1 <= nums[idx] - nums[idx + 1] <= 3:
                idx += 1
            else:
                safe = 1
                break

    elif nums[0] <= nums[1]:
        for i in range(l - 1):
            if 1 <= nums[idx + 1] - nums[idx] <= 3:
                idx += 1
            else:
                safe = 1
                break

    if safe == 0:
        count += 1
 
print(count)

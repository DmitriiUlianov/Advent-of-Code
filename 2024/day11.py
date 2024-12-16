nums = '7568 155731 0 972 1 6919238 80646 22'
nums = nums.split()
nums = [int(i) for i in nums]
n = 0
while n < 75:
    updated = []
    for idx, i in enumerate(nums):
        l = len(str(i))
        if i == 0:
            updated.append(1)
        elif l % 2 == 0:
            num1 = int(str(i)[:l//2])
            num2 = int(str(i)[l//2:])
            updated.append(num1)
            updated.append(num2)
        else:
            updated.append(2024*i)
    nums = updated.copy()
    n += 1
    if n == 25:
        print(len(updated)) # part 1
print(len(updated)) # part 2

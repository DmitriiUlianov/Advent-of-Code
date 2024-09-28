f = open("input.txt", "r")
res = 0
for line in f:
    area = 0
    line.strip()
    items = line.split("x")
    nums = [int(i) for i in items]
    nums.sort()
    ribbon = 2*nums[0] + 2*nums[1]
    bow = nums[0]*nums[1]*nums[2]
    res += (ribbon + bow) 

print(res)

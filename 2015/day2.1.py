f = open("input.txt", "r")
res = 0
for line in f:
    area = 0
    line.strip()
    items = line.split("x")
    nums = [int(i) for i in items]
    area = 2*nums[0]*nums[1] + 2*nums[1]*nums[2] + 2*nums[2]*nums[0]
    nums.sort()
    paper = nums[0]*nums[1]
    res += (area + paper) 

print(res)
    

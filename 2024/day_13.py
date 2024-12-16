with open("input.txt", "r") as file:
    comb = []
    res = []
    n = 0
    for line in file:
        for item in line:
            if '+' in item:
                num = item.split('+')
            elif '=' in item:
                num = item.split('=')
        n += 1
        if n < 4:
            res.append(int(num[1]))
        else:
            comb.append(res)
            n = 0
        
print(comb)

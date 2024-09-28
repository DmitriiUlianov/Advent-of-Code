with open ("input.txt", "r") as file:
    for line in file:
        digit = ""
        total = 0
        idx = 0
        for i in line:           
            if line[idx].isdigit() or line[idx] == '-':  
                digit += line[idx]   
            elif len(digit) > 0:
                total += int(digit)
                digit = ""
            idx += 1
print(total) 

import fileinput 
x = 0

for line in fileinput.input(files ='1.1'): 
    temp = ""
    
    for i in line:
        if i.isdigit():
            temp += i
            break
            
    rLine = line[::-1]
    for i in rLine:
        if i.isdigit():
            temp += i
            break       
            
    x += int(temp)
    
print(x)

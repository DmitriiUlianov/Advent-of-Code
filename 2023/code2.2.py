import fileinput 
import re
split1 = []
split2 = []
split3 = []
summ = 0
for line in fileinput.input(files ='2.1'):
    split1 = line.split(":")
    split2 = re.split(r' |, |; |\n', split1[1])
    split3 = split1[0].split()
    print(split3)
    print(split2)
    mul = 0
    indx = 0
    blueN = 0
    greenN = 0
    redN = 0
    count = 0
    for i in split2:
        count += 1
        if i == "blue":
            if blueN < int(split2[count - 2]):
                blueN = int(split2[count - 2])
        elif i == "red":
            if redN < int(split2[count - 2]):
                redN = int(split2[count - 2])
        elif i == "green":
            if greenN < int(split2[count - 2]):
                greenN = int(split2[count - 2])
                
    mul = greenN*blueN*redN
    print(mul)
    summ += mul    
            
print(summ)
   

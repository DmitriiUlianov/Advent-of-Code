import fileinput 

#summ = 0
myList = []
gears = []
for line in fileinput.input(files ='3.1'):
    lengthLine = len(line)
    for i in line:
        if i != "\n":
            myList.append(i)
            
LastIndx = len(myList) - 1
k = lengthLine

string = ""
num = 0
indxList = []
for indx, i in enumerate(myList):
    if i.isdigit():
        string += i
        indxList.append(indx)
    else:
        if len(string) != 0:
            num = int(string)
            length = len(indxList)
            
            minIndx = 0
            if indxList[0] == 0:
                minIndx = indxList[0]
            else:
                minIndx = indxList[0] - 1
                
            maxIndx = indxList[0] + length
            
            if myList[minIndx] == "*":
                #summ += num
                gears.append(num)
                gears.append(minIndx)
                
            elif myList[maxIndx] == "*":
                gears.append(num)
                gears.append(maxIndx)
               
            else:
                flag = 0
                if LastIndx - maxIndx >= k:
                    maxIndxStrAfter = maxIndx + k
                    minIndxStrAfter = minIndx + k
                    while minIndxStrAfter <= maxIndxStrAfter:
                        if myList[minIndxStrAfter] == "*":
                            #summ += num
                            gears.append(num)
                            gears.append(minIndxStrAfter)
                            #flag = 1
                            break
                        else:
                            minIndxStrAfter += 1
                        
                if maxIndx >= k and flag == 0:
                    maxIndxStrBefore = maxIndx - k
                    minIndxStrBefore = minIndx - k
                    while minIndxStrBefore <= maxIndxStrBefore:
                        if myList[minIndxStrBefore] == "*":
                            #summ += num
                            gears.append(num)
                            gears.append(minIndxStrBefore)
                            break
                        else:
                            minIndxStrBefore += 1
                       
            string = ""
            num = 0
            indxList = []
            
        else:
            continue

GearsResult = 0
for indx, i in enumerate(gears):
    firstGear = 0
    secondGear = 0
    if indx % 2 != 0:
        x = gears.count(i)
        if x >= 2:
            firstGear = gears[indx - 1]
            for indx2, i2 in enumerate(gears[indx + 1:]):
                if indx2 % 2 != 0:
                    if i2 == i:
                        secondGear = gears[indx + 1:][indx2 - 1]
                        GearsResult += firstGear*secondGear
                        
print(GearsResult) 
print(gears)

        

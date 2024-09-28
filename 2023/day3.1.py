import fileinput 

summ = 0
myList = []
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
            
            if myList[minIndx] != "." and minIndx != 0:
                summ += num
            elif myList[maxIndx] != ".":
                summ += num
               
            else:
                flag = 0
                if LastIndx - maxIndx >= k:
                    maxIndxStrAfter = maxIndx + k
                    minIndxStrAfter = minIndx + k
                    while minIndxStrAfter <= maxIndxStrAfter:
                        if myList[minIndxStrAfter] != "." and not myList[minIndxStrAfter].isdigit():
                            summ += num
                            flag = 1
                            break
                        else:
                            minIndxStrAfter += 1
                        
                if maxIndx >= k and flag == 0:
                    maxIndxStrBefore = maxIndx - k
                    minIndxStrBefore = minIndx - k
                    while minIndxStrBefore <= maxIndxStrBefore:
                        if myList[minIndxStrBefore] != "." and not myList[minIndxStrBefore].isdigit():
                            summ += num
                            break
                        else:
                            minIndxStrBefore += 1
                       
            string = ""
            num = 0
            indxList = []
            
        else:
            continue
    
print(summ)
        

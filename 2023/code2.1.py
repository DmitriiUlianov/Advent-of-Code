import fileinput 
import re
split1 = []
split2 = []
split3 = []
games = 0
for line in fileinput.input(files ='2.1'):
    split1 = line.split(":")
    split2 = re.split(r' |,|;|\n', split1[1])
    split3 = split1[0].split()
    print(split3)
    print(split2)
    flag = 0
    j = 0
    indx = 0
    for i in split2:
        indx = split2.index(i)
        if i.isdigit():
            j = int(i)
            if j > 14:
                flag = 1
                break
            elif j == 14:
                if split2[indx + 1] == "blue":
                    continue
                else:
                    flag = 1
                    break
            elif j == 13:
                if split2[indx + 1] != "red":
                    continue
                else:
                    flag = 1
                    break
            else:
                continue
    if flag == 0:
        games += int(split3[1])
        print(split3[1], end = " ")
    print("\n")
      

print(games)
    

import fileinput 
x = 0
digits = ["null","one","two","three","four","five","six","seven","eight","nine"]
nums = ["0","1","2","3","4","5","6","7","8","9"]

for line in fileinput.input(files ='1.1'):
    
    temp = ""
    
    indx = 0
    string = ""
    flag = 0
       
    for i in line:
        if i.isdigit():
            temp += i
            break
        elif i.isalpha():
            string += i
            for j in digits:
                if j in string:
                    indx = digits.index(j)
                    temp += nums[indx]
                    flag = 1
                    break
            if flag == 1:
                break
    
    indx = 0
    string = ""        
    rLine = line[::-1]
    flag = 0
    
    for i in rLine:
        if i.isdigit():
            temp += i
            break 
        elif i.isalpha():
            string += i
            rString = string[::-1]
            for j in digits:
                if j in rString:
                    indx = digits.index(j)
                    temp += nums[indx]
                    flag = 1
                    break
            if flag == 1:
                break
    
    x += int(temp)
    
print(x)

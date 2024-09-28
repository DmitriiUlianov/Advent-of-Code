import fileinput 
summ = 0
for line in fileinput.input(files ='input'):
    my_line = line.strip()
    parts = my_line.split (":")
    data = parts[1].split("|")
    win_num = data[0].split()
    my_num = data[1].split()
    print(win_num)
    print(my_num)
    points = 0
    flag = 0
    for i in my_num:
        if i in win_num:
            if flag == 0:
                points += 1
                flag += 1
            else:
                points *= 2
    summ += points
print(summ)

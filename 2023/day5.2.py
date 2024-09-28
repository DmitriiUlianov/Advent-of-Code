import fileinput

my_in = []
for line in fileinput.input(files ='input'):
    my_in.append(line.strip())
my_in.append("")

first_str = my_in[0].split(": ")
my_list_str = first_str[1].split()
my_list = [eval(i) for i in my_list_str]
#lenght = len(my_list)
#print("my_list:", my_list)

my_list_range = []
x = 0  
y = 0
for num in my_list:
    if x == 0:
        x = num
    else:
        y = num
        my_list_range.append(range(x, x + y))
        x = 0
        y = 0

lenght = len(my_list_range)
print("my_list_range", my_list_range)

def func(indx):
    
    temp_my_list_range = [0]*lenght
    for index, i in enumerate(my_list_range):
        temp_my_list_range[index] = my_list_range[index]
    
    print("temp_my_list_range", temp_my_list_range)
       
    while my_in[indx + 1] != "":
        new_list = my_in[indx + 1].split()
        nums = [eval(i) for i in new_list]
        dest_range = range(nums[0], nums[0] + nums[2])
        print("dest_range:", dest_range)
        source_range = range(nums[1], nums[1] + nums[2])
        print("source_range:", source_range)
        
        temp_index = 0
        for index, j in enumerate(my_list_range):
            #print(type(my_list_range[index]))
            
            index1 = 0
            index2 = 0

            if my_list_range[index][0] > source_range[-1] or my_list_range[index][-1] < source_range[0]:
                temp_index += 1
                continue
            elif my_list_range[index][0] <= source_range[0]:
                temp_my_list_range.pop(temp_index)
                index1 = source_range.index(source_range[0])
                if my_list_range[index][-1] > source_range[0]:
                    index2 = source_range.index(source_range[-1])
                    if my_list_range[index][0] < source_range[0]:
                        temp_my_list_range.append(range(my_list_range[index][0], source_range[0] - 1))
                        
                    temp_my_list_range.append(range(dest_range[index1], dest_range[index2]))
                    
                    if my_list_range[index][-1] > source_range[0]:
                        temp_my_list_range.append(range(source_range[0] + 1, my_list_range[index][-1]))
                        
                else:
                    index2 = source_range.index(my_list_range[index][-1])
                    #
                    #
        
            elif my_list_range[index][0] > source_range[0]:
                
                temp_my_list_range.pop(temp_index)
                index1 = source_range.index(my_list_range[index][0])
                if my_list_range[index][-1] > source_range[0]:
                    index2 = source_range.index(source_range[-1])
                    #
                    #
                else:
                    index2 = source_range.index(my_list_range[index][-1])
                    #
                    #
                
                
               

        indx += 1
    
    print("temp_my_list_range", temp_my_list_range)
    
    for index, i in enumerate(my_list_range):
        my_list_range[index] = temp_my_list_range[index]

for indx, line in enumerate(my_in):
    if "map" in line:
        func(indx)
        break
   
print("min", min(my_list))

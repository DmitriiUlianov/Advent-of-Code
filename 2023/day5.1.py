import fileinput

my_in = []
for line in fileinput.input(files ='input'):
    my_in.append(line.strip())
my_in.append("")

first_str = my_in[0].split(": ")
my_list_str = first_str[1].split()
my_list = [eval(i) for i in my_list_str]
lenght = len(my_list)
#print("my_list:", my_list)

def func(indx):
    
    temp_my_list = [0]*lenght
    for index, i in enumerate(my_list):
        temp_my_list[index] = my_list[index]
        
    while my_in[indx + 1] != "":
        new_list = my_in[indx + 1].split()
        nums = [eval(i) for i in new_list]
        dest_range = range(nums[0], nums[0] + nums[2])
        #print("dest_range:", dest_range)
        source_range = range(nums[1], nums[1] + nums[2])
        #print("source_range:", source_range)
        
        for index, j in enumerate(my_list):
            if j in source_range:
                j_indx = source_range.index(j)
                temp_my_list[index] = dest_range[j_indx]
       
        indx += 1
        
    for index, i in enumerate(my_list):
            my_list[index] = temp_my_list[index]

for indx, i in enumerate(my_in):
    if i == "seed-to-soil map:":
        func(indx)
        #print("my_list1",my_list)
        
    elif i == "soil-to-fertilizer map:":
        func(indx)
        #print("my_list2",my_list)
    
    elif i == "fertilizer-to-water map:":
        func(indx)
        #print("my_list3",my_list)
        
    elif i == "water-to-light map:":
        func(indx)
        #print("my_list4",my_list)
        
    elif i == "light-to-temperature map:":
        func(indx)
        #print("my_list5",my_list)
        
    elif i == "temperature-to-humidity map:":
        func(indx)
        #print("my_list6",my_list)
        
    elif i == "humidity-to-location map:":
        func(indx)
        #print("my_list7",my_list)

print(min(my_list))



import fileinput

my_in = []
for line in fileinput.input(files ='input'):
    my_in.append(line.strip())
my_in.append("")

first_str = my_in[0].split(": ")
my_list_str = first_str[1].split()
my_list = [eval(i) for i in my_list_str]
lenght = len(my_list)
#print("my_list:", my_list)

def func(indx):
    
    temp_my_list = [0]*lenght
    for index, i in enumerate(my_list):
        temp_my_list[index] = my_list[index]
        
    while my_in[indx + 1] != "":
        new_list = my_in[indx + 1].split()
        nums = [eval(i) for i in new_list]
        dest_range = range(nums[0], nums[0] + nums[2])
        #print("dest_range:", dest_range)
        source_range = range(nums[1], nums[1] + nums[2])
        #print("source_range:", source_range)
        
        for index, j in enumerate(my_list):
            if j in source_range:
                j_indx = source_range.index(j)
                temp_my_list[index] = dest_range[j_indx]
       
        indx += 1
        
    for index, i in enumerate(my_list):
            my_list[index] = temp_my_list[index]

for indx, line in enumerate(my_in):
    if "map" in line:
        func(indx)
    
print(min(my_list))


import sys
f = open("input.txt", "r")
my_in = []
for line in f:
    my_in.append(line.strip().split())

dic = {}
while True:
    for item in my_in:
        length = len(item)

        if length == 3:
            if item[0].isdigit():
                dic[item[2]] = int(item[0])
            elif item[0] in dic.keys():
                dic[item[2]] = dic[item[0]]

        elif "NOT" in item:
            if item[1] in dic.keys():
                dic[item[3]] = 65535 - dic[item[1]]
            elif item[1].isdigit():
                dic[item[3]] = 65535 - int(item[1])

        elif "AND" in item:
            if item[0] in dic.keys() and item[2] in dic.keys():
                dic[item[4]] = dic[item[0]] & dic[item[2]]
            elif item[0] in dic.keys() and item[2].isdigit():
                dic[item[4]] = dic[item[0]] & int(item[2])
            elif item[0].isdigit() and item[2] in dic.keys():
                dic[item[4]] = int(item[0]) & dic[item[2]]
            elif item[0].isdigit() and item[2].isdigit():
                dic[item[4]] = int(item[0]) & int(item[2])

        elif "OR" in item:
            if item[0] in dic.keys() and item[2] in dic.keys():
                dic[item[4]] = dic[item[0]] | dic[item[2]]
            elif item[0] in dic.keys() and item[2].isdigit():
                dic[item[4]] = dic[item[0]] | int(item[2])
            elif item[0].isdigit() and item[2] in dic.keys():
                dic[item[4]] = int(item[0]) | dic[item[2]]
            elif item[0].isdigit() and item[2].isdigit():
                dic[item[4]] = int(item[0]) | int(item[2])

        elif "LSHIFT" in item:
            if item[0] in dic.keys():
                dic[item[4]] = dic[item[0]] << int(item[2])

        elif "RSHIFT" in item:
            if item[0] in dic.keys():
                dic[item[4]] = dic[item[0]] >> int(item[2])
        
        if "a" in dic.keys():
            print("a =", dic["a"])
            sys.exit()
        

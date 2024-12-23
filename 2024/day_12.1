cont = []
filelen = 0
with open("input.txt", "r") as file:
    for line in file:
        cont += '.' + line.strip()
        linelen = len(line.strip()) + 1
        filelen += linelen
cont.append('.')

idx_dict = [] 
area = []
perimeter = []
for idx, i in enumerate(cont):
    current_area = []
    if i.isalpha() and idx not in idx_dict:
        
        # finding erea:
        current_area.append(idx)
        for j in current_area:
            if j - 1 not in current_area and cont[j - 1] == i:
                current_area.append(j - 1)
            if j + 1 not in current_area and cont[j + 1] == i:
                current_area.append(j + 1)
            if j - linelen >= 0 and j - linelen not in current_area and cont[j - linelen] == i:
                current_area.append(j - linelen)
            if j + linelen <= filelen and j + linelen not in current_area and cont[j + linelen] == i:
                current_area.append(j + linelen)
        idx_dict.extend(current_area)
        area.append(len(current_area))
        
        # finding perimeter:
        fence = 0
        for n in current_area:
            if cont[n - 1] != i:
                fence += 1
            if cont[n + 1] != i:
                fence += 1
            if n - linelen >= 0:
                if cont[n - linelen] != i:
                    fence += 1
            else:
                fence += 1
            if n + linelen <= filelen:
                if cont[n + linelen] != i:
                    fence += 1
            else:
                fence += 1
        perimeter.append(fence)

price = sum(map(lambda x, y: x * y, area, perimeter))
print(price)
    

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
        
        '''
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
        '''
        # finding 2 perimetr:
        print(current_area)
        print(linelen)
        
        l = len(current_area)
        fence = 1
        idx = 0
        
        for idx, i in enumerate(current_area):
            if len(current_area) > 1 and current_area[idx + 1] - current_area[idx] == 1:
                while len(current_area) > 1 and current_area[idx + 1] - current_area[idx] == 1:
                    current_area.pop(0)
                    print(current_area)
                fence += 1
             
            
            elif current_area[idx] + linelen == 1:
                while idx + linelen in current_area:
                    idx += linelen
                fence += 1
            
                
            elif idx - linelen in current_area:
                while idx - linelen in current_area:
                    idx -= linelen
                fence += 1
            
            
            #idx += 1

        print("fence ", fence)
        if fence < 4:
            fence = 4
            
price = sum(map(lambda x, y: x * y, area, perimeter))
print(price)

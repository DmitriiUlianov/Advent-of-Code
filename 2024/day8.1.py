cont = []
filelen = 0
with open("input.txt", "r") as file:
    for line in file:
        cont += line.strip()
        linelen = len(line.strip())
        filelen += linelen

print(cont)

antinodes = 0
for i_idx, i in enumerate(cont):
    if i != '.' and cont[i_idx - 1] == '.' and cont[i_idx + 1] == '.':
        for j_idx, j in enumerate(cont[i_idx + 1:]):
            if j == i and cont[j_idx - 1] == '.' and cont[j_idx + 1] == '.':
                j_idx += i_idx
                print(i_idx)
                print(j_idx)
                i_row = i_idx // linelen
                i_num = i_idx - linelen*i_row
                j_row = j_idx // linelen
                j_num = j_idx - linelen*j_row
                if i_num <= j_num:
                    if i_num - (j_num - i_num) >= 0 and i_row - (j_row - i_row) >= 0:
                        antinodes += 1
                    if j_num + (j_num - i_num) <= linelen and j_row + (j_row - i_row) <= filelen:
                        antinodes += 1
                else:
                    if i_num + (i_num - j_num) <= linelen and i_row - (j_row - i_row) >= 0:
                        antinodes += 1
                    if j_num - (i_num - j_num) >= 0 and j_row + (j_row - i_row) <= filelen:
                        antinodes += 1

print(antinodes) # between 290 and 435
                    
                
                
        
        

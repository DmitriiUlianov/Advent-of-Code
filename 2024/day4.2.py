cont = ''
filelen = 0
with open("input.txt", "r") as file:
    for line in file:
        cont += '.' + line.strip()
        strlen = len(line.strip()) + 1
        filelen += strlen

res = 0
word1 = 'MAS'
word2 = 'SAM'

def func(word1, word2):
    func_res = 0
    for idx, i in enumerate(cont):
        if idx + 2*strlen + 2 < filelen and cont[idx] == word1[0]:
            if cont[idx + 2] == word2[0]:
                if cont[idx + strlen + 1] == word1[1]:
                    if cont[idx + 2*strlen] == word2[2]:
                        if cont[idx + 2*strlen + 2] == word1[2]:
                            func_res += 1
    return func_res

res += func(word1, word1)
res += func(word1, word2)
res += func(word2, word1)
res += func(word2, word2)

print(res)

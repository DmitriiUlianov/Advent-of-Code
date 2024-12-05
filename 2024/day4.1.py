cont = ''
filelen = 0
with open("input.txt", "r") as file:
    for line in file:
        cont += '.' + line.strip()
        strlen = len(line.strip()) + 1
        filelen += strlen

res = 0
word1 = 'XMAS'
word2 = 'SAMX'

res += cont.count(word1)
res += cont.count(word2)

def func(word, sign, step1, step2, step3):
    func_res = 0
    for idx, i in enumerate(cont):
        if cont[idx] == word[0]:
            if idx + strlen + sign*step1 < filelen and cont[idx + strlen + sign*step1] == word[1]:
                if idx + 2*strlen + sign*step2 < filelen and cont[idx + 2*strlen + sign*step2] == word[2]:
                    if idx + 3*strlen + sign*step3 < filelen and cont[idx + 3*strlen + sign*step3] == word[3]:
                        func_res += 1
    return func_res

res += func(word1, 1, 0, 0, 0)
res += func(word1, 1, 1, 2, 3)
res += func(word1, -1, 1, 2, 3)

res += func(word2, 1, 0, 0, 0)
res += func(word2, 1, 1, 2, 3)
res += func(word2, -1, 1, 2, 3)

print(res)

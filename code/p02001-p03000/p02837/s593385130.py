def GetBitStands(val):
    i = 0
    while val > 0 :
        if (val & 1) != 0 : yield i
        i += 1
        val >>= 1

def GetBitCount(val):
    cnt = 0
    while val > 0 :
        if (val & 1) != 0 :
            cnt += 1
        val >>= 1
    return cnt

def IsAllHonest(bit_map,peaple):
    for index in GetBitStands(bit_map):
       if not peaple[index].is_honest(bit_map) :
           return False
    return True

def Honests(peaple):
    for i in range(1 << len(peaple)):
        if IsAllHonest(i,peaple):
            yield i

class UserWord:
    def __init__(self):
        self.has_word = 0
        self.word = 0
    def is_honest(self,bit):
        return (bit ^ self.word)&self.has_word == 0



num = int(input())

peaple = []


for i in range(num):
    p = UserWord()
    a = int(input())
    for j in range(a):
        x,y = map(int,input().split())
        #i番目の人が「x番目の人はyである」と証言
        mask = 1 << (x-1)
        p.has_word |= mask
        if y != 0:
            p.word |= mask
    peaple.append(p)

max = 0
for kouho in Honests(peaple):
    temp = GetBitCount(kouho)
    if max < temp:
        max = temp

print(max)

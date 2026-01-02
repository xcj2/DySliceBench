from collections import defaultdict
def getN():
    return int(input())

def getMN():
    a = input().split()
    b = [int(i) for i in a]
    return b[0],b[1]

def getlist():
    a = input().split()
    b = [int(i) for i in a]
    return b

def syori(instr):
    moji = defaultdict(list)
    for i, s in enumerate(instr):
        moji[s].append(i)
    #lis = list(moji.values())

    lisstrs = []
    for v in moji.values():
        lisstr = "@".join([str(i) for i in(v)])
        lisstrs.append(lisstr)
    st = set(lisstrs)
    #print(st)
    return (st)



stra = input()
strb = input()

aset  = syori(stra)
bset = syori(strb)

if aset == bset:
    print("Yes")
else:
    print("No")


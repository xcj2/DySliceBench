# ABC 076
def getInt(): return int(input())
def zeros(n): return [0]*n
def genBit(n): # n個の0/1のリストを生成　[0]から変化
    blist = zeros(n)
    for i in range(2**n):
        for k in range(n):
            blist[k] = i%2
            i //= 2
        yield blist
def db(x): 
    global debug
    if debug: print(x)
debug = False

N = getInt()
K = getInt()
minD = 0
for b in genBit(N):
    d = 1
    for i in range(N):
        if b[i]==0: d*=2
        if b[i]==1: d+=K
    if minD==0: minD = d
    elif d<minD: minD = d
    db(minD)
print(minD)


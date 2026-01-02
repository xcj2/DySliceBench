# ABC 075
def getInt(): return int(input())
def getIntList(): return [int(x) for x in input().split()]
def zeros(n): return [0 for i in range(n)]
def db(x): 
    global debug
    if debug: print(x)
debug = False
H,W = getIntList()
S = zeros(H+2)
S[0] = '.'*(W+2)
for i in range(H): S[i+1] = '.' + input() + '.'
S[H+1] = '.'*(W+2)
db(S)
for i in range(1,H+1):
    for j in range(1,W+1):
        if S[i][j]=='#': continue
        c = 0
        for k in range(3):
            if S[i-1][j+k-1]=='#': c += 1
        if S[i][j-1]=='#': c += 1
        if S[i][j+1]=='#': c += 1
        for k in range(3):
            if S[i+1][j+k-1]=='#': c += 1
        S[i] = S[i][:j] + str(c) + S[i][j+1:]
    db(S[i])
db(S)
for i in range(H):
    print(S[i+1][1:W+1])


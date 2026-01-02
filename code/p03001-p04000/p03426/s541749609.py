import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')

H, W, D = LI()
data = H*W
cur = int(0)
A = [LI() for _ in range(H)]
ALocat = [None]*(data+1)
a = -1
for i in A:
    a +=1
    b = 0
    for j in i:
        ALocat[j] = [a, b]
        b +=1

#print(ALocat)
ALocat[0] = [0,0]
movecost = [0]*(data+1)
for i in range(D,data+1):
    movecost[i] = movecost[i-D] + abs(ALocat[i][0]-ALocat[i-D][0])\
                                + abs(ALocat[i][1]-ALocat[i-D][1])

#print(movecost)
ans = []
Q = I()
for _ in range(Q):
    L, R = LI()
    cur = movecost[R]-movecost[L]
    ans.append(cur)
for v in ans:
    print(v)
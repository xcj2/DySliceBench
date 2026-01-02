import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

H,W,D = MI()
A = [LI() for i in range(H)]
d = {}
for i in range(H):
    for j in range(W):
        d[A[i][j]] = (i,j)

B = [0]*(H*W+1)
for i in range(1,D+1):
    a = i+D
    while a <= H*W:
        B[a] = B[a-D] + abs(d[a][0]-d[a-D][0]) + abs(d[a][1]-d[a-D][1])
        a += D

Q = I()
for i in range(Q):
    L,R = MI()
    print(B[R]-B[L])

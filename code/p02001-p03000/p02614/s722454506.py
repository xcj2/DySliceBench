import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

H,W,K = map(int,S().split())
c = [LS2() for i in range(H)]
for i in range(H):
    for j in range(W):
        if c[i][j] == '.':
            c[i][j] = 0
        else:
            c[i][j] = 1

from copy import deepcopy

ans = 0
for i in range(2**H):
    A = []
    for k in range(H):
        if (i>>k)&1:
            A.append(k)
    for j in range(2**W):
        B = []
        for l in range(W):
            if (j>>l)&1:
                B.append(l)
        d = deepcopy(c)
        for k in range(H):
            for l in range(W):
                if k in A or l in B:
                    d[k][l] = 0
        if sum(sum(d[k]) for k in range(H)) == K:
            ans += 1

print(ans)
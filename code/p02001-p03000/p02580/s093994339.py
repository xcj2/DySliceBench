import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

H,W,M = MI()
hw = [tuple(MI()) for _ in range(M)]
A = [0]*(H+1)
B = [0]*(W+1)

from collections import defaultdict
d = defaultdict(int)
for h,w in hw:
    A[h] += 1
    B[w] += 1
    d[(h,w)] = 1


ma = max(A)
mb = max(B)
ans = ma+mb
C,D = [],[]
for i in range(1,H+1):
    if A[i] == ma:
        C.append(i)
for i in range(1,W+1):
    if B[i] == mb:
        D.append(i)

if len(C)*len(D) > M:
    print(ans)
else:
    for i in C:
        for j in D:
            if d[(i,j)] == 0:
                print(ans)
                exit()
    print(ans-1)

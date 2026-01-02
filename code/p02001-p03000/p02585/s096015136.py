import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N,K = MI()
P = LI()
C = LI()

for i in range(N):
    if C[i] >= 0:
        break
else:
    print(max(C))
    exit()

from itertools import accumulate

flag = [0]*N
ans = max(C)
for i in range(N-1):
    if flag[i] != 0:
        continue
    A = [C[i]]
    flag[i] = 1
    a = i
    j = P[i]-1
    while j != i:
        A.append(C[j])
        flag[j] = 1
        j = P[j]-1
    a = len(A)
    s = 0
    if sum(A) > 0:
        if K//a > 0:
            s = sum(A)*(K//a-1)
            r = K % a + a
        else:
            s = 0
            r = K % a
    else:
        s = 0
        r = K % a + a
    A = [0] + A + A + A
    S = list(accumulate(A))
    m = 0
    for i in range(a):
        for k in range(1,r+1):
            b = S[i+k] - S[i]
            m = max(m,b)
    s += m
    ans = max(ans,s)

print(ans)

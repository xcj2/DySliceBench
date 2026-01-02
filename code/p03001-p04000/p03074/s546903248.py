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
S = LI2()

A = []
a = 1
for i in range(1,N):
    if S[i-1] == S[i]:
        a += 1
    else:
        A.append(a)
        a = 1
A.append(a)

l = len(A)
if l <= 2*K-1:
    print(N)
    exit()

if S[0] == 1:
    A = [1]+A
if S[-1] == 1:
    A = A+[1]

A = [0]+A
l = len(A)

from itertools import accumulate

A = list(accumulate(A))
ans = 0
for i in range(l//2-K+1):
    if i == 0:
        ans = max(ans,A[2*(K+i)]-A[2*i])
    elif i == l//2-K:
        ans = max(ans,A[2*(K+i)-1]-A[2*i-1])
    else:
        ans = max(ans,A[2*(K+i)]-A[2*i-1])

print(ans)

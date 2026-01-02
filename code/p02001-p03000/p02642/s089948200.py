import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
A = LI()
A = sorted(A)

if N == 1:
    print(1)
    exit()

if A[0] == 1:
    if N >= 2 and A[1] == 1:
        print(0)
        exit()
    else:
        print(1)
        exit()

B = [0]*(10**6+1)
C = [0]*(10**6+1)
for i in range(len(A)):
    if B[A[i]] == 0:
        C[A[i]] = 1
    for j in range(A[i]*2,10**6+1,A[i]):
        B[j] = 1

from collections import Counter

c = Counter(A)

for i in c.keys():
    if c[i] >= 2:
        C[i] = 0

print(sum(C))
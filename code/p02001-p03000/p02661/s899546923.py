import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
AB = [LI() for i in range(N)]
A = [AB[i][0] for i in range(N)]
B = [AB[i][1] for i in range(N)]
A = sorted(A)
B = sorted(B)

from copy import deepcopy

if N % 2 == 0:
    C = [0]*N
    D = [0]*N
    for i in range(N):
        C[i] = 2*A[i]
        D[i] = 2*B[i]
    m = N//2
    d = (D[m]+D[m-1])//2
    c = (C[m]+C[m-1])//2
    print(d-c+1)
    exit()

n = N//2
print(B[n]-A[n]+1)
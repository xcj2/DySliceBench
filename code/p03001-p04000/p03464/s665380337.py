import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


K = I()
A = LI()
A.reverse()

m,M = 2,2
for i in range(K):
    a = A[i]
    if (m+(a-1))//a > M//a:
        print(-1)
        exit()
    else:
        m = a*((m+(a-1))//a)
        M = a*(M//a)+(a-1)

print(m,M)

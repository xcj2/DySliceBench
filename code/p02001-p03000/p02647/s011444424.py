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
A = LI()

from itertools import accumulate

for _ in range(min(K,100)):
    B = [0]*(N+1)
    for i in range(N):
        a = A[i]
        B[max(i-a,0)] += 1
        B[min(N,i+a+1)] -= 1
    C = list(accumulate(B))
    A = C

print(*[A[i] for i in range(N)])

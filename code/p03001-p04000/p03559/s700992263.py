import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N = I()
A,B,C = LI(),LI(),LI()
A.sort()
C.sort()

from bisect import bisect_left,bisect_right

ans = 0
for i in range(N):
    b = B[i]
    ans += bisect_left(A,b)*(N-bisect_right(C,b))

print(ans)

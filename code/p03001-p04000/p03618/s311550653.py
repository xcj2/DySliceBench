import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


A = LS2()
N = len(A)

from collections import defaultdict

d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1


ans = 0
for key in d.keys():
    ans += d[key]*(N-d[key])

ans //= 2
ans += 1
print(ans)

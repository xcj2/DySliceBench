from math import floor,ceil,sqrt,factorial,log
from collections import Counter, deque
def S(): return input()
def I(): return int(input())
def MS(): return map(str,input().split())
def MI(): return map(int,input().split())
def LS(): return list(MS())
def LI(): return list(MI())
def LLS(): return [list(map(str, l.split() )) for l in input()]
def LLI(): return [list(map(int, l.split() )) for l in input()]
def LLSN(n: int): return [LS() for _ in range(n)]
def LLIN(n: int): return [LI() for _ in range(n)]

N = I()
X = LI()

ma = max(X)
mi = min(X)

ans = 10000000000
for i in range(mi, ma+1):
    p = i

    sum = 0
    for x in X:
        sum += pow(x-p, 2)

    if ans > sum:
        ans = sum

print(ans)
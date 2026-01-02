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

n = I()

sum = 0
for i in range(1, n+1):
    if i % 15 == 0:
        continue
    elif i % 3 == 0:
        continue
    elif i % 5 == 0:
        continue

    sum += i

print(sum)
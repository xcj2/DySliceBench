from sys import stderr
from functools import reduce
from operator import add
import bisect
def f(): return [int(i) for i in input().split()]
def yes(n): print("Yes" if n else "No")
def debug(*x, sep=" ", end="\n"):
    for item in x:
        stderr.write(str(item))
        stderr.write(sep)
    stderr.write(end)

n = int(input())
a = sorted(f())
b = sorted(f())
c = sorted(f())
debug(a,b,c,sep='\n')
ans = 0

# 各bに対して、上に乗せられるaの数を予め求めておく(後のために累積和とする)
canRideOnB = [bisect.bisect_left(a, b[0])]
for middle in b[1:]:
    top = bisect.bisect_left(a, middle)
    canRideOnB.append(top+canRideOnB[-1])
debug(canRideOnB)

# 各cに対して、上に乗せられるbの範囲を求める
canRideOnC = []
for bottom in c:
    mid = bisect.bisect_left(b, bottom)
    canRideOnC.append(mid)
debug(canRideOnC)

# 以上の計算から答えを求める
for bot in canRideOnC:
    if bot == 0:
        pass
    else:
        ans += canRideOnB[bot-1]

print(ans)
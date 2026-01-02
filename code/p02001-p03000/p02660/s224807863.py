import sys
from math import ceil, floor, gcd, sqrt
from collections import defaultdict as dd, deque, Counter as C
mod = pow(10, 9) + 7
mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var))+end)
def l(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]


n = int(data())
dp = dd(int)
i = 2
while i * i <= n:
    while n % i == 0:
        dp[i] += 1
        n //= i
    i += 1
if n > 1:
    dp[n] = 1
answer = 0
for i in dp.keys():
    temp = floor((-1 + sqrt(8 * dp[i] + 1)) / 2)
    answer += temp
out(answer)

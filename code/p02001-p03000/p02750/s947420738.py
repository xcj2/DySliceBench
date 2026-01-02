import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from functools import cmp_to_key
import itertools

N, T = map(int, readline().split())
m = map(int, read().split())
AB0 = []
AB1 = []
for a,b in zip(m,m):
    if a == 0:
        AB0.append(b)
    else:
        AB1.append((a,b))

def sort_func(ab0, ab1):
    a0, b0 = ab0
    a1, b1 = ab1
    return a1*(1+b0) - a0*(1+b1)

AB0.sort()
AB1.sort(key=lambda x: x[0] / (x[1] + 1), reverse=True)
AB0, AB1

def compute_0():
    INF = T + 1
    dp = [INF] * 40
    dp[0] = 0
    for a,b in AB1:
        for n in range(39, -1, -1):
            if dp[n] > T:
                continue
            x = (dp[n] + 1) * (a + 1) + b
            if x < dp[n+1]:
                dp[n+1] = x
    return dp

def compute_1():
    return [0] + list(itertools.accumulate(x + 1 for x in AB0))

dp0 = compute_0()
dp1 = compute_1()

R = len(dp1) - 1
answer = 0
for i,x in enumerate(dp0):
    if x > T:
        break
    while x + dp1[R] > T:
        R -= 1
    value = i + R
    if answer < value:
        answer = value

print(answer)

# coding:utf-8

import sys
from collections import defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n, p = LI()

prime_cnt = defaultdict(int)
i = 2
while i * i <= p:
    if p % i == 0:
        cnt = 0
        while p % i == 0:
            cnt += 1
            p //= i
        prime_cnt[i] += cnt
    i += 1

if p != 1:
    prime_cnt[p] += 1

ans = 1
for num, cnt in prime_cnt.items():
    while cnt >= n:
        ans *= num
        cnt -= n

print(ans)

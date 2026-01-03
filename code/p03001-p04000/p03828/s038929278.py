# coding:utf-8

import sys
from collections import defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def SI(): return input()


n = I()

prime_cnt = defaultdict(int)
for num in range(2, n + 1):
    i = 2
    while i * i <= num:
        if num % i == 0:
            cnt = 0
            while num % i == 0:
                cnt += 1
                num //= i
            prime_cnt[i] += cnt
        i += 1

    if num != 1:
        # nに素数が残っている場合処理をする
        prime_cnt[num] += 1

ans = 1
for v in prime_cnt.values():
    ans *= v + 1
    ans %= MOD

print(ans)

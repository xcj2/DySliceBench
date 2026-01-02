# coding:utf-8

import sys
from collections import defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7
dy = (0, -1, 0, 1)
dx = (1, 0, -1, 0)

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()


N, K = LI()
A = LI()

CA = [0]
for a in A:
    CA.append(CA[-1] + a)

sum_sub_array = defaultdict(int)
for l in range(N):
    for r in range(l + 1, N + 1):
        sub_sum = CA[r] - CA[l]
        sum_sub_array[sub_sum] += 1

ans = 0
for i in range(40)[::-1]:
    bit = 1 << i
    remain = 0
    new_sum_sub = {}
    for v, cnt in sum_sub_array.items():
        if v & bit > 0:
            remain += cnt
            new_sum_sub[v] = cnt

    if remain >= K:
        sum_sub_array = new_sum_sub
        ans |= bit

print(ans)

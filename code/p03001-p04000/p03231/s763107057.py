# coding:utf-8

import sys


input = sys.stdin.readline
INF = float('inf')


def inpl(): return list(map(int, input().split()))


# 整数(x, y)最大公約数を求める
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        x, y = y, x % y
        return gcd(x, y)


def lcm(x, y):
    return x * y // gcd(x, y)


N, M = inpl()
S = input()
T = input()

L = lcm(N, M)
LCM = lcm(L//N, L//M)
# print(L, LCM)

ss = L // N
cnt = 0
tmp = 0
S_li = [S[0]]
while tmp <= L:
    tmp = ss * cnt + 1
    if tmp % LCM == 1:
        S_li.append(S[cnt])
    cnt += 1

tt = L // M
cnt = 0
tmp = 0
T_li = [T[0]]
while tmp < L:
    tmp = tt * cnt + 1
    if tmp % LCM == 1:
        T_li.append(T[cnt])
    cnt += 1

# print(S_li)
# print(T_li)
if S_li == T_li:
    print(L)
else:
    print(-1)



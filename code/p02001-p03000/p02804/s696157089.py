import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def init_kaijo(MAX, MOD):
    kaijo = [0] * MAX
    kaijo[0] = 1
    for i in range(1, len(kaijo)):
        kaijo[i] = kaijo[i-1] * i % MOD
    return kaijo

MOD = 10**9+7
kaijo = init_kaijo(500000, MOD)

def inv(x, MOD):
    return pow(x, MOD-2, MOD)

def nPk(n, k, MOD):
    return kaijo[n] * inv(kaijo[n-k], MOD) % MOD

def nCk(n, k, MOD):
    return nPk(n,k, MOD) * inv(kaijo[k], MOD)

def nHk(n, k, MOD):
    return nCk(n+k-1, k, MOD)

n,k,*aaa = get_all_int()
aaa.sort()

if k == 1:
    print(0)
    exit()

ans = 0

for i,a in enumerate(aaa):
    uppers = n-(i+1)
    bottoms = i

    if bottoms >= k-1:
        ans += a * nCk(bottoms, k-1, MOD) % MOD
    if uppers >= k-1:
        ans -= a * nCk(uppers, k-1, MOD) % MOD

print(ans % MOD)

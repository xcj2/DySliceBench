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
    # log("{}C{} = {}".format(n,k,nPk(n,k, MOD) * inv(kaijo[k], MOD)))
    return nPk(n,k, MOD) * inv(kaijo[k], MOD)

h, w, a, b = get_nums_l()

ans = 0
for i in range(h-a):
    # (0,0)から(b-1, i)に到着するパターン数 * (b,i)から(W-1, H-1)に到着するパターン数
    # log(nCk(b+i-1, i, MOD), nCk(w-b+h-i-2, h-i-1, MOD))
    ans += nCk(b+i-1, i, MOD) * nCk(w-b+h-i-2, h-i-1, MOD) % MOD

print(ans % MOD)

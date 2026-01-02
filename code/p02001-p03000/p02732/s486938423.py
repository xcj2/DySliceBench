def input_int():
    return map(int, input().split())

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

from math import factorial
from operator import mul
from functools import reduce

def comb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

dicts = {}

N=one_int()

A = many_int()

# 辞書作成
for a in A:
    if a in dicts:
        dicts[a] += 1
    else:
        dicts[a] = 1

# 2個選ぶ組み合わせ計算
dicts_less ={}
sums = 0
for k, v in dicts.items():
    if v>=2:
        sums += comb(v,2)
    if v<2:
        dicts_less[k]=0
    elif v==2:
        dicts_less[k]=comb(v,2) - 0
    else:
        dicts_less[k]=comb(v,2) - comb(v-1,2)

for a in A:
    print(int(sums - dicts_less[a]))
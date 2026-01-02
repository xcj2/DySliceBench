import math
from functools import reduce
from collections import deque, Counter
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def rangeI(it, l, r):
    for i, e in enumerate(it):
        if l <= i < r:
            yield e
        elif l >= r:
            break

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

INF = 999999999999999999999999
MOD = 10**9+7

n = int(input())

if n == 1:
    print(0)
    exit()

# def factorization(n):
#     arr = []
#     temp = n
#     for i in range(2, int(n**0.5)+2):
#         if temp%i==0:
#             cnt=0
#             while temp%i==0:
#                 cnt+=1
#                 temp //= i
#             arr.append([i, cnt])

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

    if len(arr) == 0:
        arr.append((n, 1))
    return arr

fac_ = prime_factorize(n)
fac = Counter(fac_)
# log(fac)

ans = 0
for p,e in fac.items():
    # log(p,e)
    x = e
    for i in range(1, 99999999):
        if x >= i:
            x -= i
            ans += 1
        else:
            break

print(ans)

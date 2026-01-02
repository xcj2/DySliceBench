import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7


def inp():
    '''
    一つの整数
    '''
    return int(input())


def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))


def str_inp():
    '''
    文字列をリストとして読み込む
    '''
    return list(input()[:-1])


n, k = inpl()
a = inpl()
data = [[abs(i), i < 0] for i in a]
all_minus = 0
for t in data:
    if t[1]:
        all_minus += 1
if all_minus == n and k%2!=0:
    ans = 1
    data.sort()
    for i in range(k):
        ans = ans * data[i][0] % mod
    ans=ans*((-1)%mod)
    print(ans % mod)
    exit()
data.sort(reverse=True)
last_minus = 0
last_plus = 0
ans = 1
minus_amount = 0
for i in range(k):
    elem, sign = data[i][0], data[i][1]
    if elem == 0:
        print(0)
        exit()
    ans = ans * elem % mod
    minus_amount += sign
    if sign:
        last_minus = elem
    else:
        last_plus = elem
if minus_amount % 2 == 0:
    print(ans%mod)
    exit()
if n==k:
    print(-ans % mod)
    exit()
tmp_plus = 0
tmp_minus = 0
for i in range(k, n):
    elem, sign = data[i][0], data[i][1]
    if last_plus and sign and not tmp_minus:
        tmp_minus = elem
    elif last_minus and not sign and not tmp_plus:
        tmp_plus = elem
if tmp_plus == 0 and tmp_minus == 0:
    ans = 0
elif last_plus == 0:
    ans = ans * pow(last_minus, mod - 2, mod) * tmp_plus % mod
elif last_minus == 0:
    ans = ans * pow(last_plus, mod - 2, mod) * tmp_minus % mod
elif tmp_plus * last_plus > tmp_minus * last_minus:
    ans = ans * pow(last_minus, mod - 2, mod) * tmp_plus % mod
else:
    ans = ans * pow(last_plus, mod - 2, mod) * tmp_minus % mod
print(ans)

import math
from functools import reduce
from collections import deque, defaultdict
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

n,p = get_nums_l()
s = input()
X = list(map(int, list(s)))
n = len(s)

if p in (2,5):
    ans = 0
    for i,x in enumerate(X):
        if x%p == 0:
            ans += i+1
    print(ans)
else:
    ruiseki = [0] * (n+1)
    for i in (range(n-1, -1, -1)):
        ruiseki[i] = (X[i] * pow(10, (n-i-1), p) + ruiseki[i+1]) % p

    # log(ruiseki)

    ans = 0
    count = defaultdict(int)

    for x in ruiseki:
        # log(count[x])
        ans += count[x]
        count[x] += 1
    # log(count)
    print(ans)





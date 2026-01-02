import math
from functools import reduce
from collections import deque

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

n,m = get_nums_l()

lamps = []
for i in range(m):
    lamps.append(get_nums_l()[1:])

p = get_nums_l()

ans = 0
# nビット全パターン
for x in range(2**n):
    ok = True
    for ri,r in enumerate(lamps):
        count = 0
        for a in r:
            count += x&(2**(a-1)) > 0
        if count%2 != p[ri]:
            ok = False
            break
    if ok:
        ans += 1

print(ans)
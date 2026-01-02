import math
from functools import reduce
from collections import deque
from itertools import combinations
import sys
sys.setrecursionlimit(10**7)

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

def subsets(items):
    _subsets_=[]
    for i in range(len(items) + 1):
        for c in combinations(items, i):
            _subsets_.append(c)
    return _subsets_

INF = 999999999999999999999999

n,m = get_nums_l()

# ある扉の組み合わせを鍵1本で開けられる最小コストのリスト
keys = [INF] * (2 ** (n+2))

for _ in range(m):
    cost, b = get_nums_l()
    ccc = get_nums_l()

    # print(cost,b)


    for s in subsets(ccc):
        keyn = 0
        # print(s)
        for c in s:
            keyn += 2 ** c
        
        #print("keyn", keyn)
        if keys[keyn] > cost:
            keys[keyn] = cost

# print(keys)

# そもそも開けられない扉があったら無理
for i in range(1,n+1):
    if keys[2**i] == INF:
        print(-1)
        exit()

memo=[None] * (2 ** (n+2))

def solve(targets):

    lent = len(targets)
    
    # print(targets)

    if lent == 0:
        return 0

    if lent == 1:
        memo[2*list(targets)[0]] = keys[2*list(targets)[0]]
        # print(targets, keys[2**list(targets)[0]])
        return keys[2**list(targets)[0]]

    # all_s = set(targets)

    keyn=0
    for c in targets:
        keyn += 2 ** c
    
    if memo[keyn]:
        return memo[keyn]

    _min = keys[keyn]

    for s in subsets(targets):
        if len(s) in (0, lent):
            continue
        rev = targets.difference(s)
        cost = solve(s) + solve(rev)
        if _min > cost:
            _min = cost
    memo[keyn] = _min
    # print(targets, memo[keyn])
    return _min


ans = solve(set(range(1, n+1)))
# print(memo)
print(ans if ans < INF else -1)
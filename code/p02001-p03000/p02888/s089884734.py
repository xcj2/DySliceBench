import math
from functools import reduce
from collections import deque
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

# 昇順にソート済みのarrから、n以上の最小の要素を探索して返します。
# 存在しない場合は、Noneを返します。
def bin_gte(arr, n, l):
    r = len(arr) - 1
    c = (l+r)//2
    while l < r:
        c = (l+r)//2
        if arr[c] >= n:
            r = c
        else :
            l = c+1
    c = max(0, (l+r)//2)
    if arr[c] >= n:
        return (c, arr[c])
    else:
        return None

def bin_lte(arr, n, l):
    r = len(arr) - 1
    c = (l+r)//2
    while l < r:
        # c = math.ceil((l+r)/2)
        c = (l+r+1)//2
        if arr[c] <= n:
            l = c
        else :
            r = c-1
    c = max(0, (l+r)//2)
    if arr[c] <= n:
        return (c, arr[c])
    else:
        return None

n = int(input())
lll = get_nums_l()
lll.sort()

ans=0

maxs = [None] * 2002
mi = 0
prev = lll[0]
for l in lll[1:]:
    for j in range(prev, l+1):
        maxs[j] = mi
    mi += 1
    prev = l
for j in range(prev, 2002):
    maxs[j] = mi

mins = [None] * 2002
mi = 0
prev = 0
for l in lll:
    for j in range(prev+1, l+1):
        mins[j] = mi
    mi += 1
    prev = l

for ai, a in enumerate(lll):
    if ai == n-2:
        break
    for bi in range(ai+1, n-1):
        b = lll[bi]

        _min = abs(a-b) + 1
        _max = a+b - 1

        left = mins[_min]
        right = maxs[_max]
        # left = bin_gte(lll, _min, bi+1)
        # right = bin_lte(lll, _max, bi+1)

        if left is None or right is None:
            continue
        
        if right < bi:
            continue
        left = max(bi+1, left)

        # ans += right[0]-left[0]+1
        ans += right-left+1

print(ans)
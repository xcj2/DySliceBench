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
def bin_gte(arr, n):
    l = 0
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


s = input()
t = input()
n = len(s)
m = len(t)
appears = [ [] for _ in range(26)]
for i,app in enumerate(appears):
    char = chr(ord('a') + i)
    base = 0
    while True:
        f = s.find(char, base)
        if f == -1:
            break
        app.append(f)
        base = f+1

cur = 0
loop = 0
for char in t:
    appear = appears[ord(char) - ord('a')]
    if len(appear) == 0:
        print('-1')
        exit()

    nex = bin_gte(appear, cur)

    if nex == None:
        loop += 1
        cur = appear[0]+1
    else:
        cur = nex[1]+1

print(loop * n + cur)

# print(appears)
# print(appears[ord('t') - ord('a')])
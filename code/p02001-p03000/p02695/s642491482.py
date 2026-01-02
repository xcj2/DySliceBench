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

def rangeI(it, l, r):
    for i, e in enumerate(it):
        if l <= i < r:
            yield e
        elif l >= r:
            break

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

MOD = 10**9+7

n,m,q = get_nums_l()
abcd = []
for _ in range(q):
    s = input()
    abcd.append(list(map(int, s.split())))
#abcd = list(map(lambda s: list(map(int, s.split())), map(lambda s: s.strip(), sys.stdin.readlines())))

def solve(A):
    score = 0
    for query in abcd:
        if A[query[1]-1] - A[query[0]-1] == query[2]:
            score += query[3]
    return score


ans = 0

def dfs(A):
    global ans
    if len(A) == n:
        # log(A)
        ans = max(ans, solve(A))
    elif len(A) == 0:
        for a in range(1, m+1):
            dfs([a])
    else:
        for a in range(A[-1], m+1):
            dfs(A+[a])

dfs([])
print(ans)

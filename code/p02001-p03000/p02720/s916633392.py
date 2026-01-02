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

def isOk(x):
    prev = x%10
    x = x//10
    while x > 0:
        y = x%10
        if abs(y - prev) > 1:
            return False
    
    return True


k = int(input())

# if k <= 10:
#     print(k)
#     exit()

count = 0

def dfs(X,n):
    global count

    # log(X, n)

    if n == 0:
        count += 1
        if count == k:
            print("".join(map(str,X)))
            exit()
        # else:
            # log(count, "".join(map(str,X)))
        return
    
    if len(X) == 0:
        for y in range(1,10):
            dfs([y], n-1)
        return

    last = X[-1]
    for y in range(max(0,last-1), min(9,last+1)+1):
        dfs(X + [y], n-1)


dfs([], 1)
dfs([], 2)
dfs([], 3)
dfs([], 4)
dfs([], 5)
dfs([], 6)
dfs([], 7)
dfs([], 8)
dfs([], 9)
dfs([], 10)

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

def wins(c):
    if c == "r":
        return "p"
    elif c == "s":
        return "r"
    else:
        return "s"

n,k = get_nums_l()
r,s,p = get_nums_l()
point = {
    "r": r,
    "s": s,
    "p": p
}
t = input()

won = [False] * n

ans = 0
for i,c in enumerate(t):
    if i >= k and t[i-k] == c and won[i-k]:
        # 勝てる手が出せない
        # log("lose:", i, c)
        pass
    else:
        # log("win:", i, c, wins(c), point[wins(c)])
        won[i] = True
        ans += point[wins(c)]

print(ans)
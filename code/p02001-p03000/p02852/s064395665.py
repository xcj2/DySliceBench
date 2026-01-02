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

n,m = get_nums_l()
s = input()
s = s[::-1]

now = 0
steps = []
while now < n:
    for i in range(m,0,-1):
        if now+i > n:
            continue
        if s[now+i] == "0":
            now += i
            steps.append(i)
            break
    else:
        print(-1)
        exit()

print(" ".join(map(str, reversed(steps))))

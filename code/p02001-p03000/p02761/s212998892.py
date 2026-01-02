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
lines = list(map(lambda s: s.strip(), sys.stdin.readlines()))
cons = list(map(lambda s: list(map(int, s.split())), lines))

for i in range(1000):
    s = str(i)
    keta = len(s)

    if keta != n:
        continue

    for con in cons:
        if con[0] - 1 > len(s):
            break
        if s[con[0] - 1] != str(con[1]):
            break
    else:
        print(s)
        exit()
print(-1)
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

table = [False]*9

aaa1 = get_nums_l()
aaa2 = get_nums_l()
aaa3 = get_nums_l()
aaa = aaa1 + aaa2 + aaa3
n = int(input())
bbb = get_nums_n(n)

for b in bbb:
    for i,a in enumerate(aaa):
        if a == b:
            table[i] = True

check = [
    (0,3,6),
    (1,4,7),
    (2,5,8),
    (0,1,2),
    (3,4,5),
    (6,7,8),
    (0,4,8),
    (2,4,6)
]

for ch in check:
    for c in ch:
        if not table[c]:
            break
    else:
        print("Yes")
        exit()
print("No")
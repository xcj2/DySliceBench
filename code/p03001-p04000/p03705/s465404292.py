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

n,a,b = get_nums_l()

if b < a:
    print(0)
    exit()

if n == 1:
    if a==b:
        print(1)
    else:
        print(0)
    exit()

if n == 2:
    print(1)
    exit()

print( (n-2)*b - (n-2)*a + 1  )
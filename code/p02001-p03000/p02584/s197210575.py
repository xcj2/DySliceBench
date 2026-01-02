import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    x,k,d = get_all_int()
    x = abs(x)

    if k*d < x:
        print(x - k*d)
        return
    
    y = (x+d-1) // d

    if k%2 == y%2:
        print(abs(x - y*d))
    else:
        print(abs(x - y*d + d))

main()
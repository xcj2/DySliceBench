import math
from functools import reduce
from collections import deque, defaultdict
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

    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        s = input()
        d[s] += 1

    print("AC x {}".format(d["AC"]))
    print("WA x {}".format(d["WA"]))
    print("TLE x {}".format(d["TLE"]))
    print("RE x {}".format(d["RE"]))

main()
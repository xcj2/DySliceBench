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

    n,*A = get_all_int()
    A = list(A)
    A.sort(reverse=True)

    c = 1
    ans = A[0]
    i = 1
    flag = False
    while(c < n-1):
        ans += A[i]
        c += 1
        if flag:
            i+=1
            flag = False
        else:
            flag = True
    
    print(ans)


main()
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

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def gcd(m, n):
    # 入力を m, n (m ≧ n) とする。
    tmp = max(m,n)
    n = min(m,n)
    m = tmp
    # n = 0 なら、 m を出力してアルゴリズムを終了する。
    if n == 0:
        return m
    # m を n で割った余りを新たに n とし、更に 元のnを新たにm とし 2. に戻る。
    return gcd(n, m % n)

def lcm(m, n):
    return m*n//gcd(m,n)


a,b = get_nums_l()
print(lcm(a,b))
import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]


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


a,b,c,d = get_nums_l()

# cで割れる個数
t = a - (a%c-1)
cx = (b-t+1)//c + (1 if a%c==0 else 0)
# dで割れる個数
t = a - (a%d-1)
dx = (b-t+1)//d + (1 if a%d==0 else 0)
# c,dどちらも割れる個数
cd = c*d //(gcd(c,d))
t = a - (a%cd-1)
cdx = (b-t+1)//cd + (1 if a%cd==0 else 0)

all = b-a+1
print(all - cx - dx + cdx)
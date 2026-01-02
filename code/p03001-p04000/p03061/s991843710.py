import sys
# import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
# from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
# from itertools import permutations, combinations, product, accumulate, groupby
# from bisect import bisect_left, bisect_right, insort_left, insort_right
# from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0; ansli = []; tmpli = []; candili = []; mod = 10 ** 9 + 7
# dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]; ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]; ddn9 = ddn + [(0, 0)]
"""for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:"""
def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]#WideIntPoint
def ws(): return sys.stdin.readline().split()
def i(): return int(sys.stdin.readline())
def s(): return input()
def hi(n): return [i() for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]

n = i()
a = wi()

value = [] # ノードの値を持つ配列
N = 0 # 葉の数

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def update(i, x):
    # i番目の葉の値をxに変える
    i += N - 1  # i番目の葉のノード番号
    value[i] = x
    while i > 0:
        i = (i - 1) / 2  # ノード i の親ノードの番号に変える
        value[i] = min(value[i * 2 + 1], value[i * 2 + 2])  # 左右の子の min を計算しなおす


#define INF 2147483647 // 2^31-1
INF = float("INF")
def query(a, b, k, l, r) :
    # [a, b) の区間に対するクエリについて
    # ノード k （区間 [l, r) 担当）が答える
    if r <= a or b <= l:
        # 区間が被らない場合は INF を返す
        return 0
    if a <= l and r <= b:
        # ノード k の担当範囲がクエリ区間 [a, b) に完全に含まれる
        return value[k]
    else:
        # 一部だけ範囲が被る場合は左右の子に委託する
        c1 = query(a, b, 2 * k + 1, l, (l + r) // 2)  # 左の子に値を聞く
        c2 = query(a, b, 2 * k + 2, (l + r) // 2, r)  # 右の子に値を聞く
        # 左右の子の値の min を取る
        return gcd(c1, c2)



value = [] # ノードの値を持つ配列
N = 0 # 葉の数

if __name__ == '__main__':
    N = 1
    while N < n:
        N *= 2  # 葉の数を計算（n以上の最小の2冪数）

    value = [0] * (2 * N - 1)
    for i in reversed(range(2 * N - 1)):
        if N - 1 <= i < 2 * N - 1:
            if N - 1 <= i < N - 1 + n:
                value[i] = a[i - (N - 1)]
            else:
                value[i] = 0
        else:
            value[i] = gcd(value[2 * i + 1], value[2 * i + 2])

    for i in range(n):#query(,,0,0,N)
        if i == 0:
            ansli.append(query(1, n, 0, 0, N))
        elif i == n - 1:
            ansli.append(query(0, n - 1, 0, 0, N))
        else:
            ansli.append(gcd(query(0, i, 0, 0, N), query(i + 1, n, 0, 0, N)))
print(max(ansli))
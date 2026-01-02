#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    n, i = LI()
    print(n-i+1)
    return

#B
def B():
    h, w = LI()
    a = SR(h)
    dy = defaultdict(int)
    dx = defaultdict(int)
    for y in range(h):
        for x in range(w):
            if a[y][x] == "#":
                dx[x] = 1
                dy[y] = 1
    dy = list(sorted(dy.items(), key=lambda x: x[0]))
    dx = list(sorted(dx.items(), key=lambda x: x[0]))
    for y,_ in dy:
        for x,_ in dx:
            print(a[y][x], end="")
        print()
    return

#C
def C():
    n, k = LI()
    x = LI()
    ans = inf
    for i in range(n - k + 1):
        if x[i] * x[i + k - 1] > 0:
            ans = min(ans, max(abs(x[i]), abs(x[i + k - 1])))
            continue
        ans = min(ans, min(abs(x[i]), abs(x[i + k - 1])) * 2 + max(abs(x[i]), abs(x[i + k - 1])))
    print(ans)
    return

# D 
# 解説AC
# 転倒数を求める BIT(BinaryIndexedTree) は主な問題ではないので説明は省く
# 転倒数を求めるのに至るまでの考察がきもい
# 工夫したリストの転倒数を求めることで
# 各値が何個の範囲 [l,r] の中央値として存在するかを求められる
#
# 1) 工夫したリスト
# 今回必要なのはある番目において
# a[i] より小さい数が何個あって a[i] より大きい数が何個あるかという情報
# 特に a[i] より(大きい数-小さい数)の情報が欲しい
# 典型として覚えるなら、 a[k] < a[i] で 1 、 a[k] >= a[i] で-1
# として累積和とるとa[k]までの(大きい数-小さい数)が求められる
#  
# 2) 中央値の性質 
# 長さ M の整数列 b の中央値を x として
# • b 中に x 以上の要素が ⌈M/2⌉以上含まれる
# • x は，上の性質を満たす整数の中で最大である
# が中央値の性質になり、つまり2分探索で求められることがわかる
#
# 3) 問題の言いかえ
# つまり問題は
# a の連続部分列 a[l, r] (1 ≤ l ≤ r ≤ N) のうち
# x 以上の要素を ⌈r−l+1/2⌉ 個以上含むものは何通り(x通り)で、
# (n+1)*n//2 - x 通りが (n+1)*n//2 の半分より多い（要は全連続部分列において
# x以上の数がその連続列の半数以上である物の数が全連続部分文字列の半分より多い）
# ならそれは全中央値の中央値としてなりえて、この性質を満たす最大値が答えになる  
# と言い換えることができる
# 各連続部分文字列の中央値をmとしてそれにおいて x 以上の要素がその連続列の半数以上である場合
# x は中央値以下であり中央値のリストを作った際 x はその部分列の中央値としてリストに入れられた
# もの以下になるため 中央値のリストの中央値を求める際の x が中央値のリストの中央値になるかの判定
# においてその部分の中央値の値は x よりも大きいため x 以上の要素数に 1 加えることができる
# この x 以上の要素がその連続列の半数以上である場合という部分において、工夫したリストは
#  S[i] =　i_∑_j=1 {ai}となっているため a[l, r] の要素の総和は S_r − S_{l−1}となっていて
# (l, r) (0 ≤ l < r ≤ N) のうち，Sl ≤ Sr を満たすものを数えると x 以上の要素が含まれる数
# がその列の半数を超えるものの数を数えていることと同じになり、つまりこれは転倒数を求めることで求められる
#
# 注意)
# なお転倒数は負の数があると難しいのでx以下の数はどう数えてもn以上にならないためnを足すことで-1*n
# を帳消ししている
def D():
    class BinaryIndexedTree:
        # http://hos.ac/slides/20140319_bit.pdf
        def __init__(self, size):
            """
            :param int size:
            """
            self.bit = [0 for _ in range(size)]
            self.size = size

        def add(self, i, w):
            """
            i番目にwを加える
            :param int i:
            :param int w:
            :return:
            """
            x = i + 1
            while x <= self.size:
                self.bit[x - 1] += w
                x += x & -x
            return

        def sum(self, i):
            """
            [0,i]の合計
            :param int i:
            :return:
            """
            res = 0
            x = i + 1
            while x > 0:
                res += self.bit[x - 1]
                x -= x & -x
            return res

        def __len__(self):
            return self.size
            
    def count_inversions(array, Max=None):
        """
        リストから転倒数 (array[i] > array[j] (i < j) となる (i, j) の組み合わせ数) を返す
        バブルソートするときに反転する必要がある数。
        :param list of int array:
                すべての要素が 0 以上の int である配列。
        :param int max: array の最大値。指定はわかる場合
        :rtype: int
        """
        if not Max:
            Max = max(array) + n
        bit = BinaryIndexedTree(Max + 1)
        res = 0
        for i in range(len(array)):
            res += i - bit.sum(array[i])
            bit.add(array[i], 1)
        return res

    def f(i):
        x = a_sorted[i]
        c = [n] + [1 if e >= x else - 1 for e in a]
        for i in range(n):
            c[i + 1] += c[i]
        tmp = count_inversions(c, 2 * n)
        if invmax - tmp >= (invmax + 1) // 2:
            return True
        else:
            return False
        
        
        
    
    n = II()
    a = LI()
    a_sorted = sorted(a)
    invmax = (n + 1) * n // 2

    ok = 0
    ng = n
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(a_sorted[ok])
    return
#Solve
if __name__ == '__main__':
    D()

# https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0
# abcde	s=input()	s='abcde'
# abcde	s=list(input())	s=['a', 'b', 'c', 'd', 'e']
# 5(1つだけ)	a=int(input())	a=5
# 1 2	| x,y = s_inpl()   |	x=1,y=2
# 1 2 3 4 5 ... n 　	li = input().split()	li=['1','2','3',...,'n']
# 1 2 3 4 5 ... n 　	li = inpl()	li=[1,2,3,4,5,...,n]
# FFFTFTTFF 　	li = input().split('T')	li=['FFF', 'F', '', 'FF']

# INPUT
# 3
# hoge
# foo
# bar
# ANSWER
# n=int(input())
# string_list=[input() for i in range(n)]

import math
import copy
from collections import defaultdict, Counter
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
from bisect import bisect_left, bisect_right
# import numpy as np

def i_inpl(): return int(input())
def s_inpl(): return map(int,input().split())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")

N = i_inpl()
x, y, h = [], [], []
for _ in range(N):
    xi, yi, hi = s_inpl()
    x.append(xi)
    y.append(yi)
    h.append(hi)

# [0, 100]に座標があるので
MAX = 100;

ans_x, ans_y, ans_h = -1, -1, -1
for pos_y in range(MAX+1):
    for pos_x in range(MAX+1):
        # 頂上がどのくらいの高さであってほしいか
        need_h = -1
        # hが0より大きいときについて考察
        for i in range(N):
            if h[i] > 0:
                # xi, yi, hiからみて，　頂点がpos_x, pos_yのときに
                # どのくらいの高さがあってほしいか求める
                tmp_h = h[i] + abs(pos_y-y[i]) + abs(pos_x-x[i])
                if need_h == -1:
                    need_h = tmp_h
                else:
                    if need_h != tmp_h:
                        need_h = -2
                        break
        # だめだったら別のpos_x, pos_yを探す
        if need_h == -2:
            continue

        # hが1のときについて考察
        # need_hにおいて矛盾が起こらないかを調べる
        for i in range(N):
            if h[i] == 0:
                dist = abs(pos_y - y[i]) + abs(pos_x - x[i])
                if need_h > dist:
                    need_h = -2

        if need_h == -2:
            continue
        ans_x, ans_y, ans_h = pos_x, pos_y, need_h

print("{} {} {}".format(ans_x, ans_y, ans_h))


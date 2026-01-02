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
from collections import defaultdict
from collections import Counter
from collections import deque
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
from bisect import bisect_left, bisect_right
# import numpy as np

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def i_inpl(): return int(input())
def s_inpl(): return map(int,input().split())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")

############
############
############


N, K = s_inpl()
V = l_inpl()
rV = V[::-1]
ans = 0
for l in range(K+1):
    for r in range(K+1-l):
        if l + r > N:
            continue
        d = K - l - r
        get_l = []
        current_score = 0
        for i in range(l):
            current_score += V[i]
            get_l.append(V[i])
        for i in range(r):
            current_score += rV[i]
            get_l.append(rV[i])
        get_l.sort()
        for i in range(d):
            if i >= len(get_l):
                break
            if get_l[i] > 0:
                break
            current_score -= get_l[i]

        ans = max(ans, current_score)

print(ans)


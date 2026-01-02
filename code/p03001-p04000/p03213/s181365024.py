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

N = i_inpl()
# N!を素因数分解したときの指数
e = [0] * (N+1)
for i in range(2, N+1):
    cur = i
    for j in range(2, i+1):
        while cur % j == 0:
            e[j] += 1
            cur //= j

def num(m):
    cnt = 0
    for ei in e:
        if ei >= m-1:
            cnt += 1
    return cnt

print(num(75) + \
      num(25) * (num(3) - 1) + \
      num(15) * (num(5) - 1) + \
      num(5) * (num(5) - 1) * (num(3) - 2) // 2)
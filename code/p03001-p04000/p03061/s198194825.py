import math
import copy
from operator import mul
from functools import reduce
from collections import defaultdict
from collections import Counter
from collections import deque
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
# 一次元累積和
from itertools import accumulate
from bisect import bisect_left, bisect_right

import re
# import numpy as np
# from scipy.misc import perm
# from scipy.misc import comb

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
 
def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
def line_inpl(x): return [i_inpl() for _ in range(x)]

INF = int(1e18)
MOD = int(1e9)+7 # 10^9 + 7

########

n = i_inpl()

# a, bの最大公約数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

# リストnumbers最大公約数
def gcdlist(numbers):
    a = numbers[0]
    for i in range(len(numbers)):
        a = gcd(a, numbers[i])
    return a

a = [0]+l_inpl()+[0]
l = [0]*(n+2)
r = [0]*(n+2)
for i in range(1, n+1):
	l[i] = gcd(l[i-1], a[i])
for i in range(n, 0, -1):
	r[i] = gcd(r[i+1], a[i])

print(max(gcd(l[i-1], r[i+1]) for i in range(1, n+1)))

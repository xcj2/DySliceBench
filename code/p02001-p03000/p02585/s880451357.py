import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
from itertools import accumulate #list(accumulate(A))

N, K = mi()
P = li()
C = li()
ans = -float('inf')

for i in range(N):
    ind = i
    his = []
    while True:
        ind = P[ind] - 1
        his.append(C[ind])
        if ind == i:
            his = list(accumulate(his))
            #print(his)
            L = len(his)
            if K > L:
                if his[-1] > 0:
                    if not K%L:
                        ans = max(ans, his[-1] * (K//L), max(his) + his[-1] * max(K//L-1, 0))
                    else:
                        ans = max(ans, max(his[:K%L]) + his[-1] * (K//L), his[-1] * (K//L), max(his) + his[-1] * max(K//L-1, 0))
                else:
                    ans = max(ans, max(his))
            else:
                ans = max(ans, max(his[:K]))
            break

print(ans)
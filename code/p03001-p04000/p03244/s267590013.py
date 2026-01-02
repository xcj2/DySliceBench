import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

N = ii()
A = li()

d_o = defaultdict(int)
d_e = defaultdict(int)

for i in range(N):
    if i % 2:
        d_o[A[i]] += 1
    else:
        d_e[A[i]] += 1

l_d = sorted(list(d_o.items()), key=lambda x:x[1], reverse=True)
l_e = sorted(list(d_e.items()), key=lambda x:x[1], reverse=True)

if l_d[0][0] != l_e[0][0]:
    print(N - l_d[0][1] - l_e[0][1])
elif len(l_d) == len(l_e) == 1:
        print(N - max(l_d[0][1], l_e[0][1]))
elif len(l_d) == 1:
        #ans = min(N - l_d[0][1] - l_e[1][1], N - l_e[0][1])
        #print(ans)
        print(N - l_d[0][1] - l_e[1][1])
elif len(l_e) == 1:
        #ans = min(N - l_d[1][1] - l_e[0][1], N - l_d[0][1])
        #print(ans)
        print(N - l_d[1][1] - l_e[0][1])
else:
    ans = min(N-l_d[1][1]-l_e[0][1], N-l_d[0][1]-l_e[1][1])
    print(ans)
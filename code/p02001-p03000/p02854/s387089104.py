import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
from itertools import accumulate #list(accumulate(A))

N = ii()
A = li()

acc = list(accumulate(A))
#sa = acc[-1] -acc[0]

for i in range(N):
    if acc[i] - (acc[-1] - acc[i]) >= 0:
        break

if i == N-1:
    print(abs(A[i] - acc[i-1]))
elif i == 0:
    print(abs(acc[i] - (acc[-1] - acc[i])))
else:
    ans = min(abs(acc[i] - (acc[-1] - acc[i])), abs(acc[i-1] - (acc[-1] - acc[i-1])))
    print(ans)
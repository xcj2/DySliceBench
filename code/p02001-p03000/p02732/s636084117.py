import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

N = ii()
A = li()
d = defaultdict(int)

for num in A:
    d[num] += 1

sum_a = 0
for value in d.values():
    sum_a += (value)*(value-1)//2

for num in A:
    if d[num] == 1:
        print(sum_a)
    elif d[num] == 2:
        print(sum_a-1)
    else:
        print(sum_a-d[num]+1)
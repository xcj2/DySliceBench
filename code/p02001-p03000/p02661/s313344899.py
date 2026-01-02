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
#from itertools import accumulate #list(accumulate(A))

N = ii()
AB = li2(N)
A = [0]*N
B = [0]*N
for i in range(N):
    A[i] = AB[i][0]
    B[i] = AB[i][1]

if N%2:
    num_a = sorted(A)[N//2]
    num_b = sorted(B)[N//2]
    print(num_b-num_a+1)
else:
    A_ = sorted(A)
    B_ = sorted(B)
    min_a = A_[N//2-1]
    max_a = A_[N//2]
    min_b = B_[N//2-1]
    max_b = B_[N//2]
    #print(max(max_b, )-min(min_a, min_b)+1)
    print(max_b+min_b-(max_a+min_a)+1)
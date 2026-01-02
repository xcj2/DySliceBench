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
import math
    
N, K = mi()
A = li()
 
#light = [0] * (N+2)
#A = [0] + A + [0]
#print(math.log(N, 2))
'''
thre = 0
for i in range(N):
    if A[i] < i:
        thre = max(thre, i-A[i])
'''
if K > pow(N, 0.5) + 1:
        for i in range(N):
            print(N, '', end='')
        print()
        exit()
 
 
for i in range(K):
    new = [0] * (N+1)
    for j in range(N):
        new[max(j-A[j], 0)] += 1
        new[min(j+A[j]+1, N)] += -1
        #print(new)
    new = list(accumulate(new))
    A = new[:N]
 
for i in range(N):
    print(A[i], '', end='')
print()
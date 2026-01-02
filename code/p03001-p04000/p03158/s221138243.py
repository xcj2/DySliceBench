import itertools
import sys
def input(): return sys.stdin.readline()
def inpl(): return [int(i) for i in input().split()]
def f(y):
    return abs(x-A[y])
N, Q = inpl()
A = inpl()
SA = list(itertools.accumulate(A))
if N%2 :
    B = [v for i, v in enumerate(A) if not i%2]
    B = [0] + list(itertools.accumulate(B))
else:
    B = [v for i, v in enumerate(A) if i%2]
    B = [0] + list(itertools.accumulate(B))
    
for _ in range(Q):
    x = int(input())
    lo = 1
    hi = -(-N//2) + 1
    while hi - lo >1:
        mid = (lo+hi)//2
        if mid == 1:
            continue
        if max(f(N-mid-1), f(N-2*mid+1)) <= f(N-mid):
            lo = mid
        else:
            hi = mid    
    print(SA[N-1] - SA[N-lo-1] + B[-((2*lo-N)//2)])
    
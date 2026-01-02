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
 
N = ii()
A = li()
 
A_f = A[:N//2]
A_l = A[N//2:]
 
table = [0] * (N//2)
 
for i in reversed(range(N//2)):
    ind = i+1
    while(ind-1 < N):
        if ind-1 < N//2 and ind!=i+1:
            table[i] += table[ind-1]
        else:
            table[i] += A[ind-1]
        ind += i+1
    table[i] %= 2
 
table += A_l
 
ans = ''
print(sum(table))

for i in range(N):
    if table[i]%2 == 1:
        ans += str(i+1) + ' '
 
print(ans)
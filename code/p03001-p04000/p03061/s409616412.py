import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

def gcd(a, b):  
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

N = ii()
A = li()

forward = [0]*(N+1)
backward = [0]*(N+1)

forward[0] = 0
for i in range(1, N+1):
    forward[i] = gcd(A[i-1], forward[i-1])

backward[0] = 0
for i in reversed(range(1, N+1)):
    backward[N+1-i] = gcd(A[i-1], backward[N-i])

#print(forward)
#print(backward)
ans = 0
for i in range(N):
    #print(forward[i], forward[N-1-i], ans)
    ans = max(ans, gcd(forward[i], backward[N-1-i]))

print(ans)

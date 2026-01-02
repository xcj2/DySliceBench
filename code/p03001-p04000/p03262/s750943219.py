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
    #if r == 0:
        #return b
    return gcd(b, r)

N, S = mi()
X = li()
ans = abs(S - X[0])
for i in range(1, N):
    ans = gcd(ans, abs(S - X[i]))

print(ans)
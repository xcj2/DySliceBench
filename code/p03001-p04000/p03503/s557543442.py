from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

n = inp()
f = [inpl() for _ in range(n)]
p = [inpl() for _ in range(n)]
ans = -10**9

for flag in itertools.product([0,1], repeat=10):
    tmp = 0
    if not any(flag):
        continue
    for _ in range(n):
        cnt = 0
        for i,j in enumerate(flag):
            if j and f[_][i]:
                cnt += 1
        tmp += p[_][cnt]
    ans = max(ans, tmp)
print(ans)


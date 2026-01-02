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

N, M = mi()
Q = li2(M)
#Q = sorted(Q, key=lambda x:x[1])

l = [N]*N
for i in range(M):
    ind = max(0, Q[i][0]-1)
    l[ind] = min(Q[i][1]-1, l[ind])

for i in reversed(range(N-1)):
    l[i] = min(l[i], l[i+1])

cnt = 0
i = 0
#print(l)
while True:
    i = l[i]
    cnt += 1
    if l[i] == N:
        break

print(cnt)

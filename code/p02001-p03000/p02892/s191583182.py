import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
from collections import defaultdict, deque #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

N = ii()
#S = [list(map(int, list(input()))) for _ in range(N)]
rel = [[] for _ in range(N)]

for i in range(N):
    S = input()
    l = []
    for j in range(N):
        if S[j] == '1':
            l.append(j)
    rel[i] = l

flag = [0]*N
ans = 0

for i in range(N):
    flag = [0]*N
    que = deque([i])
    add = 0
    flag[i] = 1
    while que != deque([]):
        node = que.popleft()
        for nn in rel[node]:
            if not flag[nn]:
                que.append(nn)
                flag[nn] = flag[node] + 1
    ans = max(ans, max(flag))

for i in range(N):
    for t in rel[i]:
        if abs(flag[t] - flag[i]) != 1:
            print(-1)
            exit()

print(ans)
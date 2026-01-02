import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
'''
N = ii()
A = li()
right = 0
flag = [0]*(10**5+1)
ans = 0

for left in range(N):
    #flag[A[left]] = 1
    while right < N and flag[A[right]]!=1:
        flag[A[right]] = 1
        right += 1
    #print(left, right)
    ans = max(ans, right-left)
    if left == right:
        right += 1
    else:
        flag[A[left]] = 0

print(ans)
'''

from collections import deque

H, W = mi()
S = [input() for i in range(H)]

d = deque()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
ans = 0
flag = dp2(0, W, H)

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            flag = dp2(0, W, H)
            d.append([i, j, 0])
            flag[i][j] = 1
            while d!=deque():
                a = d.popleft()
                for k in range(4):
                    x, y = a[0]+dy[k], a[1]+dx[k]
                    if 0 <= x < H and 0 <= y < W:
                        if S[x][y] == '.' and flag[x][y] != 1:
                            d.append([x, y, a[2]+1])
                            flag[x][y] = 1
                            ans = max(ans, a[2]+1)

print(ans)
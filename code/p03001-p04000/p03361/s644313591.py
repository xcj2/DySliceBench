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

H, W = mi()
S = [input() for _ in range(H)]

dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            flag = 0
            for dj, di in dij:
                if -1 < i + di < H and -1 < j + dj < W:
                    if S[i + di][j + dj] == '#':
                        flag = 1
                        break
            if not flag:
                print('No')
                exit()
print('Yes')
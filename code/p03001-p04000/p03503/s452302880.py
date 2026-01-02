import sys
import numpy as np
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template


N = ii()
F = [[0] * 10 for _ in range(N)]
for i in range(N):
    F[i] = lmi()


P = [[-10**9 for _ in range(10)] for _ in range(N)]
for i in range(N):
    P[i] = lmi()

# print(F)
rieki = -10**18
for i in range(1, 2 ** 10):  # bit全探索
    tmprieki = 0
    for num in range(N):
        cnt = 0
        for j in range(10):
            if ((i >> j) & 1) and F[num][j] == 1:
                cnt += 1
        tmprieki += P[num][cnt]
    rieki = max(rieki, tmprieki)

print(rieki)

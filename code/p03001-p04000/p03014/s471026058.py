import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    H, W = LI()
    S = [list(SS()) for _ in range(H)]

    left = [[0] * W for _ in range(H)]
    for i in range(H):
        cnt = 0
        for j in range(W):
            if S[i][j] == '.':
                cnt += 1
                left[i][j] = cnt
            else:
                cnt = 0

    right = [[0] * W for _ in range(H)]
    for i in range(H):
        cnt = 0
        for j in range(W):
            if S[i][W-1-j] == '.':
                cnt += 1
                right[i][W-1-j] = cnt
            else:
                cnt = 0

    up = [[0] * W for _ in range(H)]
    for i in range(W):
        cnt = 0
        for j in range(H):
            if S[j][i] == '.':
                cnt += 1
                up[j][i] = cnt
            else:
                cnt = 0

    down = [[0] * W for _ in range(H)]
    for i in range(W):
        cnt = 0
        for j in range(H):
            if S[H-1-j][i] == '.':
                cnt += 1
                down[H-1-j][i] = cnt
            else:
                cnt = 0

    ans = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            ans[i][j] = left[i][j] + right[i][j] + up[i][j] + down[i][j] - 3

    print(max([max(i) for i in ans]))

if __name__ == '__main__':
    resolve()

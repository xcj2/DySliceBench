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

    idx_w = []
    for i in range(H):
        tmp = [-1]
        for j in range(W):
            if S[i][j] == '#':
                tmp.append(j)
        tmp.append(W)
        idx_w.append(tmp)

    idx_h = []
    for i in range(W):
        tmp = [-1]
        for j in range(H):
            if S[j][i] == '#':
                tmp.append(j)
        tmp.append(H)
        idx_h.append(tmp)

    ans = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(len(idx_w[i]) - 1):
            for k in range(idx_w[i][j] + 1, idx_w[i][j+1]):
                ans[i][k] += idx_w[i][j+1] - idx_w[i][j] - 1

    for i in range(W):
        for j in range(len(idx_h[i]) - 1):
            for k in range(idx_h[i][j] + 1, idx_h[i][j+1]):
                ans[k][i] += idx_h[i][j+1] - idx_h[i][j] - 2

    # for i in ans:
    #     print(i)

    print(max([max(i) for i in ans]))

if __name__ == '__main__':
    resolve()

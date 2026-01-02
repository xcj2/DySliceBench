import sys, math
from functools import lru_cache
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    H, W = mi()
    S = [input() for i in range(H)]

    left = [[0]*W for _ in range(H)]
    right = [[0]*W for _ in range(H)]
    top = [[0]*W for _ in range(H)]
    bottom = [[0]*W for _ in range(H)]

    # left
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                left[i][j] = 0
                continue

            if j == 0 or S[i][j-1] == '#':
                left[i][j] = 1
            else:
                left[i][j] = left[i][j-1] + 1

    # right
    for i in range(H):
        for j in range(W-1, -1, -1):
            if S[i][j] == '#':
                right[i][j] = 0
                continue

            if j == W-1 or S[i][j+1] == '#':
                right[i][j] = 1
            else:
                right[i][j] = right[i][j+1] + 1

    # top
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                top[i][j] = 0
                continue

            if i == 0 or S[i-1][j] == '#':
                top[i][j] = 1
            else:
                top[i][j] = top[i-1][j] + 1

    # bottom
    for i in range(H-1, -1, -1):
        for j in range(W):
            if S[i][j] == '#':
                bottom[i][j] = 0
                continue

            if i == H-1 or S[i+1][j] == '#':
                bottom[i][j] = 1
            else:
                bottom[i][j] = bottom[i+1][j] + 1


    m = -math.inf

    for i in range(H):
        for j in range(W):
            m = max(left[i][j]+right[i][j]+top[i][j]+bottom[i][j]-3, m)

    print(m)



if __name__ == '__main__':
    main()

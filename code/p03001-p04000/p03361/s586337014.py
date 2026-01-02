import sys
from itertools import product

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def nei(s, i, j, H, W):
    return (i+1 < H and s[i+1][j] == '#') \
        or (0 <= i-1 and s[i-1][j] == '#') \
        or (j+1 < W and s[i][j+1] == '#') \
        or (0 <= j-1 and s[i][j-1] == '#')


def main():
    H, W = mi()
    s = [input() for i in range(H)]
    for i in range(H):
        for j in range(W):
            if s[i][j] == '#' and not nei(s, i, j, H, W):
                print('No')
                return
    print('Yes')


if __name__ == '__main__':
    main()

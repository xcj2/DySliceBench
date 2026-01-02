import bisect
import math
from collections import deque

def sRaw():
    return input().rstrip("\r")


def iRaw():
    return int(input())


def ssRaw():
    return input().split()


def isRaw():
    return list(map(int, ssRaw()))


INF = 1 << 29


def main():
    H,W  =isRaw()
    ss = [sRaw() for _ in range(H)]
    memo = [[INF for _ in range(W)] for _ in range(H)]
    qu = deque()
    isF = 1 if ss[0][0] == "#" else 0
    ans = INF
    memo[0][0] = isF
    for y in range(H):
        for x in range(W):
            s = ss[y][x]
            if x!=0:
                prevM = memo[y][x-1]
                prevS = ss[y][x-1]
                if s=="#" and prevS!="#":
                    memo[y][x] = min(memo[y][x],prevM+1)
                else:
                    memo[y][x] = min(memo[y][x], prevM)
            if y!=0:
                prevM = memo[y-1][x]
                prevS = ss[y-1][x]
                if s == "#" and prevS != "#":
                    memo[y][x] = min(memo[y][x], prevM+1)
                else:
                    memo[y][x] = min(memo[y][x], prevM)
    return memo[H-1][W-1]

    
if __name__ == "__main__":
    print(main())

from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]
dy8, dx8 = [0, -1, 0, 1, 1, -1, -1, 1], [1, 0, -1, 0, 1, 1, -1, -1]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


# aとbの最大公約数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# aとbの最小公倍数
def lcm(a, b):
    g = gcd(a, b)
    return a / g * b


def solve(y, x, field, used):

    num_white, num_black = 0, 0
    que = deque()
    que.append((y, x))
    used[y][x] = True

    while len(que) != 0:
        now = que.pop()

        if field[now[0]][now[1]] == '.':
            num_white += 1
        else:
            num_black += 1

        for i in range(4):
            ny = now[0] + dy4[i]
            nx = now[1] + dx4[i]

            if inside(ny, nx, len(field), len(field[0])):
                if field[ny][nx] != field[now[0]][now[1]]:
                    if not used[ny][nx]:
                        que.append((ny, nx))
                        used[ny][nx] = True

    return num_white * num_black


def main():
    H, W = map(int, input().split())
    field = []
    for _ in range(H):
        field.append(input())

    used = [[False] * W for _ in range(H)]

    ans = 0
    for y in range(H):
        for x in range(W):
            if not used[y][x]:
                ans += solve(y, x, field, used)
    print(ans)


if __name__ == '__main__':
    main()

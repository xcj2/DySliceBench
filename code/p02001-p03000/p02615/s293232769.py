# import sys
# input = sys.stdin.readline
import itertools
import collections
from decimal import Decimal
from functools import reduce
import heapq

def main():
    n = int(input())
    a = input_list()
    aa = a + a
    aa.sort(reverse=True)
    ans = 0
    for i in range(1, n):
        ans += aa[i]
    print(ans)


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def bfs(H, W, black_cells, dist):
    d = 0
    while black_cells:
        h, w = black_cells.popleft()
        d = dist[h][w]
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            new_h = h + dy
            new_w = w + dx
            if new_h < 0 or H <= new_h or new_w < 0 or W <= new_w:
                continue
            if dist[new_h][new_w] == -1:
                dist[new_h][new_w] = d + 1
                black_cells.append((new_h, new_w))
    return d


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()

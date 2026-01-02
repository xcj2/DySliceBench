# -*- coding: utf-8 -*-
from sys import stdin


d_in = lambda: int(stdin.readline())  # N = d_in()


def get_order(n, m):
    order = 0
    while n > 0:
        n = n // m
        order += 1
    return order


def decimal2bit(n, m):
    """
    nのm進数表現
    """
    if n == 0:
        return []
    order = get_order(n, m)
    ans = []
    for i in range(order, -1, -1):
        ans.append(n // (m ** i))
        n -= m ** i * ans[-1]
    return ans


def search(n):
    ans = float('inf')
    for i in range(n // 9 + 1):
        nine = decimal2bit(9 * i, 9)
        six = decimal2bit(n - 9 * i, 6)
        ans = min(ans, sum(nine) + sum(six))
    print(ans)


if __name__ == '__main__':
    N = d_in()
    search(N)

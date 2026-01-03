import sys
from collections import deque


# sys.stdin = open('d1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def main():
    n = read_int()
    adj = [[] for u in range(n+1)]
    for i in range(n - 1):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
        adj[b].append((a, c))

    d = [0] * (n+1)
    q, k = read_int_list()

    # Q = [(k, 0, 0)]
    Q = deque([(k, 0, 0)])
    while Q:
        u, parent, dist = Q.popleft()
        for v, w in adj[u]:
            if v != parent:
                Q.append((v, u, dist+w))
        d[u] = dist

    res = [0] * q
    for i in range(q):
        x, y = map(int, input().split())
        res[i] = d[x] + d[y]
    print(*res, sep='\n')


main()

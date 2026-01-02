# coding:utf-8

import sys
from collections import deque, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7
dy, dx = (0, -1, 0, 1), (1, 0, -1, 0)

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n = II()
    G = defaultdict(list)
    for _ in range(n - 1):
        a, b = LI_()
        G[a].append(b)
        G[b].append(a)

    def DFS(start):
        stack = deque([start])
        dist = [INF] * n
        dist[start] = 0
        max_dist = 0
        farthest_v = start
        while stack:
            curr = stack.pop()

            for next in G[curr]:
                if dist[next] != INF:
                    continue
                dist[next] = dist[curr] + 1
                stack.append(next)
                if dist[next] > max_dist:
                    max_dist = dist[next]
                    farthest_v = next

        return farthest_v, max_dist

    v, d = DFS(0)
    u, d = DFS(v)

    # print(v + 1, u + 1, d)
    if d == 1: d = 0
    print('First' if d % 3 != 1 else 'Second')
    # print('First' if d % 2 else 'Second')

if __name__ == '__main__':
    main()

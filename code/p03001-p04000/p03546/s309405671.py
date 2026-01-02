import sys
from collections import defaultdict, deque, Counter
import math

# import copy
from bisect import bisect_left, bisect_right
import heapq

sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 10 ** 9 + 7
divide = lambda x: pow(x, MOD - 2, MOD)

ans = 0
def nck(n, k, kaijyo):
    return (npk(n, k, kaijyo) * divide(kaijyo[k])) % MOD


def npk(n, k, kaijyo):
    if k == 0 or k == n:
        return n % MOD
    return (kaijyo[n] * divide(kaijyo[n - k])) % MOD

def kaijyo(n):
    ret = [1]
    for i in range(1, n + 1):
        ret.append((ret[-1] * i)% MOD)
    return ret

def kaijyo_kai(n, k):
    ret = [1]
    for i in range(1, n + 1):
        ret.append((ret[-1] * (k+i))% MOD)
    return ret


def dijkstra(graph, start, n):
    h = []
    heapq.heappush(h, (0, start))
    costs = [INF for _ in range(n)]
    while h:
        cost, cur = heapq.heappop(h)
        if costs[cur] != INF:
            continue
        costs[cur] = cost
        for edge in graph[cur]:
            ecost, tgt = edge
            if costs[tgt] == INF:
                heapq.heappush(h, (cost + ecost, tgt))

    return costs

def solve():
    n, m = getList()
    graph = [[] for i in range(10)]
    magic = []
    for i in range(10):
        mg = getList()
        for j, mm in enumerate(mg):
            if i != j:
                graph[i].append((mm, j))

    for i in range(10):
        magic.append(dijkstra(graph, i, 10))
    # print(graph)
    # print(magic)


    ans = 0
    for i in range(n):
        for j in getList():
            if j != -1:
                ans += magic[j][1]

    print(ans)

def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()
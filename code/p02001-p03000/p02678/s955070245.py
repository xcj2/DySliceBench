import sys, re
from math import ceil, floor, sqrt, pi, factorial#, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left
from functools import reduce
# input = sys.stdin.readline 
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_list(N): return [s_list() for _ in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

# def bfs(si, sj, str_list, dist, h, w):
#     q = deque([[si, sj]])
#     dist[si][sj] = 0
#     max_tmp = 0
#     while len(q) != 0:
#         i, j = q.popleft()
#         for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
#             ni = i + dx
#             nj = j + dy
#             if ni < 0 or ni >= h or nj < 0 or nj >= w:
#                 continue
#             if str_list[ni][0][nj] != '.':
#                 continue
#             if dist[ni][nj] != inf:
#                 continue
#             dist[ni][nj] = dist[i][j] + 1
#             q.append([ni, nj])
#             max_tmp = max(max_tmp, dist[ni][nj])
#     return max_tmp

def create_graph(n: int, l: list) -> list:
    graph = [[] for _ in range(n)]
    for a, b in l:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    return graph

def main():
    n, m = i_map()
    num_list = i_row_list(m)

    graph = create_graph(n, num_list)

    q = deque([0])

    visited = [INF] * n
    visited[0] = 1

    ans = [0] * n

    while len(q) != 0:
        node = q.popleft()
        for leaf in graph[node]:
            if visited[leaf] != INF:
                continue
            ans[leaf] = node + 1
            visited[leaf] = 1
            q.append(leaf)

    Yes()
    for a in ans[1:]:
        print(a)

if __name__ == '__main__':
    main()

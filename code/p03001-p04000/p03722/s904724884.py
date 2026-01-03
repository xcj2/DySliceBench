import sys
input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import heapq
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**15
def search(graph, n, m):
    d = deque()
    for edge in graph[0]:
        d.append(edge)
    cnt = 0
    score = [-INF for i in range(n)]
    score[0] = 0
    loop = [0 for i in range(n)]
    while(d):
        # print(d)
        point, cur, nxt = d.popleft()
        if score[nxt] < score[cur] + point:
            score[nxt] = score[cur] + point
            for edge in graph[nxt]:
                d.append(edge)

            cnt += 1
            if cnt > n:
                loop[nxt] = 1

        if cnt >= n * 2:
            break
    # print(loop)
    if loop[n-1]:
        return "inf"

    return score[n-1]


def main():
    n,m = getlist()
    graph = [[] for i in range(n)]
    for i in range(m):
        a,b,c = getlist()
        graph[a-1].append((c, a-1, b-1))

    # print(graph)
    ans = search(graph, n, m)

    print(ans)


if __name__ == '__main__':
    main()

"""
9999
3

2916
"""
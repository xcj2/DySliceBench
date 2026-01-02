import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque, Counter
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
INF = 10**10
def bfs(graph, visited, position, root):
    visited[root] = 1
    position[root] = 0
    deq = deque([root])
    while(deq):
        cur = deq.pop()
        # print(cur)
        for nxt, dist in graph[cur]:
            if position[cur] + dist != position[nxt]:
                if position[nxt] != INF:
                    return False
                else:
                    position[nxt] = position[cur] + dist
            if not visited[nxt]:
                deq.append(nxt)
                visited[nxt] = 1

    return True

def main():
    n,m = getList()
    position = [INF for i in range(n)]
    graph = [[] for i in range(n)]
    for i in range(m):
        a,b,c = getList()
        graph[a-1].append((b-1, c))
        graph[b - 1].append((a-1, -c))

    # print(graph)
    visited = [0 for i in range(n)]
    for i in range(n):
        if not visited[i]:
            # print("===========")
            res = bfs(graph, visited, position, i)
            if res == False:
                print("No")
                return

    print("Yes")

if __name__ == "__main__":

    main()
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
    n,x = getList()

    ans = n
    mx, mn = x, n - x
    if mx < mn:
        mx,mn = mn, mx

    # print(mx, mn)

    while(True):
        if mx % mn == 0:
            ans += 2 * mn * (mx // mn) - mn
            break
        else:
            ans += mn * 2 * (mx // mn)
            mx, mn = mn, mx % mn

    print(ans)


if __name__ == "__main__":

    main()
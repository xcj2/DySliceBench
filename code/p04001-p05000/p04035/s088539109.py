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
    n, l = getList()
    nums = getList()
    flag = False
    for i in range(n - 1):
        if nums[i] + nums[i + 1] >= l:
            flag = True
            index = 1 + i
            break

    if not flag:
        print("Impossible")
        return

    else:
        print("Possible")
        for i in range(1, index):
            print(i)
        for i in range(n-1, index, -1):
            print(i)
            
        print(index)
if __name__ == "__main__":

    main()
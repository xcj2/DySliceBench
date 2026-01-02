import sys, math, collections, heapq, itertools
sys.setrecursionlimit(100000000)
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0: a, b = b, a % b
    return b

def bfs(initialnode, edge, nodeNum):
    visited = [False] * nodeNum
    dist = []
    search_que = collections.deque()
    search_que.append((0, initialnode))
    count = 0
    while count < nodeNum:
        nowDist, nowNode = search_que.popleft()
        if not visited[nowNode]:
            visited[nowNode] = True
            dist.append((nowDist, nowNode))
            count += 1
            for nextNode in edge[nowNode]:
                if not visited[nextNode]:
                    search_que.append((nowDist+1, nextNode))
    return dist[-1]


def solve():
    N = int(single_input())
    Edge = [[] for i in range(N)]
    for _ in range(N-1):
        a, b = map(int, line_input())
        Edge[a-1].append(b-1)
        Edge[b-1].append(a-1)

    most_far_from_zero = bfs(0, Edge, N)
    tree_d, node_on_otherside = bfs(most_far_from_zero[1], Edge, N)

    if tree_d % 3 == 1: print("Second")
    else: print("First")
    return 0
  
if __name__ == "__main__":
    solve()
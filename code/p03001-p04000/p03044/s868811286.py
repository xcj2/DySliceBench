import sys, math, collections, heapq, itertools
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()

def solve():
    N = int(single_input())
    edge = [[] for i in range(N)]
    for i in range(N-1):
        u, v, w = map(int, line_input())
        edge[u-1].append((v-1, w))
        edge[v-1].append((u-1, w))
    
    col = [-1] * N
    que = collections.deque()
    que.append((0, 0))
    while que:
        nownode, nowdist = que.popleft()
        if col[nownode] == -1:
            col[nownode] = nowdist
            for nextnode, weight in edge[nownode]:
                if col[nextnode] == -1:
                    que.append((nextnode, nowdist + weight))
    for i in range(N):
        print(col[i] % 2)

    return 0
  
if __name__ == "__main__":
    solve()
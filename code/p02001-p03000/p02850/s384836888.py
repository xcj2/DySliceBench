import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
class Edge:
    def __init__(self, to, id):
        self.to = to
        self.id = id
N = int(input())
graph = {}
ans = [0] * (N-1)
def dfs(v, c=-1, p=-1):
    global graph, ans
    k = 1
    for edge in graph[v]:
        nv = edge.to
        if nv == p:continue
        if k == c:k += 1
        ans[edge.id] = k
        dfs(nv, k, v)
        k += 1
def main():
    global N, graph, ans
    for i in range(N):
        graph[i] = set()
    for i in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].add(Edge(b-1, i))
        graph[b-1].add(Edge(a-1, i))
    color_count = 0
    for i in range(N):
        color_count = max(color_count, len(graph[i]))
    dfs(0, 0, -1)
    print(color_count)
    for x in ans:
        print(x)
if __name__ == "__main__":
    main()
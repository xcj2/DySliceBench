def main():

    # Input N, Q
    N, Q = [int(c) for c in input().split()]

    # Input edges
    edges = [[] for i in range(N)]
    for i in range(N-1):
        u, v = [int(c)-1 for c in input().split()]
        edges[u].append(v)
        edges[v].append(u)

    # Form tree
    parent = [None for i in range(N)]
    childs = [[] for i in range(N)]
    def dfs(root):
        parent[root] = -1
        stack = [root]
        while stack:
            now = stack.pop()
            for nex in edges[now]:
                if parent[nex] is None:
                    parent[nex] = now
                    childs[now].append(nex)
                    stack.append(nex)
    dfs(0)

    # Queries
    incremented = [0 for i in range(N)]
    for i in range(Q):
        v, add = [int(c) for c in input().split()]
        v -= 1
        incremented[v] += add

    # Lower propagate
    total = [0 for i in range(N)]
    def propagate(root):
        stack = [root]
        while stack:
            now = stack.pop()
            total[now] += incremented[now]
            for child in childs[now]:
                total[child] += total[now]
                stack.append(child)
    propagate(0)

    # Print
    print(" ".join(str(num) for num in total))

main()

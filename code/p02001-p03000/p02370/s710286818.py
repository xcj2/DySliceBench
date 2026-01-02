
def topological_sort(nodes, edges) -> []:
    visited = set()
    result = []

    def dfs(v):
        if v not in visited:
            visited.add(v)
            for u in edges[v]:
                dfs(u)
            result.append(v)

    for s in nodes:
        dfs(s)

    return result

def aoj_system_test():
    """
    The problem of aoj for topological sort use special judge.
    So, I can't verify using online-judge-tools. (T T)
    """
    V, E = map(int, input().split())
    nodes = []
    edges = []
    for i in range(V):
        nodes.append(i)
        edges.append([])
    for _ in range(E):
        a, b = map(int, input().split())
        edges[b].append(a)
    ret = topological_sort(nodes, edges)
    for v in ret:
        print(v)

if __name__ == '__main__':
    aoj_system_test()

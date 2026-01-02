def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        v = stack.pop()
        if v not in visited:
            stack.extend(graph[v])
            visited.add(v)
            yield v


def read_graph(nodes, edges):
    graph = [[] for _ in range(nodes)]
    for _ in range(edges):
        a, b = (int(x) - 1 for x in input().split())
        graph[a].append(b)
        graph[b].append(a)

    return graph


def count_candidates(n, counts, groups, block, friend):
    for i in range(n):
        count = counts[groups[i]]
        for v in block[i]:
            if groups[i] == groups[v]:
                count -= 1

        count -= len(friend[i])
        count -= 1
        yield count


def main():
    n, m, k = map(int, input().split())
    friend = read_graph(n, m)
    block = read_graph(n, k)

    groups = [-1 for _ in range(n)]
    counts = []
    i = 0
    group_id = 0
    while i < n:
        if groups[i] != -1:
            i += 1
            continue

        for j, v in enumerate(dfs(friend, i)):
            groups[v] = group_id

        counts.append(j + 1)
        group_id += 1

    print(" ".join(str(i) for i in count_candidates(n, counts, groups, block, friend)))


if __name__ == "__main__":
    main()

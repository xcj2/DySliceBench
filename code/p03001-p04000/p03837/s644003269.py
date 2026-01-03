def warshall_floyd(graph):
    n_nodes = len(graph)

    froms = []
    for i in range(len(graph)):
        froms.append([])
        for j in range(len(graph[i])):
            if i == j:
                froms[i].append(0)
            elif graph[i][j] < float("inf"):
                froms[i].append(i)
            else:
                froms[i].append(None)

    for k in range(n_nodes):
        for i in range(n_nodes):
            for j in range(n_nodes):
                adj_cost = graph[i][k] + graph[k][j]
                if adj_cost < graph[i][j]:
                    graph[i][j] = adj_cost
                    froms[i][j] = froms[k][j]
    
    has_negative_loop = False
    for i in range(n_nodes):
        if graph[i][i] < 0:
            has_negative_loop = True
            break

    return graph, froms, has_negative_loop

def restore_path(froms, start, goal):
    path = []
    cur = goal
    path.append(goal)
    while cur != start:
        prev = froms[start][cur]
        path.append(prev)
        cur = prev
    path.reverse()
    return path

def resolve():
    N, M = list(map(int, input().split()))
    graph = [[float("inf") for _ in range(N)] for __ in range(N)]
    import copy
    exists = [[False for _ in range(N)] for __ in range(N)]
    for i in range(M):
        a, b, c = list(map(int, input().split()))
        graph[a-1][b-1] = c
        graph[b-1][a-1] = c
        exists[a-1][b-1] = True
        exists[b-1][a-1] = True
    costs, froms, _ = warshall_floyd(graph)
    # print(froms)

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            path = restore_path(froms, i, j)
            # print("{} to {}".format(i, j))
            # print(path)
            src = 0
            for dst in range(1, len(path)):
                exists[path[src]][path[dst]] = False
                exists[path[dst]][path[src]] = False
                src = dst
    
    print(sum(sum(exists, []))//2)



if __name__ == '__main__':
    resolve()
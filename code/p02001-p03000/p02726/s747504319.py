# from sys import stdin

# # 解説のコード
# def get_result(data):
#     N, X, Y = data
#     dist_cnt = [0 for i in range(N)]
#     for i in range(1, N+1):
#         for j in range(i+1, N+1):
#             min_dist = min([j-i, abs(X-i) + 1 + abs(Y-j), abs(Y-i) + 1 + abs(X-j)])
#             dist_cnt[min_dist] += 1
#     for i in range(1, N):
#         print(dist_cnt[i])


# if __name__ == '__main__':
#     data = list(map(int, stdin.readline().rstrip('\n').split(' ')))
#     get_result(data)

from sys import stdin
from collections import deque


# 重みなしグラフの隣接リスト
# 0-indexed nodes
def get_adj_list(num_nodes, data, undirected=True):
    graph = [[] for _ in range(num_nodes)]
    for val in data:
        x, y = val
        graph[x-1] = graph[x-1] + [y-1]
        if undirected:
            graph[y-1] = graph[y-1] + [x-1]
    return graph


# BFS
def breadth_first_search(adj_list, start_node):
    N = len(adj_list)
    order = [-1] * N # a bfs ordering of each vertex
    parent = [-1] * N # parent of each vertex in the bfs search tree
    depth = [-1] * N # the depth of each vertex
    q = deque([(start_node, -1, 0)]) # (vertex, parent, depth)
    num = 0 # current ordering
    while q:
        v, p, d = q.popleft()
        if order[v] < 0: # visited v for the first time
            order[v] = num
            parent[v] = p
            depth[v] = d
            num += 1
            for u in adj_list[v]:
                if order[u] >= 0: continue
                q.append((u, v, d+1))
    return order, parent, depth

# BFS pypyでAC
def get_result(data):
    N, X, Y = data
    _data = [[i, i+1] for i in range(1, N)]
    _data += [[X, Y]]
    adj_list = get_adj_list(N, _data)
    dist_cnt = [0 for i in range(N)]
    for i in range(N):
        _, _, depth = breadth_first_search(adj_list, i)
        for j in range(i, N):
            dist_cnt[depth[j]] += 1
    for i in range(1, N):
        print(dist_cnt[i])


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip('\n').split(' ')))
    get_result(data)

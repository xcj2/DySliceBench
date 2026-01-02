import collections
# from typing import List, Tuple

n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b-1)
    graph[b - 1].append(a-1)


def is_connected_graph(graph):  # (graph: List[List[int]]) -> bool:
    """グラフが連結か判定する。

    Args:
        - graph: 隣接リスト形式
    """
    graph_size = len(graph)
    if graph_size == 0:
        return True
    connected = [False] * graph_size
    dq = collections.deque([0])  # 暗黙的に0をrootとして探索する。
    connected[0] = True
    while dq:
        node = dq.popleft()
        for adjacent_node in graph[node]:
            if connected[adjacent_node]:
                continue
            connected[adjacent_node] = True
            dq.append(adjacent_node)
    return all(connected)


def enumerate_bridge(graph):  # (graph: List[List[int]]) -> List[Tuple[int, int]]:
    """グラフの橋を列挙する。

    Args:
        - graph: 隣接リスト形式

    Returns:
        - 橋の配列。ソートしていない。
    """
    graph_size = len(graph)
    if graph_size == 0:
        return True

    bridges = []

    visited = [False] * graph_size
    order = [-1] * graph_size
    lowlink = [float('inf')] * graph_size
    k = 0

    def __dfs(node, pre_node):
        nonlocal k
        visited[node] = True

        order[node] = k
        lowlink[node] = order[node]
        k += 1

        ct = 0

        for next_node in graph[node]:
            if not visited[next_node]:
                ct += 1
                __dfs(next_node, node)
                lowlink[node] = min(lowlink[node], lowlink[next_node])
                if order[node] < lowlink[next_node]:
                    bridges.append(
                        (min(node, next_node), max(node, next_node)))
            elif next_node != pre_node:
                lowlink[node] = min(lowlink[node], order[next_node])

    for i in range(graph_size):
        if not visited[i]:
            __dfs(i, -1)
    return bridges


print(len(enumerate_bridge(graph)))

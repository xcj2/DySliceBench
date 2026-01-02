import copy
import queue


def read():
    N = int(input().strip())
    edge = [-1 for _ in range(N+1)]
    for i in range(1, N+1):
        edge[i] = list()
    for _ in range(N-1):
        a, b = list(map(int, input().strip().split()))
        edge[a].append(b)
        edge[b].append(a)
    C = list(map(int, input().strip().split()))
    return N, edge, C


def center_of_tree(N, edge):
    # 端点を削除していく。最後に残ったものが中心。
    n = N
    previous_parent = -1
    e = copy.deepcopy(edge)
    while n > 1:
        for child in range(1, N+1):
            if len(e[child]) == 1:
                parent = e[child][0]
                e[parent].remove(child)
                e[child].remove(parent)
                n -= 1
                previous_parent = parent
    return previous_parent


def write_node_weights(N, parent, edge, C):
    C = list(sorted(C))
    node_weight = [-1 for _ in range(N+1)]
    node_weight[parent] = C.pop()
    q = queue.Queue()
    q.put(parent)
    while len(C) > 0:
        parent = q.get()
        for child in edge[parent]:
            if node_weight[child] == -1:
                node_weight[child] = C.pop()
                q.put(child)
    return node_weight


def sum_of_edge_weights(N, node_weight, edge):
    sum_of_edge_weights = 0
    for a in range(1, N+1):
        for b in edge[a]:
            if a < b:
                sum_of_edge_weights += min(node_weight[a], node_weight[b])
    return sum_of_edge_weights


def solve(N, edge, C):
    center = center_of_tree(N, edge)
    node_weight = write_node_weights(N, center, edge, C)
    edge_weights = sum_of_edge_weights(N, node_weight, edge)
    return edge_weights, node_weight[1:]


if __name__ == '__main__':
    inputs = read()
    edge_weights, node_weight = solve(*inputs)
    print(edge_weights)
    print(' '.join(map(str, node_weight)))

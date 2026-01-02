from collections import deque, defaultdict


def read_input():
    n = int(input())
    edges = []

    for i in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    return n, edges


# グラフのノード間の距離の偶奇に応じてノードをグループ分けする
def search_graph(nodes, edges):
    edge_table = {n:[] for n in nodes}

    for e in edges:
        edge_table[e[0]].append((e[1], e[2]))
        edge_table[e[1]].append((e[0], e[2]))

    # 探索開始
    q = deque()
    # (node, これまでの距離), 初期ノードは(1, 0)とする
    q.appendleft((nodes[0], 0))

    even = []
    odd = []
    searched = defaultdict(int)

    while len(q) > 0:
        cnode, cdist = q.pop()
        searched[cnode] = 1

        if cdist % 2:
            odd.append(cnode)
        else:
            even.append(cnode)

        next_nodes = edge_table[cnode]
        for nn in next_nodes:
            if searched[nn[0]] == 0:
                q.appendleft((nn[0], cdist + nn[1]))

    return set(even), set(odd)


def submit():
    n, edges = read_input()
    nodes = [i for i in range(1, n + 1)]
    even, odd = search_graph(nodes, edges)

    for n in nodes:
        if n in even:
            print(0)
        else:
            print(1)



if __name__ == '__main__':
    submit()

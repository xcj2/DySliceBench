

def read_input():
    n, m = map(int, input().split())

    edges = []
    nodes = list(range(1, n + 1))

    for i in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))


    edges_dic = {}
    for i in range(n):
        edges_dic[i + 1] = []

    for edge in edges:
        edges_dic[edge[0]].append(edge[1])
        edges_dic[edge[1]].append(edge[0])

    return n, m, nodes, edges_dic


# throughを通過済みとして、curr_nodeから残りのnodesにたどり着けるかチェックする
def check_path(curr_node, rest_nodes, edges_dic, through):
    # 終点
    if not rest_nodes:
        return 1

    # rest_nodesのうち、curr_nodeからいけるnodeがあるか確認する
    next_nodes = edges_dic[curr_node]
    targets = []
    for n in next_nodes:
        if n in rest_nodes:
            targets.append(n)

    # restがあるにもかかわらず、次にいけるnodeがない
    if not targets:
        return 0

    # いけるnodeがあれば、その先をチェックする
    count = 0
    for t in targets:
        new_rest = [r for r in rest_nodes if r != t]
        new_through = through + [curr_node]
        count += check_path(t, new_rest, edges_dic, new_through)

    return count


def submit():
    n, m, nodes, edges_dic = read_input()

    rest_nodes = [r for r in nodes if r != 1]
    paths = check_path(1, rest_nodes, edges_dic, [])
    print(paths)


if __name__ == '__main__':
    submit()

def binarytrees():
    def set_depth(node_id):
        if tree[node_id]['parent'] == -1:
            return 0
        else:
            return set_depth(tree[node_id]['parent']) + 1

    def set_height(node_id):
        if not tree[node_id]['degree']:
            return 0
        else:
            return max(set_height(tree[node_id]['children'][0]),
                set_height(tree[node_id]['children'][1])) + 1

    n = int(input())

    tree = [{'parent': -1, 'sibling': -1, 'degree': 0, 'depth': 0, 'height': 0,
             'node_type': 'leaf', 'children': []} for i in range(n)]

    for i in range(n):
        line = list(map(int, input().split()))
        node_id = line[0]
        child1 = line[1]
        child2 = line[2]

        for child in [child1, child2]:
            if child != -1:
                tree[node_id]['children'] = line[1:]
                tree[child]['parent'] = node_id
                tree[node_id]['degree'] += 1

        if (child1 != -1) and (child2 != -1):
            tree[child1]['sibling'] = child2
            tree[child2]['sibling'] = child1

        if tree[node_id]['degree']:
            tree[node_id]['node_type'] = 'internal node'

    for node_id in range(n):
        tree[node_id]['depth'] = set_depth(node_id)
        tree[node_id]['height'] = set_height(node_id)

        if tree[node_id]['parent'] == -1:
            tree[node_id]['node_type'] = 'root'

    for node_id in range(n):
        parent = tree[node_id]['parent']
        sibling = tree[node_id]['sibling']
        degree = tree[node_id]['degree']
        depth = tree[node_id]['depth']
        height = tree[node_id]['height']
        node_type = tree[node_id]['node_type']

        print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'
            .format(node_id, parent, sibling, degree, depth, height, node_type))

if __name__ == '__main__':
    binarytrees()
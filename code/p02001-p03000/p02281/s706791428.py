class Node(object):
    """ ????????¨????????? """
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right
        self.height = None

    def get_type(self):
        if self.parent == -1:
            return 'root'
        elif self.left == -1 and self.right == -1:
            return 'leaf'
        else:
            return 'internal node'

    def get_depth(self):
        if self.parent == -1:
            return 0
        else:
            depth = 1
            t = Nodes[self.parent]
            while t.parent != -1:
                t = Nodes[t.parent]
                depth += 1
            return depth

    def get_height(self):
        if self.height:
            return self.height
        h_left = 0
        h_right = 0
        if self.left != -1:
            h_left = Nodes[self.left].get_height() + 1
        if self.right != -1:
            h_right = Nodes[self.right].get_height() + 1
        self.height = max(h_left, h_right)
        return self.height

    def get_degree(self):
        degree = 0
        if self.left != -1:
            degree += 1
        if self.right != -1:
            degree += 1
        return degree

    def get_sibling(self):
        if self.parent == -1:
            return -1
        p = Nodes[self.parent]
        if Nodes[p.left] != self and Nodes[p.left] != -1:
            return p.left
        if Nodes[p.right] != self and Nodes[p.right] != -1:
            return p.right


def process_node_data(data):
    """ ??\???????????????????????????????????¨?????????????????? """
    num_of_elem = len(data)
    if num_of_elem != 3:
        raise ValueError
    else:
        my_id, left, right = data
        Nodes[my_id].left = left
        if left != -1:
            Nodes[left].parent = my_id
        Nodes[my_id].right = right
        if right != -1:
            Nodes[right].parent = my_id


def walk_preorder(Nodes, current_id):
    results = []
    results.append(current_id)
    if Nodes[current_id].left != -1:
        results.append(walk_preorder(Nodes, Nodes[current_id].left))
    if Nodes[current_id].right != -1:
        results.append(walk_preorder(Nodes, Nodes[current_id].right))
    return results


def walk_inorder(Nodes, current_id):
    results = []
    if Nodes[current_id].left != -1:
        results.append(walk_inorder(Nodes, Nodes[current_id].left))
    results.append(current_id)
    if Nodes[current_id].right != -1:
        results.append(walk_inorder(Nodes, Nodes[current_id].right))
    return results


def walk_postorder(Nodes, current_id):
    results = []
    if Nodes[current_id].left != -1:
        results.append(walk_postorder(Nodes, Nodes[current_id].left))
    if Nodes[current_id].right != -1:
        results.append(walk_postorder(Nodes, Nodes[current_id].right))
    results.append(current_id)
    return results


def flatten(l):
    """ http://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists-in-python """
    import collections
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


if __name__ == '__main__':
    MAX_NODES = 25
    # ????´???? [Node(None, None, None)] * MAX_NODES ????????¨????????????????????????????????§??¨???
    Nodes = [Node(-1, None, None) for _ in range(MAX_NODES)]

    # ??????????????\???
    num_of_nodes = int(input())
    node_data = []
    for i in range(num_of_nodes):
        t = [int(x) for x in input().split(' ')]
        node_data.append(t)

    # ???????????????
    # ??¨???????????????
    for d in node_data:
        process_node_data(d)

    # ???????????????
    # ??¨???root????¢????
    root_id = -1
    for i, n in enumerate(Nodes):
        if n.parent == -1:
            root_id = i
            break

    print('Preorder')
    result = walk_preorder(Nodes, root_id)
    print(' {0}'.format(' '.join(map(str, flatten(result)))))

    print('Inorder')
    result = walk_inorder(Nodes, root_id)
    print(' {0}'.format(' '.join(map(str, flatten(result)))))

    print('Postorder')
    result = walk_postorder(Nodes, root_id)
    print(' {0}'.format(' '.join(map(str, flatten(result)))))
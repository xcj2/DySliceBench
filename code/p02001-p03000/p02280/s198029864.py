class Node(object):
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

    def get_sigling(self):
        if self.parent == -1:
            return -1
        p = Nodes[self.parent]
        if Nodes[p.left] != self and  Nodes[p.left] != -1:
            return p.left
        if Nodes[p.right] != self and  Nodes[p.right] != -1:
            return p.right


def process_node_data(data):
    global Nodes
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



MAX_NODES = 25
Nodes = [Node(-1, None, None) for _ in range(MAX_NODES)]  # ????´???? [Node(None, None, None)] * MAX_NODES ????????¨????????????????????????????????§??¨???

if __name__ == '__main__':
    # ??????????????\???
    num_of_nodes = int(input())
    node_data = []
    for i in range(num_of_nodes):
        t = [int(x) for x in input().split(' ')]
        node_data.append(t)

    # ???????????????
    for d in node_data:
        process_node_data(d)

    # ???????????????
    for i in range(num_of_nodes):
        p = Nodes[i]
        print('node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}'.format(
            i, p.parent, p.get_sigling(), p.get_degree(), p.get_depth(), p.get_height(), p.get_type()
        ))
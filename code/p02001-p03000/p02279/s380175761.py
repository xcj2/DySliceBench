import operator

class Tree:
    """??¨????????????"""

    def __init__(self, node_num):
        self.node_num = node_num
        self.node_list = list()
        self.root_node = -1

    def set_tree(self):
        for _ in range(self.node_num):
            input_str = [int(i) for i in input().split()]
            node_tmp = Node(input_str[0], input_str[1], input_str[2:])
            self.node_list.append(node_tmp)
        self.node_list.sort(key=operator.attrgetter('id'))

    def set_node_element(self):
        for tn in self.node_list:
            if tn.children is not None:
                for child in tn.children:
                    self.node_list[child].parent = tn.id
                    if self.node_list[child].degree == 0:
                        self.node_list[child].type = 'leaf'
                    else:
                        self.node_list[child].type = 'internal node'
        self.set_root()
        self.set_depth(self.node_list[self.root_node])

    def set_depth(self, node, dep = -1):
        node.depth = dep + 1
        for child in node.children:
            self.set_depth(self.node_list[child], node.depth)

    def set_root(self):
        for tn in self.node_list:
            if tn.type == 'root':
                self.root_node = tn.id
                break

    def show_tree(self):
        for tn in self.node_list:
            print('node {0}: parent = {1}, depth = {2}, {3}, {4}'.format(tn.id, tn.parent, tn.depth, tn.type, tn.children))


class Node:
    """?????????????????????"""

    def __init__(self, id, degree, children):
        self.id = id
        self.degree = degree
        self.children = children
        self.parent = -1
        self.depth = 0
        self.type = 'root'

if __name__ == '__main__':
    n = int(input())
    tree = Tree(n)
    tree.set_tree()
    tree.set_node_element()
    tree.show_tree()
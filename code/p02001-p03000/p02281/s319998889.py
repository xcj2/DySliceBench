class BinaryTree:
    class Node:
        def __init__(self, num, left_child, right_child):
            self.id = num
            self.left_child = left_child
            self.right_child = right_child
            
    def __init__(self, n):
        self.nodes = [None] * n
        self.root_id = int(n * (n - 1) / 2)

    def add_node(self, i_s):
        num, left_child, right_child = map(int, i_s.split())
        self.nodes[num] = BinaryTree.Node(num, left_child, right_child)
        if left_child != -1:
            self.root_id -= left_child
        if right_child != -1:
            self.root_id -= right_child

    def preorder_walk(self):
        print('Preorder')
        def _pre_walk(node_id):
            if node_id != -1:
                print(' {0}'.format(node_id), end = '')
                _pre_walk(self.nodes[node_id].left_child)
                _pre_walk(self.nodes[node_id].right_child)
        _pre_walk(self.root_id)
        print('')

    def inorder_walk(self):
        print('Inorder')
        root_node = self.nodes[self.root_id]
        def _in_walk(node_id):
            if node_id != -1:
                _in_walk(self.nodes[node_id].left_child)
                print(' {0}'.format(node_id), end = '')
                _in_walk(self.nodes[node_id].right_child)
        _in_walk(self.root_id)
        print('')

    def postorder_walk(self):
        print('Postorder')
        root_node = self.nodes[self.root_id]
        def _post_walk(node_id):
            if node_id != -1:
                _post_walk(self.nodes[node_id].left_child)
                _post_walk(self.nodes[node_id].right_child)
                print(' {0}'.format(node_id), end = '')
        _post_walk(self.root_id)
        print('')


n = int(input())

BT = BinaryTree(n)

for i in range(n):
    BT.add_node(input())

BT.preorder_walk()
BT.inorder_walk()
BT.postorder_walk()
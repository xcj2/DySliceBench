class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
        self.inorder = []
        self.preorder = []

    def insert(self, node):

        p = None
        x = self.root        
        while x is not None:
            p = x
            # print(node.key, x.key)
            if node.key <= x.key:
                x = x.left
            else:
                x = x.right

        # insertするnodeの親を設定
        node.parent = p

        if p is None:
            self.root = node
        else:
            # insertするnodeを親のleftかrightに設定
            if node.key <= p.key:
                # print('leftに設定')
                p.left = node
            else:
                # print('rightに設定')
                p.right = node


    def print_inorder(self):
        self.inorder = []
        self.inorder_traverse(self.root)
        print(' ' + ' '.join(map(str, self.inorder)))

    def print_preorder(self):
        self.preorder = []
        self.preorder_traverse(self.root)
        print(' ' + ' '.join(map(str, self.preorder)))

    def inorder_traverse(self, node):
        if node is None:
            return
        self.inorder_traverse(node.left)
        self.inorder.append(node.key)
        self.inorder_traverse(node.right)

    def preorder_traverse(self, node):
        if node is None:
            return
        self.preorder.append(node.key)
        self.preorder_traverse(node.left)
        self.preorder_traverse(node.right)

tree = Tree()
m = int(input())
for i in range(m):
    line = input().split()
    if line[0] == 'print':
        tree.print_inorder()
        tree.print_preorder()
    elif line[0] == 'insert':
        key = int(line[1])
        tree.insert(Node(key))
    # elif line[0] == 'find':
    #     key = int(line[1])
    #     if tree.find(key):
    #         print('yes')
    #     else:
    #         print('no')
    # elif line[0] == 'delete':
    #     print("current tree----")
    #     print(tree.root.key)
    #     print(tree.root.left.key)
    #     print(tree.root.left.right.key)
    #     print("current tree----")
    #     key = int(line[1])
    #     node = tree.find(key)
    #     tree.delete(node)

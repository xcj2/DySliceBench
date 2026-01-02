class Tree:
    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n)]
        self.root = -1

    def set_tree(self):
        for _ in range(self.n):
            i_str = [int(i) for i in input().split()]
            for i in range(2):
                if i_str[i+1] != -1:
                    if i == 0:
                        self.nodes[i_str[0]].left = i_str[1]
                    else:
                        self.nodes[i_str[0]].right = i_str[2]
                    self.nodes[i_str[i+1]].parent = i_str[0]

    def set_root(self):
        for tn in self.nodes:
            if tn.parent == -1:
                self.root = tn.id
                return tn.id

    def preorder(self, node):
        print(' ' + str(self.nodes[node].id), end='')
        if self.nodes[node].left != -1:
            self.preorder(self.nodes[node].left)
        if self.nodes[node].right != -1:
            self.preorder(self.nodes[node].right)

    def inorder(self, node):
        if self.nodes[node].left != -1:
            self.inorder(self.nodes[node].left)
        print(' ' + str(self.nodes[node].id), end='')
        if self.nodes[node].right != -1:
            self.inorder(self.nodes[node].right)

    def postorder(self, node):
        if self.nodes[node].left != -1:
            self.postorder(self.nodes[node].left)
        if self.nodes[node].right != -1:
            self.postorder(self.nodes[node].right)
        print(' ' + str(self.nodes[node].id), end='')

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = -1
        self.left = -1
        self.right = -1

if __name__ == '__main__':
    tree = Tree(int(input()))
    tree.set_tree()
    root = tree.set_root()
    print("Preorder")
    tree.preorder(root)
    print()
    print('Inorder')
    tree.inorder(root)
    print()
    print('Postorder')
    tree.postorder(root)
    print()
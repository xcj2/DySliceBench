class Node():
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            parentnode = curnode = self.root
            while curnode != None:
                parentnode = curnode
                if curnode.value > value:
                    curnode = curnode.left
                else:
                    curnode = curnode.right
            if value > parentnode.value:
                parentnode.right = Node(value)
            else:
                parentnode.left = Node(value)

    def preorder(self, root):
        if root == None:
            pass
        else:
            print(' %d' % root.value, end='')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root == None:
            pass
        else:
            self.inorder(root.left)
            print(' %d' % root.value, end='')
            self.inorder(root.right)

if __name__ == '__main__':
    n = int(input())
    binarytree = BinaryTree()
    for _ in range(n):
        common = input()
        if common[0] == 'i':
            binarytree.insert(int(common[7:]))
        else:
            binarytree.inorder(binarytree.root)
            print()
            binarytree.preorder(binarytree.root)
            print()

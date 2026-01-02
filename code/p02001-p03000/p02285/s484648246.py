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

    def find(self, value):
        c, _ = self.findvalue(value)
        if c is None:
            return False
        else:
            return True

    def findvalue(self, value):
        parentnode = curnode = self.root
        while curnode != None:
            if value == curnode.value:
                return curnode, parentnode
            parentnode = curnode
            if value > curnode.value:
                curnode = curnode.right
            else:
                curnode = curnode.left
        return None, None
    
    def replace_child(self, parentnode, childnode, newnode):
        if parentnode == self.root:
            self.root = newnode
        elif parentnode.value > childnode.value:
            parentnode.left = newnode
        else:
            parentnode.right = newnode
    
    def delete(self, value):
        curnode, parentnode = self.findvalue(value)
        if curnode is None:
            return False
        if curnode.left == None and curnode.right == None:
            self.replace_child(parentnode, curnode, None)
        elif curnode.right == None:
            self.replace_child(parentnode, curnode, curnode.left)
        elif curnode.left == None:
            self.replace_child(parentnode, curnode, curnode.right)
        else:
            p = curnode
            r = curnode.right
            while r.left != None:
                p = r
                r = r.left
            curnode.value = r.value
            self.replace_child(p, r, r.right)


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
        elif common[0] == 'f':
            if binarytree.find(int(common[5:])):
                print('yes')
            else:
                print('no')
        elif common[0] == 'd':
            binarytree.delete(int(common[7:]))
        else:
            binarytree.inorder(binarytree.root)
            print()
            binarytree.preorder(binarytree.root)
            print()

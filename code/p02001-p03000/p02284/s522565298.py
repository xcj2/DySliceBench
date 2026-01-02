class Node():
    def __init__(self, key = None ,left =None ,right = None):
        self.key_value = key
        self.left = left
        self.right = right

class BST():
    def __init__(self):
        self.root = None

    def insert(self, data):
        n = self.root
        if n == None:
            self.root = Node(data)
            return
        else:
            while True:
                entry = n.key_value
                if data < entry:
                    if n.left is None:
                        n.left = Node(data)
                        return
                    n = n.left
                elif data > entry:
                    if n.right is None:
                        n.right = Node(data)
                        return
                    n = n.right
                else:
                    n.data = data
                    return

    def find(self,data):
        n = self.root
        if n == None:
            return False
        else:
            lst = []
            lst.append(n)
            while len(lst) > 0:
                node = lst.pop()
                if node.key_value == data:
                    return True
                if node.left != None and data < node.key_value:
                    lst.append(node.left)
                if node.right != None and data > node.key_value:
                    lst.append(node.right)
        return False

    def inorder(self,node):
        if node is None:
            return
        else:
            self.inorder(node.left)
            print(' {}'.format(node.key_value),end='')
            self.inorder(node.right)

    def preorder(self,node):
        if node is None:
            return
        else:
            print(' {}'.format(node.key_value),end='')
            self.preorder(node.left)
            self.preorder(node.right)

if __name__ == "__main__":
    n = int(input())

    bst = BST()
    for i in range(n):
        o = input().split()

        if o[0] == 'insert':
            bst.insert(int(o[1]))
        elif o[0] == 'print':
            bst.inorder(bst.root)
            print()
            bst.preorder(bst.root)
            print()
        elif o[0] == 'find':
            if bst.find(int(o[1])):
                print('yes')
            else:
                print('no')


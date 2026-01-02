
n = int(input())
d = [0] * n
for i in range(n):
    d[i] = int(input())
    
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self, number_list):
        self.root = None
        for data in number_list:
            self.insert(data)
    
    def insert(self, data):
        n = self.root
        if n == None:
            self.root = Node(data)
            return
        else:
            while True:
                entry = n.data
                if entry > data:
                    if n.left is None:
                        n.left = Node(data)
                        return
                    n = n.left
                elif entry < data:
                    if n.right is None:
                        n.right = Node(data)
                        return
                    n = n.right
                else:
                    n.data = data
                    return

    #中間順探索
    def inorder(self,node,ll):
        if node is not None:
            self.inorder(node.left,ll)
            ll.append(node.data)
            self.inorder(node.right,ll)
        return ll

bst = BST(d)
ll = []
print(len(bst.inorder(bst.root,ll)))

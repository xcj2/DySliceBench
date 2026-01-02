class Node:
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None
        self.parent = None

    def isRoot(self):
        return self.parent is None

    def preorder(self, arr):
        arr.append(str(self.id))
        if self.left is not None:
            self.left.preorder(arr)
        if self.right is not None:
            self.right.preorder(arr)

    def inorder(self, arr):
        if self.left is not None:
            self.left.inorder(arr)
        arr.append(str(self.id))
        if self.right is not None:
            self.right.inorder(arr)

    def postorder(self, arr):
        if self.left is not None:
            self.left.postorder(arr)
        if self.right is not None:
            self.right.postorder(arr)
        arr.append(str(self.id))

def insert(root, z):
    y = None
    x = root
    while x is not None:
        y = x
        if z.id < x.id:
            x = x.left
        else:
            x = x.right

    z.parent = y

    if z.id < y.id:
        y.left = z
    else:
        y.right = z


m = int(input())
root = None

for i in range(m):
    arr = input().split()
    if arr[0] == 'print':
        arr = []
        root.inorder(arr)
        print('', ' '.join(arr))
        arr = []
        root.preorder(arr)
        print('', ' '.join(arr))
        continue

    id = int(arr[1])
    if root is None:
        root = Node(id)
        continue

    insert(root, Node(id))


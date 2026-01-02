root = None

class Node:
    def __init__(self, key, left, right):
        self.parent = -1
        self.key = key
        self.left = left
        self.right = right

def preorder(T):
    if T is None:
        return
    print(' ' + str(T.key), end='')
    preorder(T.left)
    preorder(T.right)

def inorder(T):
    if T is None:
        return
    inorder(T.left)
    print(' ' + str(T.key), end='')
    inorder(T.right)

def find(T, z):
    if T is None:
        return False
    if T.key == z:
        return True

    if z < T.key and T.left is not None:
        return find(T.left, z)
    elif z > T.key and T.right is not None:
        return find(T.right, z)
    else:
        return False

def insert(T, z):
    global root
    if T is None:
        root = Node(z, None, None)
        return

    # print("\n# Insert: " + str(z))
    # print("# T: " + str(T.key))

    parent = T
    while True:
        if parent.left is None and parent.right is None:
            break
        elif parent.left is None and z < parent.key:
            break
        elif parent.right is None and z > parent.key:
            break

        # print("# left: " + str(parent.left.key))
        # print("# right: " + str(parent.right.key))

        if z < parent.key:
            parent = parent.left
#            print("# Slide parent to left: " + str(parent.key))
        else:
            parent = parent.right
#            print("# Slide parent to right: " + str(parent.key))

    if z < parent.key:
        node = Node(z, None, None)
        parent.left = node
    elif z > parent.key:
        node = Node(z, None, None)
        parent.right = node

n = int(input())

for i in range(n):
    s = input().split()
    if s[0] == 'insert':
        insert(root, int(s[1]))
    elif s[0] == 'find':
        if find(root, int(s[1])):
            print('yes')
        else:
            print('no')
    else:
        inorder(root)
        print('')
        preorder(root)
        print('')


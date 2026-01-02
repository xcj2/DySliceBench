class Node:
    def __init__(self, x, priority):
        self.data = x
        self.priority = priority
        self.left = None
        self.right = None

def rightRotate(node):
    leftNode = node.left
    node.left = leftNode.right
    leftNode.right = node
    return leftNode

def leftRotate(node):
    rightNode = node.right
    node.right = rightNode.left
    rightNode.left = node
    return rightNode

def find(node, x):
    while node is not None:
        if x == node.data:
            return True
        elif x < node.data:
            node = node.left
        else:
            node = node.right
    return False

def insert(node, x, priority):
    if node is None:
        return Node(x, priority)

    if x == node.data:
        return node

    if x < node.data:
        node.left = insert(node.left, x, priority)
        if node.priority < node.left.priority:
            node = rightRotate(node)

    else:
        node.right = insert(node.right, x, priority)
        if node.priority < node.right.priority:
            node = leftRotate(node)
    return node

def inorder_print(node, x = 0):
    if node is not None:
        print('',node.data, end = '')
        inorder_print(node.left, x + 1)
        inorder_print(node.right, x + 1)

def preorder_print(node, x = 0):
    if node is not None:
        preorder_print(node.left, x + 1)
        print('',node.data, end = '')
        preorder_print(node.right, x + 1)


def delete(node, x):
    if node == None:
        return None
    if x < node.data:
        node.left = delete(node.left, x)
    elif x > node.data:
        node.right = delete(node.right, x)
    else:
        return _delete(node, x)

    return node

def _delete(node, x):
    if node.left == None and node.right == None:
        return None
    elif node.left == None:
        node = leftRotate(node)
    elif node.right == None:
        node = rightRotate(node)
    else:
        if node.left.priority > node.right.priority:
            node = rightRotate(node)
        else:
            node = leftRotate(node)
    return delete(node, x)

class Treap:
    def __init__(self):
        self.root = None

    def find_(self, x):
        return find(self.root, x)

    def insert_(self, x, pri):
        self.root = insert(self.root, x, pri)

    def delete_(self, x):
        self.root = delete(self.root, x)

    def traverse_(self):
        for x in traverse(self.root):
            yield x

    def print_treap_(self):
        preorder_print(self.root)
        print('')
        inorder_print(self.root)
        print('')

if __name__ == '__main__':

    n = int(input())
    treap = Treap()
    for i in range(n):
        _input = input()
        if _input == 'print':
            #print operation
            treap.print_treap_()

        else:
            operate, nums = _input.split(' ', 1)
            if operate == 'insert':
                #insert operation
                k, p = (int(z) for z in nums.split())
                treap.insert_(k, p)

            elif operate == 'find':
                k = int(nums)
                res = treap.find_(k)
                if res:
                    print("yes")
                else:
                    print("no")

            elif operate == 'delete':
                k = int(nums)
                treap.delete_(k)


class Node():
    def __init__(self, value):
        self.value = value
        self.parent = -1
        self.left = -1
        self.right = -1

def preorder(tree, root):
    if root == -1:
        pass
    else:
        print(' %d' % root, end='')
        preorder(tree, tree[root].left)
        preorder(tree, tree[root].right)

def inorder(tree, root):
    if root == -1:
        pass
    else:
        inorder(tree, tree[root].left)
        print(' %d' % root, end='')
        inorder(tree, tree[root].right)

def postorder(tree, root):
    if root == -1:
        pass
    else:
        postorder(tree, tree[root].left)
        postorder(tree, tree[root].right)
        print(' %d' % root, end='')

if __name__ == '__main__':
    n = int(input())
    tree = {}
    root = -1
    for _ in range(n):
        datas = [int(num) for num in input().split(' ')]
        nodeid = datas[0]
        if nodeid not in tree.keys():
            tree[nodeid] = Node(nodeid)
        tree[nodeid].left = left = int(datas[1])
        tree[nodeid].right = right = int(datas[2])
        if left != -1:
            if left not in tree.keys():
                tree[left] = Node(left)
            tree[left].parent = nodeid
        if right != -1:
            if right not in tree.keys():
                tree[right] = Node(right)
            tree[right].parent = nodeid

    for i in range(n):
        if tree[i].parent == -1:
            # this is root
            root = i
            break
            
    print('Preorder')
    preorder(tree, root)
    print()

    print('Inorder')
    inorder(tree, root)
    print()

    print('Postorder')
    postorder(tree, root)
    print()

class Node():
    def __init__(self, value):
        self.value = value
        self.deep = -1
        self.parent = None
        self.left = -1
        self.right = -1
        self.height = -1
        self.sib = -1

def setdeep(tree, i, deep):
    tree[i].deep = deep
    if tree[i].left != -1:
        setdeep(tree, tree[i].left, deep + 1)
    if tree[i].right != -1:
        setdeep(tree, tree[i].right, deep + 1)

def setheight(tree, i):
    if tree[i].height != -1:
        pass
    elif tree[i].left == -1 and tree[i].right == -1:
        tree[i].height = 0
    elif tree[i].left == -1:
        tree[i].height = setheight(tree, tree[i].right)
    elif tree[i].right == -1:
        tree[i].height = setheight(tree, tree[i].left)
    else:
        tree[i].height = max(setheight(tree, tree[i].right), setheight(tree, tree[i].left))
    return tree[i].height + 1

if __name__ == '__main__':
    n = int(input())
    tree = {}

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
            tree[left].sib = right
        if right != -1:
            if right not in tree.keys():
                tree[right] = Node(right)
            tree[right].parent = nodeid
            tree[right].sib = left

    for i in range(n):
        curnode = tree[i]
        if curnode.parent is None:
            # this is root
            setdeep(tree, i, 0)
            setheight(tree, i)
            break
            
    for i in range(n):
        curnode = tree[i]
        deg = 0
        if curnode.left == -1 and curnode.right == -1:
            nodetype = 'leaf'
            deg = 0
        else:
            if curnode.left != -1:
                deg += 1
            if curnode.right != -1:
                deg += 1
            nodetype = 'internal node'
        if curnode.parent == None:
            nodetype = 'root'
            parent = -1
        else:
            parent = curnode.parent
        print('node %d: parent = %d, sibling = %d, degree = %d, depth = %d, height = %d, %s' \
            % (i, parent,curnode.sib, deg,  curnode.deep, curnode.height, nodetype) )

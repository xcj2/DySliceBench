class Node():
    def __init__(self, parent =None ,left =None ,right = None):
        self.parent = parent
        self.left = left
        self.right = right

def get_depth(u,tree_list):
    d = 0
    while tree_list[u].parent != -1:
        u = tree_list[u].parent
        d += 1
    return d


def get_sibling(i, tree_list):
    if tree_list[i].parent == -1:
        return -1
    p = tree_list[i].parent
    if tree_list[p].left != i and tree_list[p].left != -1:
        return tree_list[p].left

    if tree_list[p].right != i and tree_list[p].right != -1:
        return tree_list[p].right

    return -1

def get_higt(i, tree_list):
    h1 = 0
    h2 = 0
    if tree_list[i].left != -1:
        h1 = get_higt(tree_list[i].left, tree_list) + 1
    if tree_list[i].right != -1:
        h2 = get_higt(tree_list[i].right, tree_list) + 1

    return max(h1,h2)

if __name__ == "__main__":
    n = int(input())

    tree_list = [Node(-1,-1,-1) for m in range(n)]
    for i in range(n):
        l = input().split()
        v = int(l[0])
        c_list = [int(l[m]) for m in range(1,len(l))]
        tree_list[v].left = c_list[0]
        tree_list[v].right = c_list[1]
        if c_list[0] != -1:
            tree_list[c_list[0]].parent = v
        if c_list[1] != -1:
            tree_list[c_list[1]].parent = v

    for i,t in enumerate(tree_list):
        sibling = get_sibling(i,tree_list)
        degree = 0
        if tree_list[i].left != -1:
            degree += 1
        if tree_list[i].right != -1:
            degree += 1

        depth = get_depth(i, tree_list)
        higt = get_higt(i,tree_list)
        tree_type = ''
        if tree_list[i].parent == -1:
            tree_type = 'root'
        elif tree_list[i].left == -1 and tree_list[i].right == -1:
            tree_type = 'leaf'
        else:
            tree_type = 'internal node'

        print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(
            i,t.parent,sibling,degree,depth,higt,tree_type))



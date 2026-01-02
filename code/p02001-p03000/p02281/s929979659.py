class Node():
    def __init__(self, parent =None ,left =None ,right = None):
        self.parent = parent
        self.left = left
        self.right = right

def preorder_walk(i, tree_list):
    if i == -1:
        return
    print(' {}'.format(i),end='')
    preorder_walk(tree_list[i].left,tree_list)
    preorder_walk(tree_list[i].right,tree_list)

def inorder_walk(i, tree_list):
    if i == -1:
        return
    inorder_walk(tree_list[i].left,tree_list)
    print(' {}'.format(i),end='')
    inorder_walk(tree_list[i].right,tree_list)

def postorder_walk(i, tree_list):
    if i == -1:
        return
    postorder_walk(tree_list[i].left,tree_list)
    postorder_walk(tree_list[i].right,tree_list)
    print(' {}'.format(i),end='')

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

    root = -1
    for i,t in enumerate(tree_list):
        if t.parent == -1:
            root = i
            break

    print('Preorder')
    preorder_walk(root,tree_list)
    print()
    print('Inorder')
    inorder_walk(root,tree_list)
    print()
    print('Postorder')
    postorder_walk(root,tree_list)
    print()



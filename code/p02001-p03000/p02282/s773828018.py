class Tree:
    __slots__ = ['id', 'p', 'left', 'right']
    def __init__(self, id):
        self.id = id
        self.left = -1
        self.right = -1
    def setc(self, c):
        if self.left == -1:
            self.left = c
        else:
            self.right = c
    def __str__(self):
        return f"node {self.id}: left = {self.left}, right = {self.right}"
n = int(input())
tree = tuple(Tree(i) for i in range(n + 1))
pretree = list(map(int, input().split()))
m = {a:i for i, a in enumerate(pretree)}
inotree = list(map(int, input().split()))
root = pretree[0]
def treeSet(A, id):
    if A == []:
        return -1
    elif len(A) == 1:
        return A[0]
    min_A_index = A.index(id)
    global tree
    if 0 < min_A_index:
        min_A = min(A[:min_A_index], key=lambda x: m[x])
        left = treeSet(A[:min_A_index], min_A)
        tree[id].left = left
    if 0 < len(A) - min_A_index - 1:
        min_A = min(A[min_A_index + 1:], key=lambda x: m[x])
        right = treeSet(A[min_A_index + 1:], min_A)
        tree[id].right = right
    return id
treeSet(inotree, root)
ans = []
def postorder_tree_walk(id):
    if tree[id].left != -1:
        postorder_tree_walk(tree[id].left)
    if tree[id].right != -1:
        postorder_tree_walk(tree[id].right)
    global ans
    ans.append(id)
postorder_tree_walk(root)
print(*ans)


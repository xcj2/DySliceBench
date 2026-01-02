# Tree Walk


class Node():
    def __init__(self, idx=-1, parent=-1, left=-1, right=-1):
        self.idx = idx
        self.parent = parent
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self, n):
        self.T = [Node(i) for i in range(n)]
        self.preorder_idx = []
        self.inorder_idx = []
        self.postorder_idx = []

    def set_children(self, idx, l, r):
        node = self.T[idx]
        node.left = l
        node.right = r
        if l != -1:
            self.T[l].parent = idx
        if r != -1:
            self.T[r].parent = idx

    def get_root(self):
        for idx, node in enumerate(self.T):
            if node.parent == -1:
                return idx

    def preorder(self, idx):
        if idx == -1:
            return
        node = self.T[idx]
        self.preorder_idx.append(idx)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, idx):
        if idx == -1:
            return
        node = self.T[idx]
        self.inorder(node.left)
        self.inorder_idx.append(idx)
        self.inorder(node.right)

    def postorder(self, idx):
        if idx == -1:
            return
        node = self.T[idx]
        self.postorder(node.left)
        self.postorder(node.right)
        self.postorder_idx.append(idx)


N = int(input())
tree = BinaryTree(N)

for _ in range(N):
    idx, l, r = map(int, input().split())
    tree.set_children(idx, l, r)

root = tree.get_root()
tree.preorder(root)
tree.inorder(root)
tree.postorder(root)

print('Preorder')
print('', *(tree.preorder_idx))
print('Inorder')
print('', *(tree.inorder_idx))
print('Postorder')
print('', *(tree.postorder_idx))


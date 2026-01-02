class Node:
    
    def __init__(self, parent = -1, left = -1, right = -1):
        self.parent = parent
        self.left = left
        self.right = right
    
    def get_degree(self):
        d = 0
        if self.left != -1:
            d += 1
        if self.right != -1:
            d += 1
        return d

class BinaryTree:
    
    def __init__(self, size):
        self.tree = [Node() for i in range(N)]
    
    def set(self, node_id, left, right):
        self.tree[node_id].left = left
        self.tree[node_id].right = right

        if left != -1:
            self.tree[left].parent = node_id
        if right != -1:
            self.tree[right].parent = node_id
    
    def get_root(self):
        for i in range(len(self.tree)):
            node = self.tree[i]
            if node.parent == -1:
                return i
    
    def walk_preorder(self, node):
        if node == -1:
            return
        print(' %d' % (node), end = '')
        self.walk_preorder(self.tree[node].left)
        self.walk_preorder(self.tree[node].right)
    
    def walk_inorder(self, node):
        if node == -1:
            return
        self.walk_inorder(self.tree[node].left)
        print(' %d' % (node), end = '')
        self.walk_inorder(self.tree[node].right)
    
    def walk_postorder(self, node):
        if node == -1:
            return
        self.walk_postorder(self.tree[node].left)
        self.walk_postorder(self.tree[node].right)
        print(' %d' % (node), end = '')

N = int(input())

# 二分木初期化
binary_tree = BinaryTree(N)

# 値設定
for _ in range(N):
    node_id, left, right = list(map(int, input().split()))
    binary_tree.set(node_id, left, right)

root = binary_tree.get_root()

print('Preorder')
binary_tree.walk_preorder(root)
print('\n', end = '')
print('Inorder')
binary_tree.walk_inorder(root)
print('\n', end = '')
print('Postorder')
binary_tree.walk_postorder(root)
print('\n', end = '')

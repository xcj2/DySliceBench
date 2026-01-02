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
    
    def get_depth(self, node_id):
        d = 0
        while self.tree[node_id].parent != -1:
            d += 1
            node_id = self.tree[node_id].parent
        return d
    
    def get_height(self, node_id):
        h_left = h_right = 0
        if self.tree[node_id].left != -1:
            h_left = self.get_height(self.tree[node_id].left) + 1
        if self.tree[node_id].right != -1:
            h_right = self.get_height(self.tree[node_id].right) + 1
        
        return max(h_left, h_right)
    
    def get_sibling(self, node_id):
        
        if self.tree[node_id].parent == -1:
            return -1
        
        parent_id = self.tree[node_id].parent
        parent = self.tree[parent_id]
        
        if parent.left != -1 and parent.left != node_id:
            return parent.left
        if parent.right != -1 and parent.right != node_id:
            return parent.right
        
        return -1
    
    def get_node_type(self, node_id):
        node = self.tree[node_id]
        
        if node.parent == -1:
            return 'root'
        
        if node.left == -1 and node.right == -1:
            return 'leaf'
        
        return 'internal node'
    
    def print(self):
        for i in range(len(self.tree)):
            node = self.tree[i]
            node_id = i
            parent = node.parent
            sibling = self.get_sibling(node_id)
            degree = node.get_degree()
            depth = self.get_depth(node_id)
            height = self.get_height(node_id)
            node_type = self.get_node_type(node_id)
            print('node %d: parent = %d, sibling = %d, degree = %d, depth = %d, height = %d, %s' % (node_id, parent, sibling, degree, depth, height, node_type))
            
N = int(input())

binary_tree = BinaryTree(N)

for _ in range(N):
    node_id, left, right = list(map(int, input().split()))
    binary_tree.set(node_id, left, right)

binary_tree.print()

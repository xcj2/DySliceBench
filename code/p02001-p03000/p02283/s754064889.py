import sys
input = sys.stdin.readline
n = int(input())

Order = []
for _ in range(n):
    o = input().split()
    Order.append(o)

class Node:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key, value):
        if self.root == None:
            node = Node(key, value, None, None)
            self.root = node
        else:
            node = Node(key, value, None, None)
            cmp_node = self.root
            while 1:
                if cmp_node.value > value and cmp_node.left == None:
                    cmp_node.left = node
                    break
                elif cmp_node.value > value and cmp_node.left != None:
                    cmp_node = cmp_node.left
                elif cmp_node.value < value and cmp_node.right == None:
                    cmp_node.right = node
                    break
                elif cmp_node.value < value and cmp_node.right != None:
                    cmp_node = cmp_node.right
        
def mid_search(node):
    if node == None:
        return
    mid_search(node.left)
    print('', node.key, end='')
    mid_search(node.right)
    
def fast_search(node):
    if node == None:
        return
    print('', node.key, end='')
    fast_search(node.left)
    fast_search(node.right)    
        
T = BinaryTree()
for o in Order:
    if o[0] == 'insert':
        T.insert(int(o[1]), int(o[1]))
    if o[0] == 'print':
        mid_search(T.root)
        print()
        fast_search(T.root)
        print()
        







from enum import Enum, auto
from collections import deque

class Color(Enum):
    WHITE = auto()
    GRAY = auto()
    BLACK = auto()

class BinaryTreeNode():
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.sibling = None
        self.color = Color.WHITE

def print_elements(ordered):
    for ele in ordered:
        print(' {}'.format(ele), end='')
    print('')

n = int(input())
nodes = [BinaryTreeNode() for i in range(n)]
for i in range(n):
    id, left, right = list(map(int, input().split(' ')))
    if left != -1:
        nodes[id].left = left
        nodes[left].parent = id
        nodes[left].sibling = right
    if right != -1:
        nodes[id].right = right
        nodes[right].parent = id
        nodes[right].sibling = left

root = 0
for i in range(n):
    if nodes[i].parent == None:
        root = i

def init_color():
    global nodes
    for i in range(len(nodes)):
        nodes[i].color = Color.WHITE

def preorder_bfs(s):
    preordered.append(s)
    nodes[s].color = Color.GRAY
    if nodes[s].left != None and nodes[nodes[s].left].color == Color.WHITE:
        preorder_bfs(nodes[s].left)
    if nodes[s].right != None and nodes[nodes[s].right].color == Color.WHITE:
        preorder_bfs(nodes[s].right)
    nodes[s].color = Color.BLACK

inorder_stack = deque([])
def inorder_dfs_init(s):
    init_color()
    inorder_stack.append(s)
    inorder_dfs()

def inorder_dfs():
    u = inorder_stack.pop()
    if nodes[u].left != None and nodes[nodes[u].left].color == Color.WHITE:
        inorder_stack.append(u)
        inorder_stack.append(nodes[u].left)
        inorder_dfs()
    inordered.append(u)
    if nodes[u].right != None and nodes[nodes[u].right].color == Color.WHITE:
        inorder_stack.append(nodes[u].right)
        inorder_dfs()

postorder_stack = deque([])
def postorder_dfs_init(s):
    init_color()
    postorder_stack.append(s)
    postorder_dfs()

def postorder_dfs():
    u = postorder_stack.pop()
    if nodes[u].left != None and nodes[nodes[u].left].color == Color.WHITE:
        postorder_stack.append(u)
        postorder_stack.append(nodes[u].left)
        postorder_dfs()
    if nodes[u].right != None and nodes[nodes[u].right].color == Color.WHITE:
        postorder_stack.append(nodes[u].right)
        postorder_dfs()
    postordered.append(u)

print('Preorder') # 根節点、左部分木、右部分木の順
preordered = []
preorder_bfs(root)
print_elements(preordered)

print('Inorder') # 左部分木、根節点、右部分木の順
inordered = []
inorder_dfs_init(root)
print_elements(inordered)

print('Postorder') # 左部分木、右部分木、根節点の順
postordered = []
postorder_dfs_init(root)
print_elements(postordered)


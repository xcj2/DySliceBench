from collections import deque
from sys import stdin
input = stdin.readline

class Element:
    def __init__(self, node):
        self.node = node
        self.parent = -1
        self.depth = 0
        self.status = "internal node"
        self.children = None
    
    def display(self):
        print("node %d: parent = %d, depth = %d, %s, %s"
        %(self.node, self.parent, self.depth, self.status, str(self.children)))
        
N = int(input())

NODE_DICT = {}
ROOT_SEARCH = [True]*N

for loop in range(N):
    DATA = list(map(int, input().split()))
    node = DATA[0]    
    tmp = Element(node)
    tmp.children = DATA[2:]
    NODE_DICT[node] = tmp
    for i in tmp.children:
        ROOT_SEARCH[i] = False
    
#for node in NODE_DICT.keys():
#    for child in NODE_DICT[node].children:
#        ROOT_SEARCH[child] = False


for key in range(len(ROOT_SEARCH)):
    if ROOT_SEARCH[key]:
        root = key

def Process(parent):
    for child in parent.children:
        NODE_DICT[child].parent = parent.node
        NODE_DICT[child].depth = parent.depth + 1
    if parent.children == []:
        parent.status = "leaf"
    else:
        for child in parent.children:
            Process(NODE_DICT[child])
    

Process(NODE_DICT[root])
NODE_DICT[root].status = "root"

for i in range(N):
    NODE_DICT[i].display()

#for node in range(len(NODE_DICT)):
#    print("node %d: parent = %d, depth = %d, %s, %s"%(NODE_DICT[node].node, 
#    NODE_DICT[node].parent, NODE_DICT[node].depth, NODE_DICT[node].status, 
#   str(NODE_DICT[node].children)))

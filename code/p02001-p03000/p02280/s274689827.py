from sys import stdin
input = stdin.readline

class Node:    
    def __init__(self, number):
        self.number  = number
        self.parent, self.sibling, self.degree, self.depth, self.height = -1,-1,0,0,0
        self.nodetype = 'internal node'
        self.child = []
    
    def output(self):
        print('node %d: parent = %d, sibling = %d, degree = %d, depth = %d, height = %s, %s'%(self.number,self.parent,self.sibling,self.degree,self.depth,self.height,self.nodetype))

def check(node, depth):
    node.depth = depth
    if node.child != []:
        depth += 1
        for num in node.child:
            node.height = max(check(nodelist[num],depth) + 1, node.height)
    return node.height

n = int(input())
nodelist = [Node(i) for i in range(n)]
for _ in range(n):
    idx, left, right = map(int, input().split())
    if left == -1 and right == -1:
        nodelist[idx].nodetype = 'leaf'
    elif left != -1 and right != -1:
        nodelist[idx].child = [left,right]
        nodelist[idx].degree = 2
        nodelist[left].sibling, nodelist[right].sibling = right, left
        nodelist[left].parent, nodelist[right].parent = idx, idx
    elif left == -1 or right == -1:
        exist = max(left,right)
        nodelist[idx].child = [exist]
        nodelist[idx].degree = 1
        nodelist[exist].parent = idx

for node in nodelist:
    if node.parent == -1:
        node.nodetype = 'root'
        node.height = check(node, 0)
        break

for node in nodelist:
    node.output()

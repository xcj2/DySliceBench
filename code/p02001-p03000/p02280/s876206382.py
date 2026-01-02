class Node:
    def __init__(self,num,leftchild,rightchild):
        self.id = num
        self.parent = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = 'leaf'
        self.leftchild = leftchild
        self.rightchild = rightchild
    
    def get_infomation(self):
        print('node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}'.format(self.id,self.parent,self.sibling,self.degree, self.depth,self.height,self.type))
 
def set_propaties(num,parent,sibling,depth):
    if num == -1:     
        return -1
    node = tree[num]
    lc = node.leftchild
    rc = node.rightchild
    node.parent = parent
    node.sibling = sibling
    node.depth = depth
    node.degree = (node.leftchild != -1) + (node.rightchild != -1)
    if lc != -1 or rc != -1:
        node.type = 'internal node'
    node.height = max(set_propaties(lc, num, rc, depth + 1),set_propaties(rc, num, lc, depth + 1)) + 1
    return node.height

n = int(input())
tree = [None]*n

root_num = int(n*(n-1)/2)

for x in range(n):
    num, leftchild, rightchild = list(map(int,input().split()))
    node = Node(num, leftchild, rightchild)
    tree[num] = node
    root_num -= (max(0, leftchild) + max(0, rightchild))

set_propaties(root_num, -1, -1, 0)
tree[root_num].type = 'root'

for n in tree:
    n.get_infomation()
    

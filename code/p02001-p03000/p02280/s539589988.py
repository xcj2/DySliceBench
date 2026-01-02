N = int(input())
M = []

type = ['root','internal node','leaf']

class node:
    def __init__(self,idx,parent,left,right):
        self.idx = idx
        self.parent = parent
        self.left = left
        self.right= right
        
        self.sibling = -1
        self.degree= 0
        self.depth = 0
        self.height = 0
        self.type=-1

    def tostr(self):
        print('node %d: parent = %d, sibling = %d, degree = %d, depth = %d, height = %d, %s' % (self.idx, self.parent, self.sibling, self.degree, self.depth, self.height, type[self.type])) 
tree = [[] for x in range(N)]


#'idx, parent, sibling, degree, depth, height, type'

for a in range(N):
    idx,left,right = map(int,input().strip().split(' '))
    tree[idx] = node(idx, -1, left,right)

for a in range(N):
    nd = tree[a]
    if nd.left != -1:
        tree[nd.left].parent = a
    if nd.right != -1:
        tree[nd.right].parent = a
    if nd.left !=  -1:
        tree[nd.left].sibling = nd.right
    if nd.right !=  -1:
        tree[nd.right].sibling = nd.left

    if nd.left == nd.right :
        nd.type=2
        nd.degree=0
    else:
        nd.type=1
        if nd.left == -1 or nd.right == -1:
            nd.degree = 1
        else:
            nd.degree = 2

root = ''
for a in range(N):
    if tree[a].parent == -1:
        root = a
        tree[root].type=0
    
def search(root,depth):
    root = tree[root]
    root.depth = depth
    if root.type ==  2:
        return
    else:
        if root.right == -1 and root.left == -1:
            return
        if root.right != -1:
            search(root.right,depth+1)
        if root.left != -1:
            search(root.left,depth+1)

search(root,0)

def height(root,hei):
    root = tree[root]
    if root.type==2 or (root.right == -1 and root.left == -1):
        root.height=0
        return hei
    else:
        if root.left == -1:
            return height(root.right,hei+1)
        elif root.right == -1:
            return height(root.left,hei+1)
        else:
            return max(height(root.left,hei+1),height(root.right,hei+1))
for i in range(N):
    tree[i].height=height(i,0)

for a in range(N):
    tree[a].tostr()






    
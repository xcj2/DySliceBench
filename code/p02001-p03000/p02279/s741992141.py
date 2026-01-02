class tree:
    def __init__(self,name,parent):
        self.name = name
        self.parent = parent
        
        
n = int(input())
trees = {str(i):tree(str(i),'-1') for i in range(n)}
child = {}

for i in range(n):
    s = [i for i in input().split()]
    p = s[0]
    child[p] = s[2:]
    s_t = s[2:]
    for j in range(len(s_t)):
        trees[s_t[j]] = tree(s_t[j],p)

def getDepth(u):
    d = 0
    while trees[u].parent != '-1':
        u = trees[u].parent
        d += 1
    return d

def getChildren(u):
    c = []
    for i in trees.values():
        if i.parent == u:
            c.append(i.name)
    return c

for i in range(n):
    
    par = trees[str(i)].parent
    dep = getDepth(str(i))
    ch = [int(i) for i in child[str(i)]]
    
    if par == '-1':sit = 'root'
    elif len(ch) != 0:sit = 'internal node'
    else:sit = 'leaf'
    
    print('node {}: parent = {}, depth = {}, {}, {}'.format(i,par,dep,sit,ch))

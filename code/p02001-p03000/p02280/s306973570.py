# Tree - Rooted Trees
class Node:
    def is_leaf(self):
        return self.depth > 0 and len(self.degree) == 0
    
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.sibling = None
        self.degree = []
        self.depth = 0
        self.height = 0
    def __str__(self):
        p = self.parent.id if self.parent else -1
        s = self.sibling.id if self.sibling else -1
        d = len(self.degree)
        typ = 'root'
        if self.depth > 0: typ = 'internal node'
        if d == 0 and self.depth > 0: typ = 'leaf'
        h = self.height
        return 'node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}'.format(self.id, p, s, d, self.depth, h, typ)

def calc_cld_depth(nd):
    cs = nd.degree
    for c in cs:
        c.depth = nd.depth + 1
        calc_cld_depth(c)

n = int(input())
rbt = [Node(i) for i in range(n)]
for i in range(n):
    id,left,right = map(int, input().split())
    tgt = rbt[id]
    l,r = None,None
    if not left == -1:
        l = rbt[left]
        l.depth += tgt.depth + 1
        l.parent = tgt
        calc_cld_depth(l)
        tgt.degree.append(l)
    if not right == -1:
        r = rbt[right]
        r.depth += tgt.depth + 1
        r.parent = tgt
        calc_cld_depth(r)
        tgt.degree.append(r)
    if (not left == -1) and (not right == -1):
        l.sibling, r.sibling = r,l
    if left == -1 and right == -1:
        if tgt.parent: tgt.depth = tgt.parent.depth + 1
# calc height
for c in rbt:
    h = 0
    if c.is_leaf():
        c.height = h
        p = c.parent
        while p:
            h += 1
            if p.height < h: p.height = h
            p = p.parent
for t in rbt: print(t)

# Tree - Tree Walk
class Node:
    none = 0
    right = 1
    left = -1
    def is_leaf(self):
        d = 1 if self.right else 0
        d += 1 if self.left else 0
        return self.depth > 0 and d == 0
    def num_child(self):
        d = 1 if self.right else 0
        d += 1 if self.left else 0
        return d
    
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.sibling = None
        # ?????¨?????¨????????¨?????¨????????¨
        self.right,self.left = None,None
        self.depth = 0
        self.height = 0
        self.position = Node.none
    def __str__(self):
        p = self.parent.id if self.parent else -1
        s = self.sibling.id if self.sibling else -1
        d = 1 if self.right else 0
        d += 1 if self.left else 0
        typ = 'root'
        if self.depth > 0: typ = 'internal node'
        if d == 0 and self.depth > 0: typ = 'leaf'
        h = self.height
        return 'node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}'.format(self.id, p, s, d, self.depth, h, typ)

def calc_cld_depth(nd):
    if nd.left:
        nd.left.depth = nd.depth + 1
        calc_cld_depth(nd.left)
    if nd.right:
        nd.right.depth = nd.depth + 1
        calc_cld_depth(nd.right)

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
        l.position = Node.left
        calc_cld_depth(l)
        tgt.left = l
    if not right == -1:
        r = rbt[right]
        r.depth += tgt.depth + 1
        r.parent = tgt
        r.position = Node.right
        calc_cld_depth(r)
        tgt.right = r
    if (not left == -1) and (not right == -1):
        l.sibling, r.sibling = r,l
    if left == -1 and right == -1:
        if tgt.parent: tgt.depth = tgt.parent.depth + 1
# calc height
root = None
for c in rbt:
    if c.depth == 0: root = c
    h = 0
    if c.is_leaf():
        c.height = h
        p = c.parent
        while p:
            h += 1
            if p.height < h: p.height = h
            p = p.parent
#for v in rbt: print(v)
from collections import deque
# Preorder
dq = deque()
visited = [None]*n
cnt = 0
dq.append(root)
while len(dq) > 0:
    pp = dq.pop()
    # ?????????????????¨?????¨????????¨?????¨??????
    visited[cnt] = pp
    cnt += 1
    l,r = pp.left,pp.right
    if r: dq.append(r)
    if l: dq.append(l)
print('Preorder')
ss = ''
for v in visited: ss += ' '+str(v.id)
print(ss)

# Inorder
visited = [None]*n
cnt = 0
dq.append(root)
while len(dq):
    pp = dq.pop()
    # ?????¨?????¨????????????????????¨?????¨??????
    dl = pp.num_child()
    if dl == 0:
        visited[cnt] = pp
        cnt += 1
        continue
    if dl > 0:
        l,r = pp.left,pp.right
        if l and l not in visited:
            dq.append(pp)
            dq.append(l)
        elif r:
            visited[cnt] = pp
            cnt += 1
            dq.append(r)
        else:
            visited[cnt] = pp
            cnt += 1
print('Inorder')
ss = ''
for v in visited: ss += ' '+str(v.id)
print(ss)

# Postorder
visited = [None]*n
cnt = 0
dq.append(root)
while len(dq) > 0:
    pp = dq.pop()
    # ?????¨?????¨????????¨?????¨??????????????????
    dl = pp.num_child()
    if dl == 0:
        visited[cnt] = pp
        cnt += 1
        continue
    if dl > 0:
        l,r = pp.left, pp.right
        if (l and l not in visited) or (r and r not in visited):
            if pp: dq.append(pp)
            if r: dq.append(r)
            if l: dq.append(l)
        else:
            visited[cnt] = pp
            cnt += 1
            continue
print('Postorder')
ss = ''
for v in visited: ss += ' '+str(v.id)
print(ss)

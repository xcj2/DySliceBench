class PSTNode():
    def __init__(self, val=None):
        self.val = val
        self.key = 0
        self.dep = None
        self.lt = None
        self.rt = None
        self.par = None

class PersistentSegmentTree():
    def __init__(self, q, array, func=min, ie=2**63-1):
        self.q = q
        self.h = (len(array) - 1).bit_length()
        self.n = 2**self.h
        array += [ie] * (self.n - len(array))
        self.roots = [None for _ in range(q + 2)]
        self.roots[-1] = root = PSTNode()
        root.dep = 0
        self.idx = -1
        self.func = func
        self.ie = ie
        stack = [root]
        order = [root]
        while stack:
            node = stack.pop()
            node.lt = PSTNode()
            node.rt = PSTNode()
            node.lt.par = node
            node.rt.par = node
            ndep = node.dep + 1
            node.lt.dep = ndep
            node.rt.dep = ndep
            node.lt.key = node.key
            node.rt.key = node.key + 2**(self.h - ndep)
            if ndep == self.h:
                node.lt.val = array[node.lt.key]
                node.rt.val = array[node.rt.key]
            else:
                stack.append(node.lt)
                stack.append(node.rt)
                order.append(node.lt)
                order.append(node.rt)
        for node in order[::-1]:
            node.val = self.func(node.lt.val, node.rt.val)

    def get_node(self, idx, t=-1):
        node = self.roots[t]
        k = self.h - 1
        while k != -1:
            if (idx >> k) & 1:
                node = node.rt
            else:
                node = node.lt
            k -= 1
        return node

    def get_val(self, idx, t=-1):
        return self.get_node(idx, t).val

    def set_val(self, idx, x, t=-1):
        old_node = self.get_node(idx, t)
        new_node = PSTNode(x)
        new_node.key = old_node.key
        for i in range(self.h):
            new_par = PSTNode()
            old_par = old_node.par
            new_par.key = old_par.key
            new_node.par = new_par
            if old_par.lt == old_node:
                new_par.lt = new_node
                new_par.rt = old_par.rt
                old_par.rt.par = new_par
            else:
                new_par.lt = old_par.lt
                new_par.rt = new_node
                old_par.lt.par = new_par
            new_par.val = self.func(new_par.lt.val, new_par.rt.val)
            old_node = old_par
            new_node = new_par
        self.roots[self.idx] = new_node

    def get_range(self, lt, rt, t=-1):
        node = self.roots[t]
        res = self.ie
        stack = [node]
        while stack:
            node = stack.pop()
            if lt <= node.key and node.key + 2**(self.h - node.dep) <= rt:
                res = self.func(res, node.val)
            elif node.key + 2**(self.h - node.dep) <= lt or rt <= node.key:
                continue
            else:
                stack.append(node.lt)
                stack.append(node.rt)
        return res

    def update(self):
        self.idx += 1
        self.roots[self.idx] = self.roots[self.idx - 1]

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

N = int(input())
A = list(map(int, input().split()))

pst = PersistentSegmentTree(0, A, gcd, 0)
res = 1

for i in range(N):
    res = max(res, gcd(pst.get_range(0, i), pst.get_range(i + 1, N + 1)))

print(res)
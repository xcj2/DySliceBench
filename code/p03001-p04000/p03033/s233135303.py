import sys


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.lst = None
        self.rst = None
        self.bias = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def rotate_left(self, v):
        u = v.rst
        v.rst = u.lst
        u.lst = v
        if u.bias == -1:
            u.bias = v.bias = 0
        else:
            u.bias = 1
            v.bias = -1
        return u

    def rotate_right(self, v):
        u = v.lst
        v.lst = u.rst
        u.rst = v
        if u.bias == 1:
            u.bias = v.bias = 0
        else:
            u.bias = -1
            v.bias = 1
        return u

    def rotateLR(self, v):
        u = v.lst
        t = u.rst
        u.rst = t.lst
        t.lst = u
        v.lst = t.rst
        t.rst = v
        self.update_bias_double(t)
        return t

    def rotateRL(self, v):
        u = v.rst
        t = u.lst
        u.lst = t.rst
        t.rst = u
        v.rst = t.lst
        t.lst = v
        self.update_bias_double(t)
        return t

    def update_bias_double(self, v):
        if v.bias == 1:
            v.rst.bias = -1
            v.lst.bias = 0
        elif v.bias == -1:
            v.rst.bias = 0
            v.lst.bias = 1
        else:
            v.rst.bias = 0
            v.lst.bias = 0
        v.bias = 0

    def insert(self, key, val):
        if self.root is None:
            self.root = Node(key, val)
            return

        v = self.root
        history = []
        while v is not None:
            if key < v.key:
                history.append((v, 1))
                v = v.lst
            elif v.key < key:
                history.append((v, -1))
                v = v.rst
            elif v.key == key:
                v.val = val
                return

        p, pdir = history[-1]
        if pdir == 1:
            p.lst = Node(key, val)
        else:
            p.rst = Node(key, val)

        while history:
            v, direction = history.pop()
            v.bias += direction

            new_v = None
            b = v.bias
            if b == 0:
                break

            if b == 2:
                u = v.lst
                if u.bias == -1:
                    new_v = self.rotateLR(v)
                else:
                    new_v = self.rotate_right(v)
                break
            if b == -2:
                u = v.rst
                if u.bias == 1:
                    new_v = self.rotateRL(v)
                else:
                    new_v = self.rotate_left(v)
                break

        if new_v is not None:
            if len(history) == 0:
                self.root = new_v
                return
            p, pdir = history.pop()
            if pdir == 1:
                p.lst = new_v
            else:
                p.rst = new_v

    def delete(self, key):
        v = self.root
        history = []
        while v is not None:
            if key < v.key:
                history.append((v, 1))
                v = v.lst
            elif v.key < key:
                history.append((v, -1))
                v = v.rst
            else:
                break
        else:
            return False

        if v.lst is not None:
            history.append((v, 1))
            lmax = v.lst
            while lmax.rst is not None:
                history.append((lmax, -1))
                lmax = lmax.rst

            v.key = lmax.key
            v.val = lmax.val

            v = lmax

        c = v.rst if v.lst is None else v.lst

        if history:
            p, pdir = history[-1]
            if pdir == 1:
                p.lst = c
            else:
                p.rst = c

        else:
            self.root = c
            return True

        while history:
            new_p = None

            p, pdir = history.pop()
            p.bias -= pdir

            b = p.bias
            if b == 2:
                if p.lst.bias == -1:
                    new_p = self.rotateLR(p)
                else:
                    new_p = self.rotate_right(p)

            elif b == -2:
                if p.rst.bias == 1:
                    new_p = self.rotateRL(p)
                else:
                    new_p = self.rotate_left(p)

            elif b != 0:
                break

            if new_p is not None:
                if len(history) == 0:
                    self.root = new_p
                    return True
                gp, gpdir = history[-1]
                if gpdir == 1:
                    gp.lst = new_p
                else:
                    gp.rst = new_p
                if new_p.bias != 0:
                    break
        return True

    def member(self, key):
        v = self.root
        while v is not None:
            if key < v.key:
                v = v.lst
            elif v.key < key:
                v = v.rst
            else:
                return True
        return False

    def get(self, key):
        v = self.root
        while v is not None:
            if key < v.key:
                v = v.lst
            elif v.key < key:
                v = v.rst
            else:
                return v.val
        return None

    def lower_bound(self, key):
        ret = (float('inf'), 0)
        v = self.root
        while v is not None:
            if v.key >= key:
                if ret > v.key:
                    ret = v.key
                v = v.lst
            else:
                v = v.rst
        return ret

    def upper_bound(self, key):
        ret = -float('inf')
        v = self.root
        while v is not None:
            if v.key <= key:
                if ret < v.key:
                    ret = v.key
                v = v.rst
            else:
                v = v.lst
        return ret

    def __contains__(self, key): return self.member(key)
    def __getitem__(self, key): return self.get(key)
    def __setitem__(self, key, val): return self.insert(key, val)
    def __delitem__(self, key): return self.delete(key)
    def __bool__(self): return self.root is not None

    def __str__(self):
        return self.tostr_rec("", "", self.root)

    def tostr_rec(self, head, bar, t):
        graph = ""

        if t != None:
            graph += self.tostr_rec(head + "    ", "／", t.rst)
            node = str(t.key) + ":" + str(t.bias)
            graph += head + bar + node + "\n"
            graph += self.tostr_rec(head + "    ", "＼", t.lst)

        return graph


read = sys.stdin.buffer.read
readlines = sys.stdin.buffer.readlines
input = sys.stdin.buffer.readline
N, Q = map(int, input().split())
S = []
T = []
for i in range(N):
    s, t, x = map(int, input().split())
    S.append((s-x, s, x))
    T.append((t-x, s, x))

S.sort(reverse=True)
T.sort(reverse=True)

INF = 10**10
avl = AVLTree()
ans = []
for d in map(int, read().split()):
    while S and S[-1][0] <= d:
        sx, s, x = S.pop()
        avl[(x, sx+x)] = x

    while T and T[-1][0] <= d:
        tx, s, x = T.pop()

        del avl[(x, s)]
    x, s = avl.lower_bound((-INF, 0))
    ans.append(x if x < INF else -1)

print('\n'.join(map(str, ans)))

class Node:
    def __init__(self, key):
        self.key = key
        self.lch = None
        self.rch = None
        self.bias = 0
 
 
class AVLTree:
    def __init__(self):
        self.root = None
 
    def rotate_left(self, v):
        u = v.rch
        v.rch = u.lch
        u.lch = v
        if u.bias == -1:
            u.bias = v.bias = 0
        else:
            u.bias = 1
            v.bias = -1
        return u
 
    def rotate_right(self, v):
        u = v.lch
        v.lch = u.rch
        u.rch = v
        if u.bias == 1:
            u.bias = v.bias = 0
        else:
            u.bias = -1
            v.bias = 1
        return u
 
    def rotateLR(self, v):
        u = v.lch
        t = u.rch
        u.rch = t.lch
        t.lch = u
        v.lch = t.rch
        t.rch = v
        self.update_bias_double(t)
        return t
 
    def rotateRL(self, v):
        u = v.rch
        t = u.lch
        u.lch = t.rch
        t.rch = u
        v.rch = t.lch
        t.lch = v
        self.update_bias_double(t)
        return t
 
    def update_bias_double(self, v):
        if v.bias == 1:
            v.rch.bias = -1
            v.lch.bias = 0
        elif v.bias == -1:
            v.rch.bias = 0
            v.lch.bias = 1
        else:
            v.rch.bias = 0
            v.lch.bias = 0
        v.bias = 0
 
    def add(self, key):
        if self.root is None:
            self.root = Node(key)
            return
 
        v = self.root
        history = []
        while v is not None:
            if key < v.key:
                history.append((v, 1))
                v = v.lch
            elif v.key < key:
                history.append((v, -1))
                v = v.rch
            else:
                return
 
        p, pdir = history[-1]
        if pdir == 1:
            p.lch = Node(key)
        else:
            p.rch = Node(key)
 
        while history:
            v, direction = history.pop()
            v.bias += direction
 
            new_v = None
            b = v.bias
            if b == 0:
                break
 
            if b == 2:
                u = v.lch
                if u.bias == -1:
                    new_v = self.rotateLR(v)
                else:
                    new_v = self.rotate_right(v)
                break
            if b == -2:
                u = v.rch
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
                p.lch = new_v
            else:
                p.rch = new_v
 
    def lower_bound(self, key):
        ret = None
        v = self.root
        while v is not None:
            if v.key >= key:
                if ret is None or ret > v.key:
                    ret = v.key
                v = v.lch
            else:
                v = v.rch
        return ret
 
    def upper_bound(self, key):
        ret = None
        v = self.root
        while v is not None:
            if v.key <= key:
                if ret is None or ret < v.key:
                    ret = v.key
                v = v.rch
            else:
                v = v.lch
        return ret
 
if __name__ == '__main__':
    N = int(input())
    P = [(p, i) for i, p in enumerate(map(int, input().split()))]
    P.sort()
 
    T = AVLTree()
    _, i = P.pop()
    T.add(i)
    T.add(-1)
    T.add(N)
 
    ans = 0
    while P:
        p, i = P.pop()
        l = T.upper_bound(i)
        r = T.lower_bound(i)
        ll = T.upper_bound(l-1)
        if ll is None:
            ll = -1
        rr = T.lower_bound(r+1)
        if rr is None:
            rr = N
        ans += p*((l-ll)*(r-i) + (rr-r)*(i-l))
        T.add(i)
    print(ans)
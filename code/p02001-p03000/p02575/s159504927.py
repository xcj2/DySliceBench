class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1<<n, 1<<n)

    def debug(self):
        def debug_info(nd_):
            return (nd_.value - 1, nd_.pivot , nd_.left.value - 1 if nd_.left else -1, nd_.right.value - 1 if nd_.right else -1,nd_.cnt)

        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re
        print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])

    def append(self, v):
        v += 1
        nd = self.root
        while True:
            if v == nd.value:
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p&-p)//2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p&-p)//2)
                        break

    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd

    def find_l(self, v):
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v):
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v: prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    @property
    def max(self):
        return self.find_l((1<<self.N)-1)

    @property
    def min(self):
        return self.find_r(-1)

    @property
    def sum(self):
        return self.root.sum-self.root.value+1

    @property
    def size(self):
        return self.root.cnt-1

    def delete(self, v, nd = None, prev = None):
        v += 1
        if not nd: nd = self.root
        if not prev: prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return
        if (not nd.left) and (not nd.right):
            if not prev.left:
                prev.right=None
            elif not prev.right:
                prev.left=None
            else:
                if nd.pivot==prev.left.pivot:
                    prev.left=None
                else:
                    prev.right=None
        elif nd.right:
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)
        else:
            nd.value = self.rightmost(nd.left).value
            self.delete(nd.value - 1, nd.left, nd)


    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None


import sys,heapq

input=sys.stdin.readline

H,W=map(int,input().split())
ban=[tuple(map(int,input().split())) for i in range(H)]

exist=[True for i in range(W+1)]

que=[(0,i) for i in range(1,W+1)]
heapq.heapify(que)

BT=BalancingTree(40)

for i in range(1,W+1):
    tmp=(i<<20)+i
    BT.append(tmp)


erase=set()
for i in range(H):
    a,b=ban[i]
    erasemax=(-1,-1)
    while True:
        val=BT.find_r(a<<20)
        pos=val>>20
        fr=val%(1<<20)
        if pos<=b:
            erasemax=max(erasemax,(fr,pos-fr))
            erase.add((pos-fr,fr))
            exist[fr]=False
            BT.delete(val)
        else:
            if pos>b+1 and erasemax[0]!=-1 and b+1<=W:
                BT.append(((b+1)<<20)+erasemax[0])
                deg=(erasemax[1],erasemax[0])
                erase.add(deg)
                heapq.heappush(que,(b+1-erasemax[0],erasemax[0]))
                exist[erasemax[0]]=True
            break

    while que and (not exist[que[0][1]] or que[0] in erase):
        heapq.heappop(que)

    if que:
        res = i+1+que[0][0]
        print(res)
    else:
        print(-1)
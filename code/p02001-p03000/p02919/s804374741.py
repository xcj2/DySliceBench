import sys
from bisect import bisect

class Node:
    def __init__(self, key, height):
        self.key = key #ノードの木
        self.height = height #このノードを根とする部分木の高さ
        self.left = None
        self.right = None

    def size(self, n): return 0 if n is None else n.height

    def bias(self): #左の方が高いと正、右が高いと負の値を返す
        return self.size(self.left) - self.size(self.right)

    #木の高さの計算
    def calcSize(self):
        self.height = 1 + max(self.size(self.left), self.size(self.right))

class AVLTree:
    def __init__(self):
        self.root = None #根
        self.change = False #修正フラグ

    ###############
    #回転操作, 修正操作
    ###############
    def rotateL(self, n): #ノードnの左回転
        r = n.right; rl = r.left
        r.left = n; n.right = rl
        r.left.calcSize()
        r.calcSize()
        return r

    def rotateR(self, n):
        l = n.left; lr = l.right
        l.right = n; n.left = lr
        l.right.calcSize()
        l.calcSize()
        return l

    def rotateLR(self, n): #二重回転;左回転→右回転
        n.left = self.rotateL(n.left)
        return self.rotateR(n)

    def rotateRL(self, n):
        n.right = self.rotateR(n.right)
        return self.rotateL(n)
        
    def balanceL(self, n):
        if not self.change: return n
        h = n.height
        if n.bias() == 2:
            if n.left.bias() >= 0: n = self.rotateR(n)
            else: n = self.rotateLR(n)
        else: n.calcSize()
        self.change = (h != n.height)
        return n

    def balanceR(self, n):
        if not self.change: return n
        h = n.height
        if n.bias() == -2:
            if n.right.bias() <= 0: n = self.rotateL(n)
            else: n = self.rotateRL(n)
        else: n.calcSize()
        self.change = (h != n.height)
        return n

    ###############
    #Nodeの追加
    ###############
    def insert(self, key): self.root = self.insert_sub(self.root, key)
    
    def insert_sub(self, t, key): #新たなノードの挿入。初期位置は根。
        if t is None:
            self.change = True
            return Node(key, 1)
        if key < t.key:
            t.left = self.insert_sub(t.left, key)
            return self.balanceL(t)
        elif key > t.key:
            t.right = self.insert_sub(t.right, key)
            return self.balanceR(t)
        else:
            self.change = False
            return t

    ###############
    #Nodeの探索
    ###############

    def search(self, key, leastValue, largestValue):
        t = self.root
        lb, hb = leastValue, largestValue
        while t:
            if key < t.key:
                hb = t.key
                t = t.left
            else:
                lb = t.key
                t = t.right
        return lb, hb

    def lower_bound(self, key, leastValue):
        t = self.root
        bound = leastValue
        while t:
            if key <= t.key: t = t.left
            else:
                bound = t.key
                t = t.right
        return bound 
 
    def upper_bound(self, key, largestValue):
        t = self.root
        bound = largestValue
        while t:
            if key < t.key:
                bound = t.key
                t = t.left
            else: t = t.right
        return bound

def solve():
    input = sys.stdin.readline
    N = int(input())
    P = [int(p) for p in input().split()]
    pindex = dict() 
    L, R = dict(), dict()
    for i, p in enumerate(P): pindex[p - 1] = i 
    Ans = 0
    T = AVLTree()
    T.insert(pindex[N-1])

    if N == 10 ** 5:
        for i in range(N-2, 0, -1):
            pid = pindex[i]
            left, right = T.lower_bound(pid, -1), T.upper_bound(pid, N)
            if left == -1: l2 = -1
            else: l2 = T.lower_bound(left, -1)
            if right == N: r2 = N
            else: r2 = T.upper_bound(right, N)
            Ans += (i + 1) * ((pid - left) * (r2 - right) + (right - pid) * (left - l2))
            T.insert(pid)
        Ans += (2 if 0 < pindex[0] < N - 1 else 1)

    else:
        L[pindex[N-1]] = -1
        R[pindex[N-1]] = N
        L[-1] = L[N] = -1
        R[-1] = R[N] = N    
        for i in reversed(range(N-1)):
            pid = pindex[i]
            L[pid], R[pid] = l, r = T.search(pid, -1, N)
            Ans += (i + 1) * ((pid - l) * (R[r] - r) + (r - pid) * (l - L[l]))
            T.insert(pid)
            R[l] = L[r] = pid

    print(Ans)

    return 0

if __name__ == "__main__":
    solve()

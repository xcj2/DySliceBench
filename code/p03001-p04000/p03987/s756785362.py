def examA():
    X = SI()
    d = defaultdict(int)
    for s in X:
        if s=="T" and d["S"]>=1:
            d["S"] -=1
        else:
            d[s] += 1
    ans = d["S"] + d["T"]
    print(ans)
    return

def examB():
    # 参考 earlgrey_yh
    class Node:
        def __init__(self, key, height):
            self.key = key  # ノードの木
            self.height = height  # このノードを根とする部分木の高さ
            self.left = None
            self.right = None

        def size(self, n): return 0 if n is None else n.height

        def bias(self):  # 左の方が高いと正、右が高いと負の値を返す
            return self.size(self.left) - self.size(self.right)

        # 木の高さの計算
        def calcSize(self):
            self.height = 1 + max(self.size(self.left), self.size(self.right))

    class AVLTree:
        def __init__(self):
            self.root = None  # 根
            self.change = False  # 修正フラグ

        ###############
        # 回転操作, 修正操作
        ###############
        def rotateL(self, n):  # ノードnの左回転
            r = n.right;
            rl = r.left
            r.left = n;
            n.right = rl
            r.left.calcSize()
            r.calcSize()
            return r

        def rotateR(self, n):
            l = n.left;
            lr = l.right
            l.right = n;
            n.left = lr
            l.right.calcSize()
            l.calcSize()
            return l

        def rotateLR(self, n):  # 二重回転;左回転→右回転
            n.left = self.rotateL(n.left)
            return self.rotateR(n)

        def rotateRL(self, n):
            n.right = self.rotateR(n.right)
            return self.rotateL(n)

        def balanceL(self, n):
            if not self.change: return n
            h = n.height
            if n.bias() == 2:
                if n.left.bias() >= 0:
                    n = self.rotateR(n)
                else:
                    n = self.rotateLR(n)
            else:
                n.calcSize()
            self.change = (h != n.height)
            return n

        def balanceR(self, n):
            if not self.change: return n
            h = n.height
            if n.bias() == -2:
                if n.right.bias() <= 0:
                    n = self.rotateL(n)
                else:
                    n = self.rotateRL(n)
            else:
                n.calcSize()
            self.change = (h != n.height)
            return n

        ###############
        # Nodeの追加
        ###############
        def insert(self, key):
            self.root = self.insert_sub(self.root, key)

        def insert_sub(self, t, key):  # 新たなノードの挿入。初期位置は根。
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
        # Nodeの探索
        ###############

        def search(self, key, lower, higher):
            t = self.root
            lb, hb = lower, higher
            while t:
                if key < t.key:
                    hb = t.key
                    t = t.left
                else:
                    lb = t.key
                    t = t.right
            return lb, hb
    N = I()
    A = LI()
    lst = [0] * N
    for i in range(N):
        lst[A[i]-1] = i
    AVL = AVLTree()
    ans = 0
    for a in range(1,N+1):
        i = lst[a-1]
        l, r = AVL.search(i,-1,N)
        AVL.insert(i)
        #print(l,r)
        ans += (i-l)*(r-i)*a
        #print(l,r,i,ans)
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math,random
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examB()

"""

"""
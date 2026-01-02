import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))


class AVL_like_BIT:  # 1-indexed
    def __init__(self,n):  # 1~nを要素として持ちうる。
        self.n = n
        self.tree = [0]*(self.n+1)
        self.depth = n.bit_length()

    def add(self,k):  # kを木に加える
        while k<=self.n:
            self.tree[k]+=1
            k += k&-k
    
    def delete(self,k): # kを木から削除する
        while k<=self.n:
            self.tree[k]-=1
            k += k&-k

    def sum(self,k):  # 1~kの和
        ans = 0
        while k>0:
            ans += self.tree[k]
            k -= k&-k
        return ans
    
    def lower_bound(self,k):  # k以上の最小要素
        x = self.sum(k-1)
        if x == self.sum(self.n):  # k以上の要素がないときは-1を返す
            return -1
        p = 0
        v = 1<<self.depth
        for i in range(self.depth + 1):  # sum(p) = sum(k-1)なるpの右端 + 1が答え
            q = p+v
            if q <= self.n and self.tree[q] <= x:
                x -= self.tree[q]
                p += v
            v>>=1
        return p+1

    def upper_bound(self,k):  # k以下の最大要素
        x = self.sum(k)
        if x == 0:  # k以下の要素がないときは-1を返す
            return -1
        p = 0
        v = 1<<self.depth
        for i in range(self.depth + 1):  # sum(p) = sum(k)なるpの左端が答え
            q = p+v
            if q <= self.n and self.tree[q] < x:
                x -= self.tree[q]
                p += v
            v>>=1
        return p+1

    def query(self,k):  # k番目の要素出力
        if k > self.sum(self.n):  # k個以上の要素がないときは-1を返す
            return -1
        p = 0
        v = 1<<self.depth
        for i in range(self.depth + 1):  # sum(p) = kなるpの左端が答え
            q = p+v
            if q <= self.n and self.tree[q] < k:
                k -= self.tree[q]
                p += v
            v>>=1
        return p+1

def compress(a):
    b = sorted(set(a))
    d = {x:i+1 for i,x in enumerate(b)}
    return b,d


import heapq

n,q = readints()

X = []

block = []
free = []
for i in range(n):
    s,t,x = readints()
    X.append(x)
    block.append([s-x,x])
    free.append([t-x,x])

b,d = compress(X)
block = [(x[0],d[x[1]]) for x in block]
free = [(x[0],d[x[1]]) for x in free]
heapq.heapify(block)
heapq.heapify(free)

ans = []
avl = AVL_like_BIT(len(d))
for i in range(q):
    D = readint()
    while block and block[0][0]<=D:
        a = heapq.heappop(block)
        avl.add(a[1])
    while free and free[0][0]<=D:
        a = heapq.heappop(free)
        avl.delete(a[1])
    ans.append(avl.lower_bound(0))

ans = [b[x-1] if x >=0 else -1 for x in ans]
printrows(ans)

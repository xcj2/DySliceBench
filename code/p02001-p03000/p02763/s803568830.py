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

a = ord('a')

n = readint()
s = [0] + [ord(x)-a for x in readstr()]
q = readint()

avl = [AVL_like_BIT(5*10**5 + 10) for i in range(26)]
for i in range(1,n+1):
    avl[s[i]].add(i)

ans = []
for i in range(q):
    j,l,r = readstrs()
    j = int(j)
    l = int(l)
    if j==1:
        avl[s[l]].delete(l)
        s[l] = ord(r)-a
        avl[s[l]].add(l)
    else:
        r = int(r)
        ans.append(0)
        for k in range(26):
            if avl[k].sum(l-1)-avl[k].sum(r):
                ans[-1]+=1

printrows(ans)







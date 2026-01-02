"""

普通に端っこを基準にして、貪欲的に爆弾をおいていく方法を考えるのがよさそう。
座標圧縮したうえで、遅延セグ木で各座標に蓄積しているダメージを管理しておけばよい。
一番左端のやつの体力を削れるだけの爆弾を設置してみる:O(1)
次の左端になるモンスターの位置(体力が1以上あるモンスターのなかで一番左端のやつの座標)を探す。これはO(logN)かかる。
このサイクルをモンスターが全滅するまで行うので、O(N)サイクル回す。したがって全体でO(NlogN)
"""
from math import ceil
class lazySegTree:
    def __init__(self,n):
        self.end_leave = 2**(n.bit_length()+1)
        self.tree = [0]*(2*self.end_leave)
        self.lazy = [0]*(2*self.end_leave)

    def gindex(self,left,right):
        #leftとrightの真上にあるノードを返す
        left = left + self.end_leave
        right = right + self.end_leave
        left >>= 1
        while left:
            yield left
            left >>= 1

        right >>= 1
        while right:
            yield right
            right >>= 1

    def add(self,left,right,x):
        L = left + self.end_leave
        R = right + self.end_leave
        while L < R:
            if L&1:
                self.lazy[L] += x
                self.tree[L] += x
                L += 1
            if R&1:
                R -= 1
                self.lazy[R] += x
                self.tree[R] += x
            L >>= 1
            R >>= 1
        for i in self.gindex(left,right):
            self.tree[i] = max(self.tree[i*2],self.tree[i*2+1])+self.lazy[i]
    
    def propagates(self,*ids):
        for i in reversed(ids):
            self.lazy[i*2] += self.lazy[i]
            self.lazy[i*2+1] += self.lazy[i]
            self.tree[i*2] += self.lazy[i]
            self.tree[i*2+1] += self.lazy[i]
            self.lazy[i] = 0

    def get(self,left,right):
        self.propagates(*self.gindex(left,right))
        L = left + self.end_leave
        R = right + self.end_leave
        res = 0
        while L < R:
            if L&1:
                res = max(res,self.tree[L])
                L += 1
            if R&1:
                R -= 1
                res = max(res,self.tree[R])
            L >>= 1
            R >>= 1
        return res
N,D,A = map(int,input().split())
XH = [list(map(int,input().split())) for _ in range(N)]
XH.sort()
compSet = []
for x,h in XH:
    compSet.append(x)
    compSet.append(x+2*D)
compSet.sort()
compSet = sorted(set(compSet))
compDic = {x:i for i,x in enumerate(compSet)}

LST = lazySegTree(len(compDic))
ans = 0
for x,h in XH:
    compX = compDic[x]
    h -= LST.get(compX,compX+1)
    if h > 0:
        bomb = ceil(h/A)
        ans += bomb
        damage = bomb*A
        compRight = compDic[x+2*D]
        LST.add(compX,compRight+1,damage)
print(ans)


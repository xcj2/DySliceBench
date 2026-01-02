import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    class Segtree:
        def __init__(self, A, ide_ele, initialize = True, segf = max):
            self.N = len(A)
            self.N0 = 2**(self.N-1).bit_length()
            self.ide_ele = ide_ele
            self.segf = segf
            if initialize:
                self.data = [ide_ele]*self.N0 + A + [ide_ele]*(self.N0 - self.N)
                for i in range(self.N0-1, 0, -1):
                    self.data[i] = self.segf(self.data[2*i], self.data[2*i+1]) 
            else:
                self.data = [ide_ele]*(2*self.N0)

        def update(self, k, x):
            k += self.N0
            self.data[k] = x
            while k > 0 :
                k = k >> 1
                self.data[k] = self.segf(self.data[2*k], self.data[2*k+1])

        def query(self, l, r):
            L, R = l+self.N0, r+self.N0
            s = self.ide_ele
            t = self.ide_ele
            while L < R:
                if L & 1:
                    s = self.segf(s,self.data[L])
                    L += 1
                if R & 1:
                    R -= 1
                    t = self.segf(self.data[R],t)
                L >>= 1
                R >>= 1
            return self.segf(s,t)

        # セグ木上で二分探索，[l,r)の範囲でcheck関数を満たす最小の値をとるところのindexを返す．
        # reverse=Trueなら最大値かな
        # ない時の返り値がNoneなことに注意
        def binsearch(self, l, r, check, reverse = False):
            L, R = l+self.N0, r+self.N0
            SL, SR = [], []
            while L < R:
                if R & 1:
                    R -= 1
                    SR.append(R)
                if L & 1:
                    SL.append(L)
                    L += 1
                L >>= 1
                R >>= 1

            if reverse:
                pre = self.ide_ele
                for idx in (SR + SL[::-1]):
                    if check(self.segf(self.data[idx], pre)):
                        break
                    else:
                        pre = self.segf(self.data[idx], pre)
                else:
                    return None
                while idx < self.N0:
                    if check(self.segf(self.data[2*idx+1], pre)):
                        idx = 2*idx + 1
                    else:
                        pre = self.segf(self.data[2*idx+1], pre)
                        idx = 2*idx
                return idx - self.N0
            else:
                pre = self.ide_ele
                for idx in (SL + SR[::-1]):
                    if not check(self.segf(pre, self.data[idx])):
                        pre = self.segf(pre, self.data[idx])
                    else:
                        break
                else:
                    return None
                while idx < self.N0:
                    if check(self.segf(pre, self.data[2*idx])):
                        idx = 2*idx
                    else:
                        pre = self.segf(pre, self.data[2*idx])
                        idx = 2*idx + 1
                return idx - self.N0

    class UnionFind:
        def __init__(self, N: int):
            """
            N:要素数
            root:各要素の親要素の番号を格納するリスト.
                 ただし, root[x] < 0 ならその頂点が根で-root[x]が木の要素数.
            rank:ランク
            """
            self.N = N
            self.root = [-1] * N
            self.rank = [0] * N

        def __repr__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

        def find(self, x: int):
            """頂点xの根を見つける"""
            if self.root[x] < 0:
                return x
            else:
                while self.root[x] >= 0:
                    x = self.root[x]
                return x

        def union(self, x: int, y: int):
            """x,yが属する木をunion"""
            # 根を比較する
            # すでに同じ木に属していた場合は何もしない.
            # 違う木に属していた場合はrankを見てくっつける方を決める.
            # rankが同じ時はrankを1増やす
            x = self.find(x)
            y = self.find(y)
            if x == y:
                return
            elif self.rank[x] > self.rank[y]:
                self.root[x] += self.root[y]
                self.root[y] = x
            else:
                self.root[y] += self.root[x]
                self.root[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

        def same(self, x: int, y: int):
            """xとyが同じグループに属するかどうか"""
            return self.find(x) == self.find(y)

        def count(self, x):
            """頂点xが属する木のサイズを返す"""
            return - self.root[self.find(x)]

        def members(self, x):
            """xが属する木の要素を列挙"""
            _root = self.find(x)
            return [i for i in range(self.N) if self.find == _root]

        def roots(self):
            """森の根を列挙"""
            return [i for i, x in enumerate(self.root) if x < 0]

        def group_count(self):
            """連結成分の数"""
            return len(self.roots())

        def all_group_members(self):
            """{ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す"""
            return {r: self.members(r) for r in self.roots()}
    
    N=I()
    X=[0]*N
    Y=[0]*N
    
    from collections import defaultdict
    dd = defaultdict(int)# y2i
    X2Y = defaultdict(int)
    
    for i in range(N):
        X[i],Y[i]=MI()
        X[i]-=1
        Y[i]-=1
        
        X2Y[X[i]]=Y[i]
        dd[Y[i]]=i
        
    X.sort()
    uf=UnionFind(N)
    
    inf = 10**7
    seg=Segtree([-1]*N,-100,segf=max)
    seg2=Segtree([inf]*N,inf,segf=min)
    
    # xを小さい順に並べておけば既出のものは必ずx座標が小さい．結べるものの中でy座標が最大のものと繋いでおく，最小のものも繋いでおくか
    for i in range(N):
        y=X2Y[X[i]]
        k=dd[y]
        yM=seg.query(0,y)
        kM=dd[yM]  
        if yM>=0:#あれば
            uf.union(k,kM)
            
        ym=seg2.query(0,y)
        km=dd[ym]
        if ym<inf:
            uf.union(k,km)
        
        seg.update(y,y)
        seg2.update(y,y)
        
    # 逆向きに見る
    seg=Segtree([-1]*N,-100,segf=max)
    seg2=Segtree([inf]*N,inf,segf=min)
    for i in range(N-1,-1,-1):
        y=X2Y[X[i]]
        k=dd[y]
        yM=seg.query(y,N)
        kM=dd[yM]  
        if yM>=0:#あれば
            uf.union(k,kM)
            
        ym=seg2.query(y,N)
        km=dd[ym]
        if ym<inf:
            uf.union(k,km)

        seg.update(y,y)
        seg2.update(y,y)
        
    roots=[0]*N
    for i in range(N):
        y=X2Y[X[i]]
        k=dd[y]
        roots[k]=uf.find(k)
        
    ddr = defaultdict(lambda:-1)
        
    for i in range(N):
        root=roots[i]
        if ddr[root]!=-1:
            print(ddr[root])
        else:
            ans=uf.count(root)
            print(ans)
            ddr[root]=ans
        
        
        
    
    

main()

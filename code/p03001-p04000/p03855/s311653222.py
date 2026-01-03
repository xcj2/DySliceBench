#unionfind
class UF:
    def __init__(self, n):
        # 負  : 根であることを示す。絶対値はランクを示す
        # 非負: 根でないことを示す。値は親を示す
        self.table = [-1] * n
    def _root(self, x):
        if self.table[x] < 0:
            return x
        else:
            # 経路の圧縮
            self.table[x] = self._root(self.table[x])
            return self.table[x]
    def find(self, x, y):
        return self._root(x) == self._root(y)
    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        # ランクの取得
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2
    def show(self):
        print(self.table)
    def data(self):
        res={}
        n=len(self.table)
        for i in range(n):
            res.update({i:[i] if self.table[i]<0 else [self.table[i]]})
        for i in range(n):
            res[res[i][0]]+=[i]
        for i in range(n):
            if len(res[i])==1:
                del res[i]
            else:
                del res[i][0]
        return list(res.values())

n,k,l=map(int,input().split())
pq=[list(map(int,input().split())) for _ in range(k)]
rs=[list(map(int,input().split())) for _ in range(l)]
auf=UF(n)
buf=UF(n)
for p,q in pq:
    auf.union(p-1,q-1)
for r,s in rs:
    buf.union(r-1,s-1)
key_list=[]
from collections import defaultdict
count=defaultdict(int)
for i in range(n):
    key=(auf._root(i),buf._root(i))
    key_list.append(key)
    count[key]+=1
ans=[0 for _ in range(n)]
for i,key in enumerate(key_list):
    ans[i]=str(count[key])
print(" ".join(ans))
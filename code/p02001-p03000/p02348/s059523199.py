
class LazySegTree:
    inf = 2147483647
    INF = [-1,2147483647]
    def __init__(self,n_):
        self.n_ = n_
        self.n = 1
        while self.n < n_: self.n*=2
        self.st = [self.INF]*(2*self.n-1)
        self.lazy = [self.INF]*(2*self.n-1)

    def propagate(self,k):
        if self.lazy[k]==self.INF:return
        self.st[k] = self.lazy[k][1]
        if k<self.n_-1:
            self.lazy[k*2+1] = self.lazy[k]
            self.lazy[k*2+2] = self.lazy[k]
        self.lazy[k] = self.INF
    
    def update(self,a,b,k,x,l,r):
        #self.propagate(k)
        if r<=a or b<=l :return
        if a<=l and r<=b:
            self.st[k] = x
            self.lazy[k] = x
            return
        self.update(a,b,k*2+1,x,l,(l+r)//2)
        self.update(a,b,k*2+2,x,(l+r)//2,r)

    def Update(self,a,b,x):
        return self.update(a,b,0,x,0,self.n)

    def search(self,k,l,r):
        #self.propagate(k)
        k += self.n-1
        res = self.INF
        while 0<=k:
            res = max(res,self.lazy[k])
            k = (k-1)//2
        return res[1]

    def Search(self,k):
        return self.search(k,0,self.n)

def main():
    n,m = map(int,input().split())
    lst = LazySegTree(n)
    for i in range(m):
        q = list(map(int,input().split()))
        if q[0] == 0:
            lst.Update(q[1],q[2]+1,[i,q[3]])
        else        :print(lst.Search(q[1]))

if __name__ == '__main__':
    main()




class RMQ:
    inf = 2147483647
    def __init__(self,n_):
        self.n_ = n_
        self.n = 1
        while self.n < n_: self.n*=2
        self.st = [self.inf]*(2*self.n-1)
    
    def update(self,k,x):
        k+=(self.n-1)
        self.st[k] = x
        while k >0:
            k = (k-1)//2
            self.st[k] = min(self.st[2*k+1],self.st[2*k+2])

    def search(self,a,b,k,l,r):
        if r<=a or b<=l :return self.inf
        if a<=l and r<=b:return self.st[k]
        L = self.search(a,b,k*2+1,l,(l+r)//2)
        R = self.search(a,b,k*2+2,(l+r)//2,r)
        return min(L,R)

    def query(self,a,b):
        return self.search(a,b,0,0,self.n)

def main():
    n,q = map(int,input().split())
    ST = RMQ(n)
    for _ in range(q):
        a,b,c = map(int,input().split())
        if a == 0:ST.update(b,c)
        else     :print (ST.query(b,c+1))

if __name__ == '__main__':
    main()



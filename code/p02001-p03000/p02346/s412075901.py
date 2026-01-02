class RSQ:
    def __init__(self,n_):
        self.n_ = n_
        self.n = 1
        while self.n < n_: self.n*=2
        self.st = [0]*(2*self.n-1)
    
    def update(self,k,x):
        k+=(self.n-1)
        self.st[k] += x
        while k >0:
            k = (k-1)//2
            self.st[k] = self.st[2*k+1]+self.st[2*k+2]

    def search(self,a,b,k,l,r):
        if r<=a or b<=l :return 0
        if a<=l and r<=b:return self.st[k]
        L = self.search(a,b,k*2+1,l,(l+r)//2)
        R = self.search(a,b,k*2+2,(l+r)//2,r)
        return L+R

    def query(self,a,b):
        return self.search(a,b,0,0,self.n)

def main():
    n,q = map(int,input().split())
    ST = RSQ(n)
    for _ in range(q):
        a,b,c = map(int,input().split())
        if a == 0:ST.update(b-1,c)
        else     :print (ST.query(b-1,c))

if __name__ == '__main__':
    main()






class dset:
    def __init__(self,n):
        self.par = [-1]*n

    def size(self,n):
        return -self.par[self.root(n)]

    def root(self,n):
        if self.par[n]<0:
            return n
        else:
            self.par[n] = self.root(self.par[n])
            return self.par[n]

    def same(self, a, b):
        return self.root(a) == self.root(b)

    def __link__(self,a,b):
        if a == b:
            return 
        
        if self.size(a) < self.size(b):
            a,b = b,a
        
        self.par[a] += self.par[b]
        self.par[b] = a

    def unite(self,a,b):
        self.__link__(
            self.root(a)
            ,self.root(b)
            )


def main():
    n, m = map(int, input().split() ) 


    ins = [ list( map(int,input().split()) ) for i in range(m)  ]

    ds = dset(n)

    ans = [0]*m
    ans[-1] = n*(n-1)//2
    for i in range(m-1,0,-1):
        ans[i-1] = ans[i]

        a,b = ins[i]
        a-=1
        b-=1

#        print(ins[i])
       # print( (ds.root(a),ds.root(b)) ) 
        if not ds.same(a,b):
            x = ds.size(a)
            y = ds.size(b)
            #print((x,y))
            ans[i-1] -= x*y
            ds.unite(a,b)

    for e in ans:
        print(e)

if __name__ == '__main__':
    main()
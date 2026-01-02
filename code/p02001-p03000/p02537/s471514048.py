class SegmentTree:
    def __init__(self, L, op, ide):
        self.op = op
        self.ide = ide
        self.sz = len(L)
        self.n = 1
        self.s = 1
        for i in range(1000):
            self.n *= 2
            self.s += 1
            if self.n >= self.sz:
                break
        self.node = [self.ide]*(2*self.n-1)

        for i in range(self.sz):
            self.node[i+self.n-1] = L[i]

        for i in range(self.n-2,-1,-1):
            self.node[i] = self.op(self.node[i*2+1],self.node[i*2+2])
    
    def add(self, a, x):
        k = a+self.n-1
        self.node[k] += x
        for i in range(1000):
            k = (k-1)//2
            self.node[k] = self.op(self.node[2*k+1], self.node[2*k+2])
            if k <= 0:
                break
    
    def substitute(self, a, x):
        k = a+self.n-1
        self.node[k] = x
        for i in range(1000):
            k = (k-1)//2
            self.node[k] = self.op(self.node[2*k+1], self.node[2*k+2])
            if k <= 0:
                break

    def get_one(self, a):
        k = a+self.n-1
        return self.node[k]
    
    def get(self, l, r):
        res = self.ide
        n = self.n
        if self.sz <= r or 0 > l:
            print()
            return False

        for i in range(self.s):
            count = 2**i-1
            a = (r+1)//n
            b = (l-1)//n
            if a-b == 3:
                res = self.op(self.node[count+b+1],res)
                res = self.op(self.node[count+b+2],res)
                right = a*n
                left = (b+1)*n-1
                break
            if a-b == 2:
                res = self.op(self.node[count+b+1],res)
                right = a*n
                left = (b+1)*n-1
                break
            n = n//2

        #left
        n1 = n//2        
        for j in range(i+1,self.s):
            count = 2**j-1 
            a = (left+1)//n1
            b = (l-1)//n1
            if a-b == 2:
                res = self.op(self.node[count+b+1],res)
                left = (b+1)*n1-1                
            n1 = n1//2

        #right
        n1 = n//2        
        for j in range(i+1,self.s):
            count = 2**j-1 
            a = (r+1)//n1
            b = (right-1)//n1
            if a-b == 2:
                res = self.op(self.node[count+b+1],res)
                right = a*n1                
            n1 = n1//2
        return res
    
import sys

sys.setrecursionlimit(500000)
def input():
    return sys.stdin.readline()[:-1]


def smax(a,b):
    if a>b:
        return a
    else:
        return b

def smin(a,b):
    if a>b:
        return b
    else:
        return a


def main():
    N,K = list(map(int,input().split()))

    A = [int(input()) for i in range(N)]
    maxA = max(A)
    from collections import defaultdict

    ST1 = SegmentTree([0]*(maxA+1), smax, 0)

    D1 = [0]*N
    for i in range(N):
        a = A[i]
        b = ST1.get(smax(a-K,0),smin(a+K,maxA))
        c = ST1.get_one(a)
        d = smax(b+1,c)
        D1[i] = d
        ST1.substitute(a,d)

    ST2 = SegmentTree([0]*(maxA+1), smax, 0)

    D2 = [0]*N
    for i in range(N):
        a = A[N-i-1]
        b = ST2.get(smax(a-K,0),smin(a+K,maxA))
        c = ST2.get_one(a)
        d = smax(b+1,c)
        D2[N-i-1] = d
        ST2.substitute(a,d)

    D3 = [D1[i]+D2[i]-1 for i in range(N)]

    print(max(D3))

if __name__ == '__main__':
    main()



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

        #for i in range(self.sz):
        #    self.node[i+self.n-1] = L[i]

        #for i in range(self.n-2,-1,-1):
        #    self.node[i] = self.op(self.node[i*2+1],self.node[i*2+2])
    
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
            print('ERROR: the indice are wrong.')
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
from operator import itemgetter
sys.setrecursionlimit(500000)
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    def max_func(a,b):
        if a>b:
            return a
        else:
            return b
    ST = SegmentTree([0]*N,max_func,0)

    M = [list(map(int,input().split())) for i in range(N)]

    M.sort(key=itemgetter(0))

    def bisect(l,v):
        r = N-1
        if M[r][0] < v:
            return r
        while r-l>1:
            if M[(r+l)//2][0]<v:
                l = (r+l)//2
            else:
                r = (r+l)//2
        return l


    for i in range(N):
        j = N-i-1
        index = bisect(j,M[j][0]+M[j][1])
        if N-index-1 < i:
            ST.substitute(j,ST.get(j,index))
        else:
            ST.substitute(j,j)
            

    DP = [0]*(N+1)
    DP[0] = 1
    mod = 998244353
    #print(M)
    for i in range(N):
        #print(DP)
        index = ST.get_one(N-i-1)
        j = N-1-index
        DP[i+1] = (DP[j]+DP[i])%mod

    print(DP[N])

if __name__ == '__main__':
    main()


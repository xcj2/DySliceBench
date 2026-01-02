MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

class SegmentTree():
    def __init__(self,array,func,unit):
        self.N = len(array)
        self.f = func
        self.unit = unit
        self.tree = [self.unit] * (2*self.N)
        for i,x in enumerate(array,self.N):
            self.tree[i] = x
        for i in range(self.N - 1,0,-1):
            self.tree[i] = self.f(self.tree[i << 1],self.tree[i << 1|1])
    
    def update(self,k,x):
        k += self.N
        self.tree[k] = x
        while k > 1:
            k >>= 1
            self.tree[k] = self.f(self.tree[k << 1],self.tree[k << 1|1])
    
    def query(self,l,r):
        l += self.N
        r += self.N
        vl = self.unit
        vr = self.unit
        while l < r:
            if l&1: 
                vl = self.f(vl,self.tree[l])
                l += 1
            if r&1:
                r -= 1
                vr = self.f(self.tree[r],vr)
            l >>= 1
            r >>= 1
        return self.f(vl,vr)

def main():
    n,q = map(int,input().split())
    st = SegmentTree([(1<<31) - 1]*n,min,1<<32)

    for _ in range(q):
        query = list(map(int,input().split()))
        if query[0] == 0:
            i = query[1]
            x = query[2]
            st.update(i,x)
        else:
            s = query[1]
            t = query[2]
            print(st.query(s,t + 1))
if __name__ == '__main__':
    main()

import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
MOD = 10 ** 9 + 7


class SegmentTree():
    f = max
    unit = 0
   
    def __init__(self,array):
        self.N = len(array)
        self.tree = [self.unit] * (2*self.N)
        #self._build(array)
    
    def _build(self,array):
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
    
    def __str__(self):
        return '\n'.join(' '.join(str(v) for v in self.tree[1<<i:1<<(i + 1)]) for i in range((2*self.N).bit_length()))

def main():
    N = int(input())
    H = list(map(int,input().split()))
    A = list(map(int,input().split()))

    st = SegmentTree([0] * N)
    ans = 0
    for i in range(N):
        a = st.query(0,H[i] - 1)
        ans = max(ans,a + A[i])
        st.update(H[i] - 1,a + A[i])
    print(ans)
if __name__ == '__main__':
    main()
    

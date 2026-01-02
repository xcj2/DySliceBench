class SegTreeSum:
    '''
    0-indexedで実装していることに注意
    '''

    def __init__(self, V):
        self.sz = len(V)
        N = 1
        while N < self.sz:
            N *= 2

        self.N = N
        self.node = [0] * (2 * self.N - 1)
        
        for i in range(self.sz):
            self.node[i + self.N - 1] = V[i]
        
        for i in range(self.N - 2, 0, -1):
            # 親から子ノードへアクセスする
            self.node[i] = self.node[2*i+1] + self.node[2*i+2]
    
    def add(self,i,x):
        i += (self.N - 1)
        self.node[i] += x

        while i > 0:
            i = (i - 1) // 2
            self.node[i] = self.node[2*i+1] + self.node[2*i+2]

    def getsum(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.N
        
        if b <= l or a >= r:
            return 0
        
        if a <= l and b >= r:
            return self.node[k]

        vl = self.getsum(a,b, 2*k+1, l, (l+r)//2)
        vr = self.getsum(a,b, 2*k+2, (l+r)//2, r)
        return vl + vr

def main():
    n,q = map(int, input().split())
    V = [0] * n
    seg = SegTreeSum(V)
    for _ in range(q):
        com, x, y = map(int, input().split())
        x -= 1
        if com:
            print(seg.getsum(x,y))
        else:
            seg.add(x,y)

if __name__ == "__main__":
    main()


class BIT: #0-indexed
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
        self.depth = n.bit_length()
        self.n0 = 1<<self.depth
#        self.element = [0]*(n+1)
    def get_sum(self, i): #a_0 + ... + a_{i} #閉区間
        s = 0; i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def query(self,l,r): #a_l + ... + a_r 閉区間
        return self.get_sum(r) - self.get_sum(l-1) 
    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
        # self.element[i] += x
    #def get(self,i): return element[i]        
    def bisect_left(self,w):
        #和が w 以上になる最小の index
        #w が存在しない場合 self.size を返す
        if w <= 0: return 0
        x,k = 0,self.n0
        for _ in range(self.depth):
            k >>= 1
            if x+k <= self.size and self.tree[x+k] < w:
                w -= self.tree[x+k]
                x += k
        return x
    
###########################################
import sys
readline = sys.stdin.readline

n,q = map(int, readline().split())
*a, = map(int, readline().split())

b = BIT(n)
for i in range(n):
    b.add(i,a[i])

for _ in range(q):
    v,p,x = map(int, readline().split())
    if v==0:
        b.add(p,x)
    else:
        print(b.query(p,x-1))





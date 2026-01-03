def sgn(n):
    if n>0:
        return 1
    elif n==0:
        return 0
    else:
        return -1
    
class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2-1) # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size-1
        self.dat[i] = x
        while i > 0:
            i = (i-1) >> 1
            self.dat[i] = self.f(self.dat[i*2+1], self.dat[i*2+2])

    def query(self, l, r, k=0, L=0, R=None):
        if R is None:
            R = self.size
        if R <= l or r <= L:
            return self.default
        if l <= L and R <= r:
            return self.dat[k]
        else:
            lres = self.query(l, r, k*2+1, L, (L+R) >> 1)
            rres = self.query(l, r, k*2+2, (L+R) >> 1, R)
            return self.f(lres, rres)
        
n=int(input())
b=[int(i) for i in input().split()]
l = SegmentTree(size=n)
p0=0
for i in range(n):
    l.update(i,b[i])
for i in range(n):
    sg=(-1)**(i)
    v=l.query(0,i+1)
    #print(v,p0)
    if sgn(v) != sg:
        tmp= abs(v)+1
        #print(f'{b[i]}---{tmp}--->{sg}')
        p0 += tmp
        l.update(i,b[i]+tmp*sg)
        
l = SegmentTree(size=n)
for i in range(n):
    l.update(i,b[i])
p1=0
#print()
for i in range(n):
    sg=(-1)**(i+1)
    v=l.query(0,i+1)
    #print(v,p1)
    if sgn(v) != sg:
        tmp= abs(v)+1
        #print(f'{b[i]}---{tmp}--->{sg}')
        p1 += tmp
        l.update(i,b[i]+tmp*sg)
    #print(l.query(0,i+1),p1)
print(min(p0,p1))
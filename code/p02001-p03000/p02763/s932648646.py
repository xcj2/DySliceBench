class SegmentTree:
    def __init__(self,siz,v = 0):
        self.n = 1
        self.v = v
        while self.n < siz: self.n *= 2
        self.node = [self.v]*(2*self.n-1)

    def merge(self,x,y): return x | y

    def update(self,i,x):
        i += self.n-1
        self.node[i] = x
        while i > 0:
            i = (i-1)//2
            self.node[i] = self.merge(self.node[i*2+1],self.node[i*2+2])
    
    def query(self,a,b):
        vl = vr = self.v
        a += self.n-1
        b += self.n-1
        while a < b:
            if a & 1 == 0: vl = self.merge(vl,self.node[a])
            if b & 1 == 0: vr = self.merge(vr,self.node[b-1])
            a //= 2
            b = (b-1)//2
        return self.merge(vl,vr)
    
n = int(input())
st = SegmentTree(n)
s = list(input())
def f(c): return 1<<(ord(c) - ord("a"))
for i in range(n): st.update(i,f(s[i]))
q = int(input())
for _ in range(q):
    typ,x,y = input().split()
    if typ == "1":
        i,c = int(x)-1,y
        if s[i] == c: continue
        st.update(i,f(c))
        s[i] = c
    else:
        l,r = int(x)-1,int(y)
        print(bin(st.query(l,r)).count("1"))
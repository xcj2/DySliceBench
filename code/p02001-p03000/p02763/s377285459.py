import sys
read=sys.stdin.readline
class SEGTree:
    def __init__(self,n):
        self.Unit=0
        i=1
        while(i<n):
            i*=2
        self.SEG=[self.Unit]*(2*i-1)
        self.d=i
    def update(self,i,x):
        i+=self.d-1
        self.SEG[i]=1<<x
        while i>0:
            i=(i-1)//2
            self.SEG[i]=self.SEG[i*2+1]|self.SEG[i*2+2]
    def find(self,a,b,k,l,r):
        if r<=a or b<=l:
            return self.Unit
        if a<=l and r<=b:
            return self.SEG[k]
        else:
            c1=self.find(a,b,2*k+1,l,(l+r)//2)
            c2=self.find(a,b,2*k+2,(l+r)//2,r)
            return c1|c2
    def get(self,a,b):
        return self.find(a,b,0,0,self.d)
def bitcnt(x):
    res=0
    while x>0:
        if x&1:
            res+=1
        x//=2
    return res

n=int(input())
s=input()
q=int(input())
seg=SEGTree(n)
for i in range(n):
    seg.update(i,ord(s[i])-97)
for i in range(q):
    q,x,y=read().rstrip().split()
    if q=='1':
        seg.update(int(x)-1,ord(y)-97)
    else:
        x,y=int(x)-1,int(y)
        bit=seg.get(x,y)
        print(bitcnt(bit))
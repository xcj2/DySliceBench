import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class SegTree:
    def __init__(self,aa):
        n=1<<(len(aa)-1).bit_length()
        tree=[0]*(2*n-1)
        tree[n-1:n-1+len(aa)]=aa
        for i in range(n-2,-1,-1):tree[i]=tree[2*i+1]|tree[2*i+2]
        self.tree=tree
        self.n=n

    def update(self,i,a):
        i=self.n-1+i
        self.tree[i]=a
        while i:
            i=(i-1)//2
            self.tree[i]=self.tree[2*i+1]|self.tree[2*i+2]

    def SegOr(self,l,r,i=0,segl=0,segr=-1):
        if segr==-1:segr=self.n
        if r<=segl or segr<=l:return 0
        if l<=segl and segr<=r:return self.tree[i]
        m=(segl+segr)//2
        return self.SegOr(l,r,2*i+1,segl,m)|self.SegOr(l,r,2*i+2,m,segr)

def main():
    code=lambda c:ord(c)-ord("a")
    popcnt=lambda x:bin(x).count("1")
    n=II()
    s=SI()
    aa=[1<<code(c) for c in s]
    st=SegTree(aa)
    q=II()
    for _ in range(q):
        op,x,y=SI().split()
        if op=="1":
            i=int(x)-1
            st.update(i,1<<code(y))
        else:
            l,r=int(x)-1,int(y)
            print(popcnt(st.SegOr(l,r)))

main()
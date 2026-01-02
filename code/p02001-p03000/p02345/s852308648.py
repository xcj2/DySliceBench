from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

class SegmentTree:
    def __init__(self,N,d):
        self.NN = 1
        while self.NN < N:
            self.NN *= 2
        self.SegTree = [d]*(self.NN*2-1)

    def update(self,i,x): #iの値をxに更新
        i += self.NN - 1
        self.SegTree[i] = x
        while i>0:
            i = (i-1)//2
            self.SegTree[i] = self.process(self.SegTree[i*2+1],self.SegTree[i*2+2])

    def query(self,a,b,k=0,l=0,r=None): #[A,B)の値, 呼ぶときはquery(a,b)
        if r == None: r = self.NN
        if r <= a or b <= l: #完全に含まない
            return INF
        elif a <= l and r <= b : #完全に含む
            return self.SegTree[k]
        else: #交差する
            vl = self.query(a,b,k*2+1,l,(l+r)//2)
            vr = self.query(a,b,k*2+2,(l+r)//2,r)
            return(self.process(vl,vr))

    def process(self,x,y): #x,yが子の時，親に返る値
        return min(x,y)


N,Q = inpl()
ST = SegmentTree(N,2**31-1)

for _ in range(Q):
    c,x,y = inpl()
    if c == 0:
        ST.update(x,y)
    else:
        print(ST.query(x,y+1))


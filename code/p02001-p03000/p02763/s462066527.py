class SegmentTree():
    def __init__(self,n):
        self.e = 0
        self.r = 0 #ノードの段数
        cnt = 0
        while cnt<n:
            cnt=2**self.r
            self.r +=1
        self.tree = [self.e]*(2**self.r -1)# 0-index
        self.n = 2**(self.r-1) #一番下のnodeの数
    def func(self,a,b): #適宜書き換え
        return a|b
    def update(self,i,val):
        i += self.n -1
        self.tree[i] = val
        while i>0:
            i = (i-1)//2
            self.tree[i] = self.func(self.tree[i*2+1],self.tree[i*2+2])

    def query(self,l,r):
        l += self.n -1
        r += self.n -1 #開区間 idxはr-1
        lval = self.e
        rval = self.e
        while r>l:
            if l%2 == 0:
                lval = self.func(lval,self.tree[l])
                l+=1
            if r%2==0:
                rval = self.func(rval,self.tree[r-1])
                r-=1
            r//=2
            l//=2
        return self.func(lval,rval)
    def index(self,i):
        return i+self.n -1
def sid(s):
    return ord(s)-ord("a") #chr("a") == 0

import sys
input = sys.stdin.readline
n = int(input())
S = input()[:-1]
Q = int(input())
seg = SegmentTree(n)
for i in range(n):
    s = S[i]
    seg.update(i,2**(sid(s)))
for q in range(Q):
    num,a,b = input().split()
    if num=="1":
        seg.update(int(a)-1,2**sid(b))
        #print(a,b,list(map(lambda x:bin(x)[2:],seg.tree)))
    else:
        print(bin(seg.query(int(a)-1,int(b))).count("1"))

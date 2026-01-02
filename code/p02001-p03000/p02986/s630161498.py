# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N,Q=map(int,input().split())
edge=[[] for _ in range(N)]
for _ in range(N-1):
    a,b,c,d=map(int1,input().split())
    d+=1
    edge[a].append((b,c,d))
    edge[b].append((a,c,d))
U=defaultdict(list)
V=defaultdict(list)
Query=[]
for i in range(Q):
    x,y,u,v=map(int1,input().split())
    y+=1
    Query.append((x,y,u,v))
    U[u].append((x,y,i))
    V[v].append((x,y,i))

S=[0]*(2*N-1)

def EulerTour(start,n,edges):
    used=[False]*n
    et=[]
    left=[-1]*n
    right=[-1]*n
    depth=[]
    stack=[(start,-1,-1)]
    cur_depth=-1
    while stack:
        v,c,d=stack.pop()
        if et:
            S[len(et)]=S[len(et)-1]+d
        if v>=0:
            used[v]=True
            cur_depth+=1
            left[v]=right[v]=len(et)
            et.append(v)
            depth.append(cur_depth)
            for nv,c,d in edges[v]:
                if not used[nv]:
                    stack.append((~v,c,-d))
                    stack.append((nv,c,d))
        else:
            cur_depth-=1
            right[~v]=len(et)
            et.append(~v)
            depth.append(cur_depth)
    return et,left,depth

et,left,depth=EulerTour(0,N,edge)

class SegmentTree:
    def __init__(self,n,segfunc,ide_ele):
        self.segfunc=segfunc
        self.ide_ele=ide_ele
        self.num=2**(n-1).bit_length()
        self.dat=[ide_ele]*2*self.num
    
    def init(self,iter):
        for i in range(len(iter)):
            self.dat[i+self.num]=iter[i]
        for i in range(self.num-1,0,-1):
            self.dat[i]=self.segfunc(self.dat[i*2],self.dat[i*2+1])
    
    def update(self,k,x):
        k+=self.num
        self.dat[k]=x
        while k:
            k//=2
            self.dat[k]=self.segfunc(self.dat[k*2],self.dat[k*2+1])
    
    def query(self,p,q):
        if q<=p:
            return self.ide_ele
        p+=self.num
        q+=self.num-1
        res=self.ide_ele
        while q-p>1:
            if p&1==1:
                res=self.segfunc(res,self.dat[p])
            if q&1==0:
                res=self.segfunc(res,self.dat[q])
                q-=1
            p=(p+1)//2
            q=q//2
        if p==q:
            res=self.segfunc(res,self.dat[p])
        else:
            res=self.segfunc(self.segfunc(res,self.dat[p]),self.dat[q])
        return res

s=SegmentTree(2*N-1,lambda a,b:min(a,b,key=lambda t:t[0]),(INF,INF))
for i in range(2*N-1):
    s.update(i,(depth[i],i))

LCA=defaultdict(list)
LLCA=[-1]*Q
for i,(x,y,u,v) in enumerate(Query):
    p,q=min(left[u],left[v]),max(left[u],left[v])+1
    res=s.query(p,q)
    LCA[et[res[1]]].append((x,y,i))
    LLCA[i]=res[1]

diff=[0]*Q

def EulerTour2(start,n,edges):
    used=[False]*n
    et=[]
    left=[-1]*n
    right=[-1]*n
    depth=[]
    stack=[(start,-1,-1)]
    cur_depth=-1
    col=[[0,0] for _ in range(N)]
    while stack:
        v,c,d=stack.pop()
        if v>=0:
            col[c][0]+=d
            col[c][1]+=1
            used[v]=True
            cur_depth+=1
            left[v]=right[v]=len(et)
            et.append(v)
            depth.append(cur_depth)
            for nv,c,d in edges[v]:
                if not used[nv]:
                    stack.append((~v,c,-d))
                    stack.append((nv,c,d))
        else:
            col[c][0]+=d
            col[c][1]-=1
            cur_depth-=1
            right[~v]=len(et)
            et.append(~v)
            depth.append(cur_depth)
        while LCA[v]:
            qc,qd,qi=LCA[v].pop()
            diff[qi]-=(col[qc][1]*qd-col[qc][0])*2
        while U[v]:
            qc,qd,qi=U[v].pop()
            diff[qi]+=col[qc][1]*qd-col[qc][0]
        while V[v]:
            qc,qd,qi=V[v].pop()
            diff[qi]+=col[qc][1]*qd-col[qc][0]
    return

EulerTour2(0,N,edge)

for i,(x,y,u,v) in enumerate(Query):
    print(S[left[v]]+S[left[u]]-S[LLCA[i]]*2+diff[i])
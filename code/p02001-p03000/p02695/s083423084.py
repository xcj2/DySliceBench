import sys,bisect,string,math,time,functools,random
from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
from itertools import permutations,combinations,groupby
def Golf():*a,=map(int,open(0))
def I():return int(input())
def S_():return input()
def IS():return input().split()
def LS():return [i for i in input().split()]
def LI():return [int(i) for i in input().split()]
def LI_():return [int(i)-1 for i in input().split()]
def NI(n):return [int(input()) for i in range(n)]
def NI_(n):return [int(input())-1 for i in range(n)]
def StoLI():return [ord(i)-97 for i in input()]
def ItoS(n):return chr(n+97)
def LtoS(ls):return ''.join([chr(i+97) for i in ls])
def GI(V,E,ls=None,Directed=False,index=1):
    org_inp=[];g=[[] for i in range(V)]
    FromStdin=True if ls==None else False
    for i in range(E):
        if FromStdin:
            inp=LI()
            a,b,c=(inp+[1])[:3]
            org_inp.append(inp)
        else:
            index=0
            a,b,c=(ls[i]+[1])[:3]
        if index==1:a-=1;b-=1
        aa=(a,c);bb=(b,c);g[a].append(bb)
        if not Directed:g[b].append(aa)
    return g,org_inp
def GGI(h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1):
#h,w,g,sg=GGI(h,w,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0}) # sample usage
    mp=[boundary]*(w+2);found={}
    for i in range(h):
        s=input()
        for char in search:
            if char in s:
                found[char]=((i+1)*(w+2)+s.index(char)+1)
                mp_def[char]=mp_def[replacement_of_found]
        mp+=[boundary]+[mp_def[j] for j in s]+[boundary]
    mp+=[boundary]*(w+2)
    return h+2,w+2,mp,found
def TI(n):return GI(n,n-1)
def bit_combination(k,n=2):
    rt=[]
    for tb in range(n**k):
        s=[tb//(n**bt)%n for bt in range(k)];rt+=[s]
    return rt
def show(*inp,end='\n'):
    if show_flg:print(*inp,end=end)

YN=['YES','NO'];Yn=['Yes','No']
mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
#sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()

class Comb:
    def __init__(self,n,mo=10**9+7):
        self.fac=[0]*(n+1)
        self.inv=[1]*(n+1)
        self.fac[0]=1
        self.fact(n)
        for i in range(1,n+1):
            self.fac[i]=i*self.fac[i-1]%mo
            self.inv[n]*=i
            self.inv[n]%=mo
        self.inv[n]=pow(self.inv[n],mo-2,mo)
        for i in range(1,n):
            self.inv[n-i]=self.inv[n-i+1]*(n-i+1)%mo
        return
    
    def fact(self,n):
        return self.fac[n]
        
    def invf(self,n):
        return self.inv[n]

    def comb(self,x,y):
        if y<0 or y>x:
            return 0
        return self.fac[x]*self.inv[x-y]*self.inv[y]%mo

class Tree:
    def __init__(self,inp_size=None,init=True):
        if init:
            self.stdin(inp_size)
        return

    def stdin(self,inp_size=None):
        if inp_size==None:
            self.size=int(input())
        else:
            self.size=inp_size
        self.edges,_=GI(self.size,self.size-1)
        return
    
    def listin(self,ls):
        self.size=len(ls)+1
        self.edges,_=GI(self.size,self.size-1,ls)
        return

    def __str__(self):
        return  str(self.edges)

    def dfs(self,x,func=lambda prv,nx,dist:prv+dist,root_v=0):
        q=deque()
        q.append(x)
        v=[-1]*self.size
        v[x]=root_v
        while q:
            c=q.pop()
            for nb,d in self.edges[c]:
                if v[nb]==-1:
                    q.append(nb)
                    v[nb]=func(v[c],nb,d)
        return v

    def EulerTour(self,x,func=lambda prv,nx,dist:prv+dist,root_v=0):
        q=deque()
        q.append((-1,x))
        v=[None]*self.size
        v[x]=root_v
        et=[]
        while q:
            cb,ce=q.pop()
            et.append(ce)
            for nb,d in self.edges[ce]:
                if v[nb]==None:
                    q.append((nb,ce))
                    q.append((ce,nb))
                    v[nb]=func(v[ce],nb,d)
        vid=[[-1,-1]for i in range(self.size)]
        for i,j in enumerate(et):
            if vid[j][0]==-1:
                vid[j][0]=i
            else:
                vid[j][1]=i
        return v,et,vid
    
    def LCA_init(self,depth,et):
        self.st=SegTree(self.size*2-1,func=min,ide=inf)
        for i,j in enumerate(et):
            self.st.update(i,j)
        self.LCA_init_stat==True
        return
    
    def LCA(self,root,x,y):
        if self.LCA_init_stat==False:
            depth,et,vid=self.EulerTour(root)
            self.LCA_init(depth,et)
        return self.st.query(x,y+1)

show_flg=False
show_flg=True

p=[]
def pat(n,m,ls):
    if ls:
        M=ls[-1]
    else:
        M=1

    if n==0:
        p.append(ls[:])
        return
    
    for i in range(M,m+1):
        pat(n-1,m,ls[:]+[i])

ans=0
z=[]
N,M,q=LI()
pat(N,M,[])
for i in range(q):
    a,b,c,d=LI()
    z+=[(a,b,c,d)]

for y in p:
    
    tmp=0
    for a,b,c,d in z:
        if y[b-1]-y[a-1]==c:
            tmp+=d
    if ans<tmp:
        ans=tmp
        rt=y[:]

print(ans)

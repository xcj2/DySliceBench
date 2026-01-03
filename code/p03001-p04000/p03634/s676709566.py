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
def GI(V,E,ls=None,Directed=False,index=0):
    org_inp=[];g=[[] for i in range(V)]
    FromStdin=True if ls==None else False
    for i in range(E):
        if FromStdin:
            inp=LI()
            org_inp.append(inp)
        else:
            inp=ls[i]
        if index==0:inp[0]-=1;inp[1]-=1
        if len(inp)==2:
            a,b=inp;g[a].append(b)
            if not Directed:g[b].append(a)
        elif len(inp)==3:
            a,b,c=inp;aa=(inp[0],inp[2]);bb=(inp[1],inp[2]);g[a].append(bb)
            if not Directed:g[b].append(aa)
    return g,org_inp
def GGI(h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0}):
#h,w,g,sg=GGI(h,w,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0}) # sample usage
    mp=[1]*(w+2);found={}
    for i in range(h):
        s=input()
        for char in search:
            if char in s:
                found[char]=((i+1)*(w+2)+s.index(char)+1)
                mp_def[char]=mp_def[replacement_of_found]
        mp+=[1]+[mp_def[j] for j in s]+[1]
    mp+=[1]*(w+2)
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

show_flg=False
show_flg=True


## Segment Tree ##

## Initializer Template ##
# Range Sum:        sg=SegTree(n)
# Range Minimum:    sg=SegTree(n,inf,min,inf)

class SegTree:

    def __init__(self,n,init_val=0,function=lambda a,b:a+b,ide=0):
        self.n=n
        self.ide_ele=ide_ele=ide
        self.num=num=2**(n-1).bit_length()
        self.seg=seg=[self.ide_ele]*2*self.num
        self.lazy=lazy=[self.ide_ele]*2*self.num
        self.segfun=segfun=function
        #set_val
        for i in range(n):
            self.seg[i+self.num-1]=init_val
        #built
        for i in range(self.num-2,-1,-1):
            self.seg[i]=self.segfun(self.seg[2*i+1],self.seg[2*i+2])
    
    def update(self,k,x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfun(self.seg[k*2+1],self.seg[k*2+2])
        
        
    def evaluate(k,l,r): #遅延評価処理
        if lazy[k]!=0:
            node[k]+=lazy[k]
            if(r-l>1):
                lazy[2*k+1]+=lazy[k]//2
                lazy[2*k+2]+=lazy[k]//2

        lazy[k]=0
        
    def query(self,p,q):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfun(res,self.seg[p])
            if q&1 == 1:
                res = self.segfun(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfun(res,self.seg[p])
        else:
            res = self.segfun(self.segfun(res,self.seg[p]),self.seg[q])
        return res
    
    def find_min_index(self,p,q,m):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfun(res,self.seg[p])
            if q&1 == 1:
                res = self.segfun(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfun(res,self.seg[p])
        else:
            res = self.segfun(self.segfun(res,self.seg[p]),self.seg[q])
        return res


    def __str__(self):
        # 生配列を表示
        rt=self.seg[self.num-1:self.num-1+self.n]
        return str(rt)


ans=0


class Tree:
    def __init__(self,init=True):
        if init:
            self.stdin()
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

    def dfs(self,x,func=lambda x,y,z:x+z,root_v=0):
        q=deque()
        q.append(x)
        v=[-1]*self.size
        v[x]=root_v
        while q:
            c=q.pop()
            for nb in self.edges[c]:
                d=1
                if type(nb) is not int:
                    nb,d=nb
                if v[nb]==-1:
                    q.append(nb)
                    v[nb]=func(v[c],nb,d)
        return v

    def EulerTour(self,x,func=lambda x:x+1,root_v=0):
        q=deque()
        q.append((-1,x))
        v=[None]*self.size
        v[x]=root_v
        et=[]
        while q:
            cb,ce=q.pop()
            et.append(ce)
            for nb in self.edges[ce]:
                if v[nb]==None:
                    q.append((nb,ce))
                    q.append((ce,nb))
                    v[nb]=func(v[ce])
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
        
#tr=Tree(init=False)
tr=Tree()
q,k=LI()

v=tr.dfs(k-1)

for i in range(q):
    x,y=LI_()
    print(v[x]+v[y])
    
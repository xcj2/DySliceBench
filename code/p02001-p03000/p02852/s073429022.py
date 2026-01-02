import sys,bisect,string,math,time,functools,random,fractions
from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
from itertools import permutations,combinations,groupby
def Golf():n,*t=map(int,open(0).read().split())
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
            org_inp.append(inp)
        else:
            inp=ls[i]
        if len(inp)==2:
            a,b=inp;c=1
        else:
            a,b,c=inp
        if index==1:a-=1;b-=1
        aa=(a,c);bb=(b,c);g[a].append(bb)
        if not Directed:g[b].append(aa)
    return g,org_inp
def GGI(h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1):
#h,w,g,sg=GGI(h,w,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1) # sample usage
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
def bit_combination(n,base=2):
    rt=[]
    for tb in range(base**n):s=[tb//(base**bt)%base for bt in range(n)];rt+=[s]
    return rt
def gcd(x,y):
    if y==0:return x
    if x%y==0:return y
    while x%y!=0:x,y=y,x%y
    return y
def show(*inp,end='\n'):
    if show_flg:print(*inp,end=end)
 
YN=['YES','NO'];Yn=['Yes','No']
mo=10**9+7
inf=float('inf')
FourNb=[(-1,0),(1,0),(0,1),(0,-1)];EightNb=[(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)];compas=dict(zip('WENS',FourNb));cursol=dict(zip('LRUD',FourNb))
l_alp=string.ascii_lowercase
#sys.setrecursionlimit(10**7)
read=sys.stdin.buffer.read
readline=sys.stdin.buffer.readline
input=lambda: sys.stdin.readline().rstrip()

class Tree:
    def __init__(self,inp_size=None,ls=None,init=True,index=0):
        self.LCA_init_stat=False
        self.ETtable=[]
        if init:
            if ls==None:
                self.stdin(inp_size,index=index)
            else:
                self.size=len(ls)+1
                self.edges,_=GI(self.size,self.size-1,ls,index=index)
        return
 
    def stdin(self,inp_size=None,index=1):
        if inp_size==None:
            self.size=int(input())
        else:
            self.size=inp_size
        self.edges,_=GI(self.size,self.size-1,index=index)
        return
    
    def listin(self,ls,index=0):
        self.size=len(ls)+1
        self.edges,_=GI(self.size,self.size-1,ls,index=index)
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
 
    def EulerTour(self,x):
        q=deque()
        q.append(x)
        self.depth=[None]*self.size
        self.depth[x]=0
        self.ETtable=[]
        self.ETdepth=[]
        self.ETin=[-1]*self.size
        self.ETout=[-1]*self.size
        cnt=0
        while q:
            c=q.pop()
            if c<0:
                ce=~c
            else:
                ce=c
                for nb,d in self.edges[ce]:
                    if self.depth[nb]==None:
                        q.append(~ce)
                        q.append(nb)
                        self.depth[nb]=self.depth[ce]+1
            self.ETtable.append(ce)
            self.ETdepth.append(self.depth[ce])
            if self.ETin[ce]==-1:
                self.ETin[ce]=cnt
            else:
                self.ETout[ce]=cnt
            cnt+=1
        return
    
    def LCA_init(self,root):
        self.EulerTour(root)
        #self.st=SparseTable(self.ETdepth,init_func=min,init_idl=inf)
        self.st=SegTree(self.size*2-1,self.ETdepth,function=min,ide=inf)
        self.LCA_init_stat=True
        return
    
    def LCA(self,root,x,y):
        if self.LCA_init_stat==False:
            self.LCA_init(root)
        xin,xout=self.ETin[x],self.ETout[x]
        yin,yout=self.ETin[y],self.ETout[y]
        a=min(xin,yin)
        b=max(xout,yout,xin,yin)
        id_of_min_dep_in_et=self.st.query_id(a,b+1)
        return self.ETtable[id_of_min_dep_in_et]
 
class SparseTable: # O(N log N) for init, O(1) for query(l,r)
    def __init__(self,ls,init_func=min,init_idl=float('inf')):
        self.func=init_func
        self.idl=init_idl
        self.size=len(ls)
        self.N0=self.size.bit_length()
        self.table=[ls[:]]
        self.index=[list(range(self.size))]
        self.lg=[0]*(self.size+1)
        
        for i in range(2,self.size+1):
            self.lg[i]=self.lg[i>>1]+1
 
        for i in range(self.N0):
            tmp=[self.func(self.table[i][j],self.table[i][min(j+(1<<i),self.size-1)]) for j in range(self.size)]
            tmp_id=[self.index[i][j] if self.table[i][j]==self.func(self.table[i][j],self.table[i][min(j+(1<<i),self.size-1)]) else self.index[i][min(j+(1<<i),self.size-1)] for j in range(self.size)]
            self.table+=[tmp]
            self.index+=[tmp_id]
    
    # return func of [l,r)
    def query(self,l,r):
        if r>self.size:r=self.size
        #N=(r-l).bit_length()-1
        N=self.lg[r-l]
        return self.func(self.table[N][l],self.table[N][max(0,r-(1<<N))])
    
    # return index of which val[i] = func of v among [l,r)
    def query_id(self,l,r):
        if r>self.size:r=self.size
        #N=(r-l).bit_length()-1
        N=self.lg[r-l]
        a,b=self.index[N][l],self.index[N][max(0,r-(1<<N))]
        if self.table[0][a]==self.func(self.table[N][l],self.table[N][max(0,r-(1<<N))]):
            b=a
        return b
    
    def __str__(self):
        return str(self.table[0])
 
    def print(self):
        for i in self.table:
            print(*i)

## Segment Tree ##

## Test case: ABC 146 F
## https://atcoder.jp/contests/abc146/tasks/abc146_f

## Initializer Template ##
# Range Sum:        sg=SegTree(n)
# Range Minimum:    sg=SegTree(n,inf,min,inf)

class SegTree:
    def __init__(self,n,init_val=0,function=lambda a,b:a+b,ide=0):
        self.size=n
        self.ide_ele=ide
        self.num=1<<(self.size-1).bit_length()
        self.table=[self.ide_ele]*2*self.num
        self.index=[0]*2*self.num
        self.lazy=[self.ide_ele]*2*self.num
        self.func=function
        #set_val
        if not hasattr(init_val,"__iter__"):
            init_val=[init_val]*self.size
        for i,val in enumerate(init_val):
            self.table[i+self.num-1]=val
            self.index[i+self.num-1]=i
        #build
        for i in range(self.num-2,-1,-1):
            self.table[i]=self.func(self.table[2*i+1],self.table[2*i+2])
            if self.table[i]==self.table[i*2+1]:
                self.index[i]=self.index[i*2+1]
            else:
                self.index[i]=self.index[i*2+2]
        
    def update(self,k,x):
        k+=self.num-1
        self.table[k]=x
        while k:
            k=(k-1)//2
            res=self.func(self.table[k*2+1],self.table[k*2+2])
            self.table[k]=res
            
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
        p+=self.num-1
        q+=self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1==0:
                res=self.func(res,self.table[p])
            if q&1==1:
                res=self.func(res,self.table[q])
                q-=1
            p=p>>1
            q=(q-1)>>1
        if p==q:
            res=self.func(res,self.table[p])
        else:
            res=self.func(self.func(res,self.table[p]),self.table[q])
        return res
    
    def query_id(self,p,q):
        if q<=p:
            return self.ide_ele
        p+=self.num-1
        q+=self.num-2
        res=self.ide_ele
        idx=p
        while q-p>1:
            if p&1==0:
                res=self.func(res,self.table[p])
                if res==self.table[p]:
                    idx=self.index[p]
            if q&1==1:
                res=self.func(res,self.table[q])
                if res==self.table[q]:
                    idx=self.index[q]
                q-=1
            p=p>>1
            q=(q-1)>>1
        if p==q:
            res=self.func(res,self.table[p])
            if res==self.table[p]:
                idx=self.index[p]
        else:
            res=self.func(self.func(res,self.table[p]),self.table[q])
            if res==self.table[p]:
                idx=self.index[p]
            elif res==self.table[q]:
                idx=self.index[q]
        return idx


    def __str__(self):
        # 生配列を表示
        rt=self.table[self.num-1:self.num-1+self.size]
        return str(rt)

show_flg=False
show_flg=True
ans=0

n,m=LI()
s=[int(i) for i in input()]
 
def dp(b,m): # N log (N)
    N=len(b)-1
    n=N+1
    sg=SegTree(n,inf,min,inf)
 
    sg.update(0,0)
 
    dp=[0]+[inf]*(N)
    for i in range(N):
        if b[i+1]==1:
            continue
        dp[i+1]=sg.query(max(i-m+1,0),i+1)+1
        sg.update(i+1,dp[i+1])

    return dp
 
dp1=dp(s,m)
step=dp1[n]
if step==inf:
    print(-1)
    exit()
 
dp2=dp(s[::-1],m)[::-1]
 

move=[0]
ans=[]
j=1
for i in range(step,0,-1): # N
    while j<=n and dp2[j]!=i-1:
        j+=1
    move.append(j)
 
for i in range(len(move)-1):
    ans.append(move[i+1]-move[i])
print(*ans)
exit()
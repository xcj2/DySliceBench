import sys,bisect,string,math,time,functools,random,fractions
from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
from itertools import permutations,combinations,groupby
rep=range;R=range
def Golf():n,*t=map(int,open(0).read().split())
def I():return int(input())
def S_():return input()
def IS():return input().split()
def LS():return [i for i in input().split()]
def MI():return map(int,input().split())
def LI():return [int(i) for i in input().split()]
def LI_():return [int(i)-1 for i in input().split()]
def NI(n):return [int(input()) for i in range(n)]
def NI_(n):return [int(input())-1 for i in range(n)]
def NLI(n):return [[int(i) for i in input().split()] for i in range(n)]
def NLI_(n):return [[int(i)-1 for i in input().split()] for i in range(n)]
def StoLI():return [ord(i)-97 for i in input()]
def ItoS(n):return chr(n+97)
def LtoS(ls):return ''.join([chr(i+97) for i in ls])
def RA():return map(int,open(0).read().split())
def RLI(n=8,a=1,b=10):return [random.randint(a,b)for i in range(n)]
def RI(a=1,b=10):return random.randint(a,b)
def INP():
    N=10;A=10
    n=random.randint(1,N)
    a=[random.randint(1,A) for i in range(n)]
    return n,a
def Rtest(T):
    case,err=0,0
    for i in range(T):
        inp=INP()
        a1=naive(*inp)
        a2=solve(*inp)
        if a1!=a2:
            print((a1,a2),inp)
            err+=1
        case+=1
    print('Tested',case,'case with',err,'errors')
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
    for i in R(h):
        s=input()
        for char in search:
            if char in s:
                found[char]=((i+1)*(w+2)+s.index(char)+1)
                mp_def[char]=mp_def[replacement_of_found]
        mp+=[boundary]+[mp_def[j] for j in s]+[boundary]
    mp+=[boundary]*(w+2)
    return h+2,w+2,mp,found
def TI(n):return GI(n,n-1)
def accum(ls):
    rt=[0]
    for i in ls:rt+=[rt[-1]+i]
    return rt
def bit_combination(n,base=2):
    rt=[]
    for tb in R(base**n):s=[tb//(base**bt)%base for bt in R(n)];rt+=[s]
    return rt
def gcd(x,y):
    if y==0:return x
    if x%y==0:return y
    while x%y!=0:x,y=y,x%y
    return y
def YN(x):print(['NO','YES'][x])
def Yn(x):print(['No','Yes'][x])
def show(*inp,end='\n'):
    if show_flg:print(*inp,end=end)

mo=10**9+7
#mo=998244353
inf=float('inf')
FourNb=[(-1,0),(1,0),(0,1),(0,-1)];EightNb=[(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)];compas=dict(zip('WENS',FourNb));cursol=dict(zip('LRUD',FourNb))
l_alp=string.ascii_lowercase
#sys.setrecursionlimit(10**9)
read=sys.stdin.buffer.read;readline=sys.stdin.buffer.readline;input=lambda:sys.stdin.readline().rstrip()
 
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
            
            ## Remove if index is not needed
            if res==self.table[k*2+1]:
                self.index[k]=self.index[k*2+1]
            else:
                self.index[k]=self.index[k*2+2]
            ## Remove if index is not needed
        
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
 
ans=0

n,k=LI()
a=NI(n)
A=max(a)
sg=SegTree(A+2,init_val=0,function=max,ide=0)
for i in a:
    l=max(0,i-k)
    r=min(A,i+k)
    t=sg.query(i,i+1)
    sg.update(i,max(t,sg.query(l,r+1)+1))

print(sg.query(0,A+1))

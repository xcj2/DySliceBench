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
def StoLI():return [ord(i)-97 for i in input()]
def ItoS(n):return chr(n+97)
def LtoS(ls):return ''.join([chr(i+97) for i in ls])
def RA():return map(int,open(0).read().split())
def RLI(n=8,a=1,b=10):return [random.randint(a,b)for i in range(n)]
def RI(a=1,b=10):return random.randint(a,b)
def Rtest(T):
    case,err=0,0
    for i in range(T):
        inp=INP()
        a1,ls=naive(*inp)
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
inf=float('inf')
FourNb=[(-1,0),(1,0),(0,1),(0,-1)];EightNb=[(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)];compas=dict(zip('WENS',FourNb));cursol=dict(zip('LRUD',FourNb))
l_alp=string.ascii_lowercase
#sys.setrecursionlimit(10**9)
read=sys.stdin.buffer.read;readline=sys.stdin.buffer.readline;input=lambda:sys.stdin.readline().rstrip()

########################################################################################################################################################################
# Verified by
# https://atcoder.jp/contests/arc033/submissions/me
# https://atcoder.jp/contests/abc174/tasks/abc174_f
#
# speed up TIPS: delete update of el. non-use of getitem, setitem.
#
# Binary Indexed Tree
# Bit.add(i,x)    : add x at i-th value
# Bit.sum(i)      : get sum up to i-th value
# Bit.l_bound(w)  : get bound of index where x1+x2+...+xi<w

class Bit: # 1-indexed
    def __init__(self,n,init=None):
        self.size=n
        self.m=len(bin(self.size))-2
        self.arr=[0]*(2**self.m+1)
        self.el=[0]*(2**self.m+1)
        if init!=None:
            for i in range(len(init)):
                self.add(i,init[i])
                self.el[i]=init[i]

    def __str__(self):
        a=[self.sum(i+1)-self.sum(i) for i in range(self.size)]
        return str(a)
        
    def add(self,i,x):
        if not 0<i<=self.size:return NotImplemented
        self.el[i]+=x
        while i<=self.size:
            self.arr[i]+=x
            i+=i&(-i)
        return
    
    def sum(self,i):
        if not 0<=i<=self.size:return NotImplemented
        rt=0
        while i>0:
            rt+=self.arr[i]
            i-=i&(-i)
        return rt
    
    def __getitem__(self,key):
        return self.el[key]
        return self.sum(key+1)-self.sum(key)

    def __setitem__(self,key,value):
        self.add(key,value-self.sum(key+1)+self.sum(key))

    def l_bound(self,w):
        if w<=0:
            return 0
        x=0
        k=2**self.m
        while k>0:
            if x+k<=self.size and self.arr[x+k]<w:
                w-=self.arr[x+k]
                x+=k
            k>>=1
        return x+1
        
    def u_bound(self,w):
        if w<=0:
            return 0
        x=0
        k=2**self.m
        while k>0:
            if x+k<=self.size and self.arr[x+k]<=w:
                w-=self.arr[x+k]
                x+=k
            k>>=1
        return x+1
        
class Bit0(Bit): # 0-indexed
    def add(self,j,x):
        super().add(j+1,x)
    def l_bound(self,w):
        return max(super().l_bound(w)-1,0)
    def u_bound(self,w):
        return max(super().u_bound(w)-1,0)

class Multiset(Bit0):
    def __init__(self,max_v):
        super().__init__(max_v)
    def insert(self,x):
        super().add(x,1)
    def find(self,x):
        return super().l_bound(super().sum(x))
    def __str__(self):
        return str(self.arr)

def compress(L):
    dc={v:i for i,v in enumerate(sorted(set(L)))}
    return [dc[i] for i in L]


show_flg=False
show_flg=True

ans=0

h,w=LI()
sh,sw=LI()
gh,gw=LI()

w+=2
m=[1]*w
for i in range(h):
    s=input()
    m+=[1]+[i=='#'for i in s]+[1]
m+=[1]*w
h+=2
n=h*w
v=[-1]*w*h

dc=dict()
cn=0
def bfs(x):
    global cn
    q=[x]
    v[x]=x
    dc[x]=cn
    cn+=1
    while q:
        c=q.pop()
        for nx in [c+1,c-1,c+w,c-w]:
            if 0<=nx<n and m[nx]!=1 and v[nx]==-1:
                q+=nx,
                v[nx]=x
    return        
            
for i in range(n):
    if m[i]!=1 and v[i]==-1:
        bfs(i)

g=[set()for i in range(cn)]
nbw=[-2*w+1,-2*w+2,-w+1,-w+2,2,2*w+1,2*w+2,w+1,w+2,+2*w,-2*w,-2*w-1,-2*w-2,-w-1,-w-2,-2,2*w-1,2*w-2,w-1,w-2]
nb=[1,-1,w,-w]
d=[-1]*n
v=[0]*n
vw=[0]*n
q=deque([(sh*w+sw,0)])
v[sh*w+sw]=1
vw[sh*w+sw]=1
while q:
    i,dist=q.pop()
    if d[i]==-1:
        d[i]=dist
    else:
        d[i]=min(dist,d[i])
    if m[i]==1:
        continue
    for di in nb:
        nx=i+di
        if 0<=nx<n and m[nx]!=1 and v[nx]==0:
            #d[nx]=d[i]
            v[nx]=1
            q.append((nx,d[i]))

    for di in nbw:
        nx=i+di
        if 0<=nx<n and m[nx]!=1 and vw[nx]==0:
            vw[nx]=1
            q.appendleft((nx,d[i]+1))
print(d[gh*w+gw])
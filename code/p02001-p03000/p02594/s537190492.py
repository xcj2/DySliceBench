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
def Ra():return map(int,open(0).read().split())
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
sys.setrecursionlimit(10**9)
read=sys.stdin.buffer.read;readline=sys.stdin.buffer.readline;input=lambda:sys.stdin.readline().rstrip()

########################################################################################################################################################################


def dijkstra(edge,st):
    # edge=[[(v_to,dist_to_v),...],[],...]
    # initialize: def: d=dist(st,i), prev=[previous vertex in minimum path], q[]
    n=len(edge)
    d=[(0 if st==i else inf) for i in range(n)]
    q=[(j,i) for i,j in enumerate(d)]
    heapify(q)
    v=[False]*n
    # calc
    while q:
        dist,cur=heappop(q)
        if v[cur]:
            continue
        v[cur]=True
        for dst,dist in edge[cur]:
            alt=d[cur]+c[cur]
            if alt<d[dst]:
                d[dst]=alt
                heappush(q,(alt,dst))
    return d

class UnionFind:
    def __init__(self, n):
        # 負  : 根であることを示す。絶対値はランクを示す
        # 非負: 根でないことを示す。値は親を示す
        self.table = [-1] * n
 
    def _root(self, x):
        if self.table[x] < 0:
            return x
        else:
            # 経路の圧縮
            self.table[x] = self._root(self.table[x])
            return self.table[x]
 
    def find(self, x, y):
        return self._root(x) == self._root(y)
 
    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        # ランクの取得
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2
    
    def __str__(self):
        rt=[i if j<0 else j for i,j in enumerate(self.table)]
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


Yn(I()>=30)
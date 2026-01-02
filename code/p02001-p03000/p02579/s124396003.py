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

inf=1<<20
def dijkstra(edge,st):
    n=len(edge)
    d=[(0 if st==i else inf) for i in range(n)]
    q=[(0,st)]
    heapify(q)
    v=[False]*n
    while q:
        dist,cur=heappop(q)
        if v[cur]:
            continue
        v[cur]=True
        for dst,dist in edge[cur]:
            alt=d[cur]+dist
            if alt<d[dst]:
                d[dst]=alt
                heappush(q,(alt,dst))
    return d

# Under construction
# To be verified by https://atcoder.jp/contests/abc176/tasks/abc176_d

class GridGraph:
    def __init__(self,h,w,search=None,replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1):
        self.h=h+2
        self.w=w+2
        self.n=self.h*self.w
        self.edge=[[]for i in range(self.n)]
        self.nb=[-1,1,-self.w,self.w]
        #h,w,g,sg=GGI(h,w,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0},boundary=1) # sample usage
        self.mp=[boundary]*self.w
        self.found={}
        for i in range(self.h-2):
            s=input()
            self.mp+=[boundary]
            for i in range(self.w-2):
                char=s[i]
                if search and char in search:
                    self.found[char]=((i+1)*self.w+i+1)
                    mp_def[char]=mp_def[replacement_of_found]
                self.mp+=[mp_def[char]]
            self.mp+=[boundary]
        self.mp+=[boundary]*self.w
        self.h,self.w,self.mp,self.found
        return

    def create_edge(self,cost_func=lambda x,y:1):
        w=self.w
        nbw=[2,2*w+1,2*w+2,w+1,w+2,+2*w,2*w-1,2*w-2,w-1,w-2]
        for i in range(self.n):
            if self.mp[i]==1:
                continue
            for di in self.nb:
                nx=i+di
                if self.mp[nx]!=1:
                    #self.edge[i].append((nx,cost_func(self.mp[i],self.mp[nx])))
                    self.edge[i].append((nx,0))
            
            for di in nbw:
                nx=i+di
                if 0<=nx<self.n and self.mp[nx]!=1:
                    self.edge[i].append((nx,1))
                    self.edge[nx].append((i,1))
            
        return self.edge


    def dfs(self,x,func=lambda pr,prv,nx,dist:prv+dist,root_v=0):
        q=deque([x])
        v=[None]*self.node_size
        v[x]=root_v
        while q:
            c=q.pop()
            for nb,d in self.edges[c]:
                if v[nb]==None:
                    q.append(nb)
                    v[nb]=func(c,v[c],nb,d)
        return v
 
    def bfs(self,x,func=lambda pr,prv,nx,dist:prv+dist,root_v=0):
        q=deque([x])
        v=[None]*self.node_size
        v[x]=root_v
        while q:
            c=q.popleft()
            for nb,d in self.edges[c]:
                if v[nb]==None:
                    q.append(nb)
                    v[nb]=func(c,v[c],nb,d)
        return v

    def __str__(self):
        for i in range(self.h):
            print(self.mp[i*self.w:(i+1)*self.w])
        return ''
 
    def show_map(self,length=2):
        for i in range(self.h):
            print(*[' '*(length-(len(str(j))))+str(j) for j in self.mp[i*self.w:(i+1)*self.w]])

    def show_node_num(self,length=2):
        for i in range(self.h):
            print(*[' '*(length-(len(str(j))))+str(j) for j in range(i*self.w,(i+1)*self.w)])

    def show_map_w_node_num(self,length=2):
        for i in range(self.h):
            print(*[[' '*(length-(len(str(j))))+str(j),self.mp[j]] for j in range(i*self.w,(i+1)*self.w)])
    
    def show_edge(self,length=2):
        for i in range(self.h):
            print(*[[' '*(length-(len(str(j))))+str(j),self.edge[j]] for j in range(i*self.w,(i+1)*self.w)])


    def dfs2(self,x,func=lambda pr,prv,nx,dist:prv+dist,root_v=0):
        q=deque([x])
        v=[None]*self.node_size
        v[x]=root_v
        dfs_tr=[x]
        while q:
            c=q.pop()
            for nb,d in self.edges[c]:
                if v[nb]==None:
                    q.append(nb)
                    v[nb]=func(c,v[c],nb,d)
                    dfs_tr+=nb,
        return v,dfs_tr

show_flg=False
show_flg=True

ans=0

h,w=LI()
sh,sw=LI()
gh,gw=LI()

gg=GridGraph(h,w)
gg.create_edge()
d=dijkstra(gg.edge,sh*gg.w+sw)
ans=d[gh*gg.w+gw]
if ans==inf:
    ans=-1
print(ans)
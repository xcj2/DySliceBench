from heapq import heappush,heappop,heapify
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

mo=10**9+7
FourNb=[(-1,0),(1,0),(0,1),(0,-1)];EightNb=[(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)];compas=dict(zip('WENS',FourNb));cursol=dict(zip('LRUD',FourNb))
import sys
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


nbw=[-2*w+1,-2*w+2,-w+1,-w+2,2,2*w+1,2*w+2,w+1,w+2,+2*w,-2*w,-2*w-1,-2*w-2,-w-1,-w-2,-2,2*w-1,2*w-2,w-1,w-2]
nbw=[2,2*w+1,2*w+2,w+1,w+2,+2*w,2*w-1,2*w-2,w-1,w-2]
nb=[1,-1,w,-w]
nb=[1,w]
d=[-1]*n
g=[[]for i in range(n)]
for i in range(n):
    if m[i]==1:
      continue
    for di in nbw:
        nx=i+di
        if 0<=nx<n and m[nx]!=1:
            g[i]+=(nx,1),
            g[nx]+=(i,1),
    for di in nb:
        nx=i+di
        if 0<=nx<n and m[nx]!=1:
            g[i]+=(nx,0),
            g[nx]+=(i,0),
            
d=dijkstra(g,sh*w+sw)
ans=d[gh*w+gw]
if ans==inf:
    ans=-1
print(ans)

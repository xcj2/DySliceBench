from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
from itertools import permutations,combinations,groupby
import sys,bisect,string,math,time,functools,random
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
def GI(V,E,Directed=False,index=0):
    org_inp=[];g=[[] for i in range(n)]
    for i in range(E):
        inp=LI();org_inp.append(inp)
        if index==0:inp[0]-=1;inp[1]-=1
        if len(inp)==2:
            a,b=inp;g[a].append(b)
            if not Directed:g[b].append(a)
        elif len(inp)==3:
            a,b,c=inp;aa=(inp[0],inp[2]);bb=(inp[1],inp[2]);g[a].append(bb)
            if not Directed:g[b].append(aa)
    return g,org_inp
def GGI(h,w,boundary=1,search=[],replacement_of_found='.',mp_def={'#':1,'.':0}):
#h,w,g,sg=GGI(h,w,boundary=1,search=['S','G'],replacement_of_found='.',mp_def={'#':1,'.':0}) # sample usage
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
def bit_combination(k,n=2):return [[tb//(n**bt)%n for bt in range(k)] for tb in range(n**k)]
def show(*inp,end='\n'):
    if show_flg:print(*inp,end=end)
def show2d(g,h,w):
    for i in range(h):show(g[i*w:i*w+w])

YN=['YES','NO'];Yn=['Yes','No']
mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
#sys.setrecursionlimit(10**7)
input=lambda: sys.stdin.readline().rstrip()

def ran_input():
    n=random.randint(4,16)
    rmin,rmax=1,10
    a=[random.randint(rmin,rmax) for _ in range(n)]
    return n,a

show_flg=False
show_flg=True

ans=0

def gcj(t,*x):
    print("Case #"+str(t)+":",*x)
    return

n,t=LI()
N=6001
N=31
dp=[[0]*t for i in range(n+1)]
c=[]
for i in range(n):
    a,b=LI()
    c+=[(a,b)]
c.sort(key=lambda x:x[0]*4000-x[1])
for i in range(n):
    a,b=c[i]
    ans=max(ans,dp[i][-1]+b)
    for j in range(t):
        dp[i+1][j]=max(dp[i+1][j],dp[i][j])
        if j+a<t:
            dp[i+1][j+a]=max(dp[i][j]+b,dp[i][j+a])

print(ans)
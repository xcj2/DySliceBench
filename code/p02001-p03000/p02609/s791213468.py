import sys,bisect,string,math,time,functools,random,fractions
from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
from itertools import permutations,combinations,groupby
rep=range
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
def GI(V,E,ls=None,Directed=False,index=1):
    org_inp=[];g=[[] for i in R(V)]
    FromStdin=True if ls==None else False
    for i in R(E):
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
#sys.setrecursionlimit(10**7)
read=sys.stdin.buffer.read;readline=sys.stdin.buffer.readline;input=lambda:sys.stdin.readline().rstrip()

show_flg=False
show_flg=True

ans=0

def f(x):
    c=0
    while x>0:
        c+=1
        y=bin(x).count('1')
        x%=y
    return c

def f_init(x):
    rt=[0]*3
    p=x.count('1')
    N=len(x)
    for i in range(N):
        if x[i]=='1':
            for j in [-1,0,1]:
                rt[j]+=b[j][N-1-i]
                rt[j]%=p+j
#    show('init',x,rt,1+a[rt[0]])
    ans=[0]*3
    for j in [-1,0,1]:
        ans[j]=1+f(rt[j])
    return rt,ans
    


n=I()
s=S_()

N=2*10**5+10
a=[0]*(N+1)
p=s.count('1')


if p>1:
            
    for i in rep(N):
        a[i]=f(i)
    
    t=1
    t_p=1
    t_m=1
    p_p=p+1
    p_m=p-1
    
    f_x=0
    f_p=0
    f_m=0
    for i in rep(n)[::-1]:
        if s[i]=='1':
            f_x+=t%p
            f_p+=t_p%p_p
            f_m+=t_m%p_m
        t*=2
        t_p*=2
        t_m*=2
        t%=p
        t_p%=p_p
        t_m%=p_m
    
    t_p=1
    t_m=1
    ans=[]
    for i in rep(n)[::-1]:
        if s[i]=='1':
            nx=f_m-t_m%p_m
            nx%=p_m
        if s[i]=='0':
            nx=f_p+t_p%p_p
            nx%=p_p
        ans+=a[nx]+1,
    
        t*=2
        t_p*=2
        t_m*=2
        t%=p
        t_p%=p_p
        t_m%=p_m
    
    
    for i in ans[::-1]:
        print(i)

elif p==1:
       
    for i in rep(N):
        a[i]=f(i)
    
    t=1
    t_p=1
    t_m=1
    p_p=p+1
    p_m=p-1
    
    f_x=0
    f_p=0
    f_m=0
    for i in rep(n)[::-1]:
        if s[i]=='1':
            f_x+=t%p
            f_p+=t_p%p_p
            #f_m+=t_m%p_m
        t*=2
        t_p*=2
        t_m*=2
        t%=p
        t_p%=p_p
        #t_m%=p_m
    
    t_p=1
    t_m=1
    ans=[]
    for i in rep(n)[::-1]:
        if s[i]=='1':
            ans+=0,
        if s[i]=='0':
            nx=f_p+t_p%p_p
            nx%=p_p
            ans+=a[nx]+1,
    
        t*=2
        t_p*=2
        t_m*=2
        t%=p
        t_p%=p_p
        #t_m%=p_m
    
    
    for i in ans[::-1]:
        print(i)

elif p==0:
       
    for i in rep(N):
        a[i]=f(i)
    
    t=1
    t_p=1
    t_m=1
    p_p=p+1
    p_m=p-1
    
    f_x=0
    f_p=0
    f_m=0
    for i in rep(n)[::-1]:
        if s[i]=='1':
            f_x+=t%p
            f_p+=t_p%p_p
            #f_m+=t_m%p_m
        t*=2
        t_p*=2
        t_m*=2
        #t%=p
        t_p%=p_p
        #t_m%=p_m
    
    t_p=1
    t_m=1
    ans=[]
    for i in rep(n)[::-1]:
        if s[i]=='1':
            ans+=0,
        if s[i]=='0':
            nx=f_p+t_p%p_p
            nx%=p_p
            ans+=a[nx]+1,
    
        t*=2
        t_p*=2
        t_m*=2
#        t%=p
        t_p%=p_p
        #t_m%=p_m
    
    
    for i in ans[::-1]:
        print(i)

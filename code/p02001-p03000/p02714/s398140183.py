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

## return prime factors of N as dictionary {prime p:power of p}
## within 2 sec for N = 2*10**20+7
def primeFactor(N):
    i,n=2,N
    ret={}
    d,sq=2,99
    while i<=sq:
        k=0
        while n%i==0:
            n,k,ret[i]=n//i,k+1,k+1
        if k>0 or i==97:
            sq=int(n**(1/2)+0.5)
        if i<4:
            i=i*2-1
        else:
            i,d=i+d,d^6
    if n>1:
        ret[n]=1
    return ret


## return the list of prime numbers in [2,N], using eratosthenes sieve
## within 2sec for N = 1.2*10**7
def PrimeNumSet(N):
    Max = int(N**0.5)
    seachList = [i for i in range(2,N+1)]
    primeNum = []
    while seachList:
        if seachList[0] <= Max:
            break
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum

## retrun LCM of numbers in list b
## within 2sec for no of B = 10*5  and  Bi < 10**6
def LCM(b,mo=10**9+7):
    prs=PrimeNumSet(max(b))
    M=dict(zip(prs,[0]*len(prs)))
    for i in b:
        dc=primeFactor(i)
        for j,k in dc.items():
            M[j]=max(M[j],k)
    
    r=1
    for j,k in M.items():
        if k!=0:
            r*=pow(j,k,mo)
            r%=mo
    return r

show_flg=False
show_flg=True

'''
#C
g=[[1]*201 for i in range(201)]
for a in range(1,201):
    for b in range(1,201):
        g[a][b]=math.gcd(a,b)

k=I()
ans=0
for a in range(1,k+1):
    for b in range(1,k+1):
        for c in range(1,k+1):
            ans+=g[a][g[b][c]]
         
print(ans)
'''


#D
n=I()
s=input()
A=[[0],[0],[0]]
for i in range(n):
    w=s[i]
    A[0].append(A[0][-1]+(w=='R'))
    A[1].append(A[1][-1]+(w=='G'))
    A[2].append(A[2][-1]+(w=='B'))

#show(A)
t='RGB'

a=0
for i in range(1,n-1):
    w=s[i]
    if w=='R':
        j,k=1,2
    elif w=='G':
        j,k=0,2
    elif w=='B':
        j,k=0,1

    a+=A[j][i]*(A[k][n]-A[k][i])
    a+=A[k][i]*(A[j][n]-A[j][i])
    for l in range(i):
        if i+i-l>=n:
            continue
        if set([s[l],s[i+i-l]])==set([t[j],t[k]]):
            a-=1

print(a)

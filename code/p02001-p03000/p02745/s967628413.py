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
 
def ran_input():
    n=random.randint(4,16)
    rmin,rmax=1,10
    a=[random.randint(rmin,rmax) for _ in range(n)]
    return n,a

show_flg=False
show_flg=True



def PonAC(a,b,c):
    A = len(a)
    B = len(b)
    C = len(c)
     
    def judge(s, t):
    	X = [0] * 200
    	ns, nt = len(s), len(t)
    	for i in range(ns):
    		for j in range(nt):
    			if s[i] != t[j] and s[i] != '?' and t[j] != '?':
    				X[i-j+80] = 1
    	return X
     
    ab = judge(a, b)
    bc = judge(b, c)
    ac = judge(a, c)
    r = A + B + C
    for i in range(-40, 41):
    	for j in range(-40, 41):
    		if (not ab[i+80]) and (not ac[j+80]) and (not bc[j-i+80]):
    			st = min(i, j, 0)
    			en = max(i+B, j+C, A)
    			r = min(en-st, r)
    return r


def ran():
    chs=[-34,-34,0,1,2,3]
    N=len(chs)-1
    mx,Mx=1,6
    x=random.randint(mx,Mx);z=[chs[random.randint(0,N)] for i in ' '*x]
    a=LtoS(z)
    x=random.randint(mx,Mx);z=[chs[random.randint(0,N)] for i in ' '*x]
    b=LtoS(z)
    x=random.randint(mx,Mx);z=[chs[random.randint(0,N)] for i in ' '*x]
    c=LtoS(z)
    return a,b,c

def mys(a,b,c):
    def check(a,b):
        na=len(a)
        nb=len(b)
        rt=[0]*na
        for i in range(na):
            fl=True
            for j in range(min(na-i,nb)):
                if a[i+j]!=b[j] and a[i+j]!='?' and b[j]!='?':
                    fl=False
                    break
            if fl:
                rt[i]=1
        return rt+[1]
    
    def tri_check(idx):
        id1,id2,id3=idx
        a,b,c=[strs[i] for i in idx]
        ab,bc,ac=chMat[id1][id2],chMat[id2][id3],chMat[id1][id3]
        na,nb,nc=map(len,(a,b,c))
        rt=na+nb+nc
        al,ar=na,nb
        for l in range(na+1):
            for r in range(nb+1):
                if ab[l]==1 and bc[r]==1 and (l+r>=na or ac[l+r]==1):
                    #alt=max(na,na+nb+nc-(na-l)-(nb-r))
                    alt=max(na,l+nb,na+nb+nc-(na-l)-(nb-r))
                    if alt<rt:
                        rt=alt
                        al,ar=l,r
            
            if ab[l]==1:
                for r in range(l+nb,na+1):
                    if ac[r]==1:
                        #alt=max(na,na+nb+nc-(na-l)-(nb-r))
                        alt=max(na,r+nc)
                        if alt<rt:
                            rt=alt
                            al,ar=l,r-l
        '''    
        show(a[:al]+b[:ar]+c,' '*(na+nb+nc-len(a[:al]+b[:ar]+c)),rt,(al,ar),ab,bc,ac)
        show(a)
        show(' '*al+b)
        show(' '*(al+ar)+c)
        '''
        return rt
    '''
    a=input()
    b=input()
    c=input()
    '''
    #a,b,c=ran()
    
    na,nb,nc=map(len,(a,b,c))
    ans=10**5
    strs=[a,b,c]
    chMat=[[check(strs[i],strs[j]) if i!=j else [] for j in range(3)]for i in range(3)]
    
    for i in permutations(range(3)):
        x=tri_check(i)
        ans=min(ans,x)
    
    return ans

a=input()
b=input()
c=input()
print(mys(a,b,c))


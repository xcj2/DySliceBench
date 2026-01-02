import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def bisection(l,r,f,left=True,discrete=True):
    eps=1 if discrete else 10**-12
    if((not left)^f(r)): return r if left else r+1
    elif(left^f(l)): return l-1 if left else l
    while(r-l>eps):
        h=(l+r)//2 if discrete else (l+r)/2
        if((not left)^f(h)): l=h
        else: r=h
    return (l+r)/2 if not discrete else l if left else r

class RollingHash(object):
    from random import randint
    __MASK30=(1<<30)-1
    __MASK31=(1<<31)-1
    __MOD=(1<<61)-1
    __base=randint(129,__MASK31)

    def __init__(self,s:str):
        n=len(s)
        H=[0]*(n+1); P=[1]*(n+1)
        for i in range(n):
            H[i+1]=self.__modulo(self.__multiple(H[i],self.__base)+ord(s[i]))
            P[i+1]=self.__modulo(self.__multiple(P[i],self.__base))
        self.__H=H; self.__P=P

    def __multiple(self,a,b):
        au=a>>31
        ad=a&self.__MASK31
        bu=b>>31
        bd=b&self.__MASK31
        m=ad*bu+au*bd
        mu=m>>30
        md=m&self.__MASK30
        return 2*au*bu+mu+(md<<31)+ad*bd

    def __modulo(self,x):
        x=(x&self.__MOD)+(x>>61)
        if(x>self.__MOD): x-=self.__MOD
        return x

    def hash(self,l,r):
        H=self.__H; P=self.__P
        res=H[r]+self.__MOD*3-self.__multiple(H[l],P[r-l])
        if(res<0): return res+self.__MOD
        else: return self.__modulo(res)

def resolve():
    n=int(input())
    s=input()
    rh=RollingHash(s)
    def check(d):
        J={rh.hash(i,i+d):-1 for i in range(n-d+1)}
        for i in range(n-d+1):
            h=rh.hash(i,i+d)
            if(J[h]!=-1):
                if(i-J[h]>=d): return True
            else: J[h]=i
        return False
    print(bisection(0,n,check))
resolve()
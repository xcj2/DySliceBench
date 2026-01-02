def Prime_Factorization(N):
    if N<0:
        R=[[-1,1]]
    else:
        R=[]

    N=abs(N)
    k=2
    while k*k<=N:
        if N%k==0:
            C=0
            while N%k==0:
                C+=1
                N//=k
            R.append([k,C])
        k+=1

    if N!=1:
        R.append([N,1])
    if not R:
        R.append([N,1])

    return R

class Modulo_Error(Exception):
    pass

class Modulo():
    def __init__(self,a,n):
        self.a=a%n
        self.n=n

    def __str__(self):
        return "{} (mod {})".format(self.a,self.n)

    #+,-
    def __pos__(self):
        return self

    def __neg__(self):
        return  Modulo(-self.a,self.n)

    #等号,不等号
    def __eq__(self,other):
        if isinstance(other,Modulo):
            return (self.a==other.a) and (self.n==other.n)
        elif isinstance(other,int):
            return (self-other).a==0

    def __neq__(self,other):
        return not(self==other)

    #加法
    def __add__(self,other):
        if isinstance(other,Modulo):
            if self.n!=other.n:
                raise Modulo_Error("異なる法同士の演算です.")
            return Modulo(self.a+other.a,self.n)
        elif isinstance(other,int):
            return Modulo(self.a+other,self.n)

    def __radd__(self,other):
        if isinstance(other,int):
            return Modulo(self.a+other,self.n)

    #減法
    def __sub__(self,other):
        return self+(-other)

    def __rsub__(self,other):
        if isinstance(other,int):
            return -self+other

    #乗法
    def __mul__(self,other):
        if isinstance(other,Modulo):
            if self.n!=other.n:
                raise Modulo_Error("異なる法同士の演算です.")
            return Modulo(self.a*other.a,self.n)
        elif isinstance(other,int):
            return Modulo(self.a*other,self.n)

    def __rmul__(self,other):
        if isinstance(other,int):
            return Modulo(self.a*other,self.n)

    #Modulo逆数
    def inverse(self):
        return self.Modulo_Inverse()

    def Modulo_Inverse(self):
        x0, y0, x1, y1 = 1, 0, 0, 1
        a,b=self.a,self.n
        while b != 0:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1

        if a!=1:
            raise Modulo_Error("{}の逆数が存在しません".format(self))
        else:
            return Modulo(x0,self.n)

    #除法
    def __truediv__(self,other):
        return self*(other.Modulo_Inverse())

    def __rtruediv__(self,other):
        return other*(self.Modulo_Inverse())

    #累乗
    def __pow__(self,m):
        u=abs(m)

        r=Modulo(pow(self.a,m,self.n),self.n)
        if m>=0:
            return r
        else:
            return r.Modulo_Inverse()

#法の合成
def __modulo_composite__(p,q):
    from math import gcd

    a,n=p.a,p.n
    b,m=q.a,q.n

    d=b-a
    g=gcd(n,m)

    if d%g:
        raise Modulo_Error("{}と{}は両立しません.".format(p,q))

    n//=g
    m//=g
    d//=g

    s=(Modulo(1,m)/Modulo(n,m)).a

    return Modulo(a+(n*g)*d*s,n*m*g)


def Modulo_Composite(*X):
    from functools import reduce
    return reduce(__modulo_composite__,X)
#=======================================
N=int(input())

if N==1:
    print(1)
    exit()

R=Prime_Factorization(N)

X=[]
for (p,e) in R:
    if p==2:
        X.append(2**(e+1))
    else:
        X.append(p**e)

Y=[Modulo(0,1) for x in X]
M=float("inf")
for s in range(1<<len(X)):
    t=s
    for k in range(len(X)):
        if t&1:
            Y[k]=Modulo(0,X[k])
        else:
            Y[k]=Modulo(-1,X[k])
        t>>=1

    Z=Modulo_Composite(*Y)
    if Z!=0:
        M=min(M,Z.a)
    else:
        M=min(M,Z.n)
print(M)
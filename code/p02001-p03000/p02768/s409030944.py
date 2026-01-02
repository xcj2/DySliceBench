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
        return self*other.Modulo_Inverse()

    #累乗
    def __pow__(self,m):
        u=abs(m)

        r=Modulo(1,self.n)

        while u>0:
            if u%2==1:
                r*=self
            self*=self
            u=u>>1

        if m>=0:
            return r
        else:
            return r.Modulo_Inverse()

#-------------------------------------------------------------------------
M=10**9+7
n,a,b=map(int,input().split())
C=[Modulo(1,M)]*(b+1)

for k in range(1,b+1):
    C[k]=C[k-1]*Modulo(n-(k-1),M)/Modulo(k,M)

print((Modulo(2,M)**n-(C[a]+C[b])-1).a)

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
        return self*(other.Modulo_Inverse())
    
    def __rtruediv__(self,other):
        return other*(self.Modulo_Inverse())

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

    #根号
    def sqrt(self):
        if self==0:
            return self
        elif self.n==2:
            return self
        elif self.n%4==3:
            return self**((self.n+1)//4)
        else:
            p=self.n
            u=2
            s=1
            while (p-1)%(2*u)==0:
                u*=2
                s+=1

            z=Modulo(2,p)
            while z**((p-1)//2)!=-1:
                z+=1

            q=(p-1)//u
            m=s
            c=z**q
            t=self**q
            r=self**((q+1)//2)

            while m>1:
                k=1
                d=t*t

                while d!=1:
                    k+=1
                    d*=d
                    print(m,k)
                b=Modulo(2,p)**(2**(m-k-1))
                c,t,r,m=b*b,t*b*b,r*b,k
            return r
#=======================================
N,M=map(int,input().split())
K=10**9+7
if abs(N-M)>=2:
    print(0)
elif abs(N-M)==1:
    N,M=max(N,M),min(N,M)
    P=Modulo(1,K)
    for i in range(1,M+1):
        P*=i
    print((P*P*N).a)
else:
    P=Modulo(1,K)
    for i in range(1,M+1):
        P*=i
    print((P*P*2).a)
          

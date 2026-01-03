def gcd(n,m):#n,mは正の整数、最大公約数　許容は？
    if n==0:
        return m
    elif m==0:
        return n
    elif n>m:
        n=n%m
        return gcd(n,m)
    else:
        m=m%n
        return gcd(n,m)
def lcm(n,m):
    return n*m//gcd(n,m)


def longlcm(A):
    import copy
    if len(A)==2:
        return A[0]*A[1]//gcd(A[0],A[1])
    else:
        x=A[0]
        for i in range(1,len(A)):
            x=lcm(x,A[i])
        return x

N=int(input())
T=[0]*N
for i in range(0,N):
    T[i]=int(input())

print(longlcm(T))
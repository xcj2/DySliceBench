import sys
import math
import random

def isPrime(q):
    if q==2:
        return True
    if q<2:
        return False
    if pow(2,q-1,q)==1:
        return True
    else:
        return False

def f(x,c,n):
    return (x**2+c)%n

def rho(n):
    x=random.randint(0,n-1)
    y=random.randint(0,n-1)
    c=random.randint(1,n-3)
    d=math.gcd(abs(x-y),n)
    while d==1:
        print(d)
        x=f(x,c,n)
        y=f(y,c,n)
        y=f(y,c,n)
        d=math.gcd(abs(x-y),n)
        if d==n:
            break

    return d


def main():
    N=int(input())

    P={}

    # d=rho(N)
    # P[d]=1
    #
    # while N>d:
    #     N=N//d
    #     d=rho(N)
    #     if (d in P.keys()):
    #         P[d]+=1
    #     else:
    #         P[d]=1

    if isPrime(N):
        print("1")
        sys.exit()

    for i in range(2,N):
        if N%i==0:
            P[i]=1
            N=N//i
            while N%i==0:
                N=N//i
                P[i]+=1
            if isPrime(N):
                P[N]=1
                break
        if N==1:
            break

    counter=1
    res=0
    KEY=list(P.keys())
    while len(KEY)>0:
        for i in KEY:
            if P[i]-counter>=0:
                res+=1
                P[i]=P[i]-counter
            else:
                KEY.remove(i)
                P.pop(i,None)
        counter+=1

    print(res)


if __name__ == "__main__":
    main()
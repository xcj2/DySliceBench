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


def partions(M):#Mの約数列 O(n^(0.5+e))
    import math
    d=[]
    i=1
    while math.sqrt(M)>=i:
        if M%i==0:
            d.append(i)
            if i**2!=M:
                d.append(M//i)
        i=i+1
    d.sort()
    return d

def main():
    A,B,K=map(int,input().split())
    c=gcd(A,B)
    C=partions(c)
    print(C[len(C)-K])

if __name__ == '__main__':
    main()
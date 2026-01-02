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

def ord(N,n):#N,nは正の整数、Nで割り切れる回数、許容はN^1000
    if n%N!=0:
        return 0
    else:
        return 1+ord(N,n//N)

def get_sieve_of_eratosthenes_new(n):
    import math
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

primelist=get_sieve_of_eratosthenes_new(10**6)

A,B=map(int,input().split())
x=gcd(A,B)
count=1

for i in range(0,len(primelist)):
    if x%primelist[i]==0:
        count+=1
        x=x//primelist[i]**ord(primelist[i],x)
if x!=1:
    count+=1
print(count)
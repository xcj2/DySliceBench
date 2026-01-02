#!/mnt/c/Users/moiki/bash/env/bin/python
# N,M = map(int, input().split())
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

BIT = Bit(10**5+1)

plist = primes(10**5+1)
# print(plist)
pp = []
for p in plist[1:]:
    if (p+1) //2 in plist:
        pp.append( p )
        BIT.add(p,1)
# print(pp)

Q = int(input())
for i in range(Q):
    l,r = map(int,input().split())
    if l in pp:
        l-=1
    if r in pp:
        r+=1
    print( BIT.sum(r) - BIT.sum(l) )

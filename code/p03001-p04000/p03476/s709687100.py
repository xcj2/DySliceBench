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


import math

def mirror_prime(n):
    answer = True
    # Test 0 and 1
    if n==0 or n==1:
        answer = False
    # End if

    # Test even numbers
    if n != 2 and n%2==0:
        answer= False
    # End if

    # Test if there is a proper odd divisor
        for d in range (3, int(math.sqrt(n))+1, 2):
            if n%d==0:
                answer=False
            # End if
        # End for



    #Reverse n
    mirror_n = int(str(n)[::-1])
    mirror_answer = True

    # Test 0 and 1
    if mirror_n==0 or mirror_n==1:
        mirror_answer = False

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

# BIT = Bit(10**5+1)

isprime = None
 
def sieve(n):
    global isprime
 
    if n < 2:
        isprime = [False] * (n + 1)
        return
 
    isprime = [True if i % 2 != 0 else False for i in range(n + 1)]
    isprime[0] = isprime[1] = False
    isprime[2] = True
 
    from math import sqrt, ceil
 
    for i in range(3, int(sqrt(n)) + 1):
        if isprime[i] == True:
            for j in range(i + i, n + 1, i):
                isprime[j] = False

# plist = primes(10**5+1)
sieve(10**5+1)


accm = [0] * (10**5+1)
for i in range(3, 10**5+1):
    accm[i] += accm[i-1]
    # if mirror_prime(i) and mirror_prime((i+1)//2):
    if isprime[i] and isprime[(i+1)//2]:
        accm[i] += 1

Q = int(input())
for i in range(Q):
    l,r = map(int,input().split())
    # if mirror_prime(l) and mirror_prime((l+1)//2):
    if isprime[l] and isprime[(l+1)//2]:
        l-=1
    # if mirror_prime(r) and mirror_prime((r+1)//2):
    if isprime[r] and isprime[(r+1)//2]:
        r+=1
    print( accm[r] - accm[l] ) 

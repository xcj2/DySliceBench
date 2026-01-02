import math as mt
import sys
import bisect
input=sys.stdin.readline
#t=int(input())
t=1

# Python 3 program to answer queries 
# of nCr in O(1) time. 
N = 1000001
  
# array to store inverse of 1 to N 
factorialNumInverse = [None] * (N + 1) 
  
# array to precompute inverse of 1! to N! 
naturalNumInverse = [None] * (N + 1) 
  
# array to store factorial of  
# first N numbers 
fact = [None] * (N + 1) 
  
# Function to precompute inverse of numbers 
def InverseofNumber(p): 
    naturalNumInverse[0] = naturalNumInverse[1] = 1
    for i in range(2, N + 1, 1): 
        naturalNumInverse[i] = (naturalNumInverse[p % i] * 
                                   (p - int(p / i)) % p) 
  
# Function to precompute inverse  
# of factorials 
def InverseofFactorial(p): 
    factorialNumInverse[0] = factorialNumInverse[1] = 1
  
    # precompute inverse of natural numbers 
    for i in range(2, N + 1, 1): 
        factorialNumInverse[i] = (naturalNumInverse[i] * 
                                  factorialNumInverse[i - 1]) % p 
  
# Function to calculate factorial of 1 to N 
def factorial(p): 
    fact[0] = 1
  
    # precompute factorials 
    for i in range(1, N + 1): 
        fact[i] = (fact[i - 1] * i) % p 
  
# Function to return nCr % p in O(1) time 
def Binomial(N, R, p): 
      
    # n C r = n!*inverse(r!)*inverse((n-r)!) 
    ans = ((fact[N] * factorialNumInverse[R])% p * 
                      factorialNumInverse[N - R])% p 
    return ans 
p = 1000000007
InverseofNumber(p) 
InverseofFactorial(p) 
factorial(p)
x1=10**6+1


mod=10**9+7
for _ in range(t):
    
    n=int(input())
    #a,b,c,d=map(int,input().split())
    #u1,d1=map(int,input().split())
    #u2,d2=map(int,input().split())
    #l=list(map(int,input().split()))
    ans=0
    i=1
    while n-i*3>=0:
        ans=(ans%mod+Binomial(n-3*i+i-1, i-1, p))%mod
        i+=1
    print(ans%mod)    
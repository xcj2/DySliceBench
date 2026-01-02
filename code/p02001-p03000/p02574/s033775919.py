import math
from functools import reduce

N=int(input())
T=list(map(int,input().split()))

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0 :
            if i!=1:
                divisors.append(i)
            if i != n // i:

                divisors.append(n//i)

    divisors.sort()
    return divisors

    


def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)
S=[]
tmp=gcd_list(T)
if tmp!=1:
    print("not coprime")
else:
    T.sort()

    n=10**6+1
    isprime=[True]*(n+1)
    isprime[0]=False
    isprime[1]=False
    for i in range(len(T)):
        S=make_divisors(T[i])
        #print(S)
        while len(S)!=0: 
            tmp=S.pop()
            if isprime[tmp]==True:
                j=tmp+tmp
                while j<=n:
                     
                    isprime[j] =False
                    j=j+tmp
                    
                        
            else:
                print("setwise coprime")
                exit()
    print("pairwise coprime")
    
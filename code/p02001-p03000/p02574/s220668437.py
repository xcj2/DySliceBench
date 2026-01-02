def max(a,b):
    if a>b:
        return a
    else:
        return b
 
def min(a,b):
    if a>b:
        return b
    else:
        return a
 
def gcd(a,b):
    a,b = max(a,b),min(a,b)
    while a%b!=0:
        a,b = b,a%b
    return b
 
 
def gcdl(A):
    if len(A)==2:
        return gcd(A[0],A[1])
    elif len(A)==1:
        return A[0]
    else:
        return gcd(gcdl(A[:len(A)//2]),gcdl(A[len(A)//2:]))


def sieve_of_eratosthenes(n):
    p = 2
    D = [0]*(n+1)
    while p**2<=n:
        if D[p]==0:
            k = p*p
            while k <= n:
                if D[k] == 0:
                    D[k] = p
                k += p
        p+=1
    return D

import sys

sys.setrecursionlimit(500000)
def input():
    return sys.stdin.readline()[:-1]

def main():
    D = sieve_of_eratosthenes(1000000)
    #print(D)
    N = int(input())
    A = list(map(int,input().split()))

    F = set([])
    flag = True
    for a in A:
        b = a
        fact = set([])
        while D[b]>0:
            fact.add(D[b])
            b//=D[b]
        if b!=1:
            fact.add(b)
        for p in fact:
            if p in F:
                flag=False
                break
            else:
                F.add(p)

    if flag:
        print("pairwise coprime")
    else:
        if gcdl(A)==1:
            print("setwise coprime")
        else:
            print("not coprime")

if __name__ == '__main__':
    main()


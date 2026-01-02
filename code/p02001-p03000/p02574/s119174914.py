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

from collections import defaultdict
def factorize(n,dd):
    #print(int(n**0.5))
    for i in range(2,int(n**0.5)+1):
        flag=True
        while n%i==0 and n>0:
            if flag:
                if dd[i]>0:
                    return False
                else:
                    flag=False
            dd[i]+=1
            n//=i
    if n>1:
        if dd[n]>0:
            return False
        dd[n]+=1
    #print(dd)
    return True

def gcdl(A):
    if len(A)==2:
        return gcd(A[0],A[1])
    elif len(A)==1:
        return A[0]
    else:
        return gcd(gcdl(A[:len(A)//2]),gcdl(A[len(A)//2:]))

import sys

sys.setrecursionlimit(500000)
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())

    A = list(map(int,input().split()))

    B = [a for a in A if a!=1]

    if len(B)<=1:
        print("pairwise coprime")
    else:
        N = len(B)
        if N>78498:
            if len(B)!=len(A):
                print("setwise coprime")
            else:
                print("not coprime")
        else:
            dd = defaultdict(int)
            flag=True
            for b in B:
                if factorize(b,dd)==False:
                    flag=False
                    break
            if flag:
                print("pairwise coprime")
            else:
                if len(B)!=len(A):
                    print("setwise coprime")
                elif gcdl(B)==1:
                    print("setwise coprime")
                else:
                    print("not coprime")        
        
if __name__ == '__main__':
    main()


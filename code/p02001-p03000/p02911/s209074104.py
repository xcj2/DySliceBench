import math
import queue

mod = 1e9+7

def swap(a,b):
    return (b,a)

def gcd(a,b):
    if (a<b):
        a,b = swap(a,b)
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

def divisors(a):
    divisors = []
    for i in range(1,int(a**0.5)+1):
        if a%i==0:
            divisors.append(i)
            if i!=a//i:
                divisors.append(a//i)
    return divisors

def main():
    n,k,q = map(int,input().split())
    p = [0 for i in range(n)]
    for i in range(q):
        a = int(input())
        p[a-1] += 1
    for i in range(n):
        if k-q+p[i]>0:
            print("Yes")
        else:
            print("No")
    return

if __name__ == '__main__':
    main()
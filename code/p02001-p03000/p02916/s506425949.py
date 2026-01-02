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
    n = int(input())
    a = [x for x in map(int,input().split())]
    b = [x for x in map(int,input().split())]
    c = [x for x in map(int,input().split())]
    eat = n+1
    ans = 0
    for i in range(n):
        ans += b[a[i]-1]
        if a[i]==eat+1:
            ans += c[a[i]-2]
        eat = a[i]
    print(ans)
    return

if __name__ == '__main__':
    main()
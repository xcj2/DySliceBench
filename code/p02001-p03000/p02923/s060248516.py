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
    h = [x for x in map(int,input().split())]
    h.insert(0,0)
    x = []
    for i in range(1,n+1):
        if h[i]<=h[i-1]:
            x.append(x[-1]+1)
        else:
            x.append(0)
    print(max(x))
    return

if __name__ == '__main__':
    main()
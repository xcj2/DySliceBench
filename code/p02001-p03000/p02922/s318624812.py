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
    a,b = map(int,input().split())
    x = 1
    ans = 0
    while x<b:
        x += a-1
        ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
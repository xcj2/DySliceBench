import math
import queue
import bisect
import heapq

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
    n,m = map(int,input().split())
    a = [-x for x in map(int,input().split())]
    heapq.heapify(a)
    for i in range(m):
        x = heapq.heappop(a)
        if x%2==0:
            heapq.heappush(a,x//2)
        else:
            heapq.heappush(a,x//2+1)
    ans = 0
    for i in range(n):
        ans += heapq.heappop(a)*(-1)
    print(ans)
    return

if __name__ == '__main__':
    main()
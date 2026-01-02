import math
import queue
import bisect
import heapq
import time
import itertools

mod = 1e9+7
global a,n,xy,ans

def swap(a,b):
    return (b,a)

def gcd(a,b): #最大公約数
    if (a<b):
        a,b = swap(a,b)
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

def divisors(a): # 約数列挙
    divisors = []
    for i in range(1,int(a**0.5)+1):
        if a%i==0:
            divisors.append(i)
            if i!=a//i:
                divisors.append(a//i)
    return divisors

def is_prime(a): #素数判定
    if a<2:
        return False
    elif a==2:
        return True
    elif a%2==0:
        return False
    sqrt_num = int(a**0.5)
    for i in range(3,sqrt_num+1,2):
        if a%i==0:
            return False
    return True

def prime_num(a): #素数列挙
    pn = [2]
    for i in range(3,int(a**0.5),2):
        prime = True
        for j in pn:
            if i%j==0:
                prime = False
                break
        if prime:
            pn.append(i)
    return pn


def func():
    global a,n,xy,ans
    count = 0
    for i in range(n):
        for j in xy[i]:
            if a[i]:
                if a[j[0]]!=j[1]:
                    return
        if a[i]:
            count += 1
    ans = max(ans,count)

def dfs(pos):
    global n
    if pos==n:
        func()
        return
    a[pos] = 0
    dfs(pos+1)
    a[pos] = 1
    dfs(pos+1)

def main():
    global a,n,xy,ans
    n = int(input())
    xy = []
    for i in range(n):
        a = int(input())
        xy.append([])
        for j in range(a):
            x,y = map(int,input().split())
            xy[i].append([x-1,y])
    a = [0 for i in range(n)]
    ans = 0
    dfs(0)
    print(ans)
    return

if __name__=='__main__':
    main()

import math
import queue
import bisect
import heapq
import time
import itertools

mod = int(1e9+7)

def swap(a,b):
    return (b,a)

def gcd(a,b): #最大公約数
    if (a<b):
        a,b = swap(a,b)
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b): #最小公倍数
    return a/gcd(a,b)*b

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

def prime_fact(a): #素因数分解
    sqrt = math.sqrt(a)
    res = []
    i = 2
    if is_prime(a):
        res.append(a)
    else:
        while a!=1:
            while a%i==0:
                res.append(i)
                a //= i
            i += 1
    return res

def main():
    n = int(input())
    p = [x for x in map(int,input().split())]
    q = [x for x in map(int,input().split())]
    if p == q:
        print(0)
        return
    nums = [i+1 for i in range(n)]
    cnt = 1
    l = 0
    h = 0
    for x in itertools.permutations(nums):
        y = [z for z in x]
        if y == p:
            l = cnt
        elif y == q:
            h = cnt
        cnt += 1
    print(abs(l-h))
    return

if __name__=='__main__':
    main()

import math
import queue
import bisect
import heapq
import time
import itertools

mod = 1e9+7

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

def main():
    x = int(input())
    if x<100:
        print(0)
        return
    buy = x//100
    sur = x%100
    num = (sur+4)//5
    if num<=buy:
        print(1)
    else:
        print(0)
    return

if __name__=='__main__':
    main()

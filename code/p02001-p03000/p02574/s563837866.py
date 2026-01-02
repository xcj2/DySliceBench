import bisect
import collections
import copy
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
MOD = 10**9+7

N = int(input())
A = list(map(int,input().split()))

one = A.count(1)

def find_prime(n):
    prime_list = []
    find_list = list(range(2,n+1))
    while True:
        if find_list[0] > n**(1/2):
            prime_list.extend(find_list)
            break
        else:
            head = find_list[0]
            prime_list.append(head)
            find_list.pop(0)
            find_list = [num for num in find_list if num % head != 0]
    return prime_list

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i ==0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def multiple(a, b):
    return a*b // euclid(a, b)

def gcd(nums):
    return functools.reduce(euclid, nums)

if gcd(A) != 1:
    print("not coprime")

else:
    """
    flag = 0
    M = [False]*(10**6+1)
    for i in range(N):
        n = A[i]
        if M[n]:
            flag = 1
            break
        if n != 1:
            k = 1
            while n*k <= 10**6:
                M[n*k] = True
                k += 1
    """
    flag = 0

    if N-one <= 78500:
        M = [False]*(10**6+1)
        for i in range(N):
            n = A[i]
            if n == 1:
                continue
            l = factorization(n)
            for j in range(len(l)):
                p = l[j][0]
                if M[p]:
                    flag = 1
                    break
                M[p] = True
    else:
        flag = 1
    
    if flag == 0:
        print("pairwise coprime")
    else:
        print("setwise coprime")
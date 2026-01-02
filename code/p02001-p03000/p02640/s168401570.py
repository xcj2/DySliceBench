import collections
import itertools
import math
import statistics
import datetime
from bisect import bisect_left
import heapq

__author__ = 'sudoplox // Sudhanshu'
__contact__ = "sudoplox[at]gmail.com"


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


def ngreatestelem(lis, n):
    return heapq.nlargest(n, lis)


def nsmallestelem(lis, n):
    return heapq.nsmallest(n, lis)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def sieve():
    # Complexity: O(n * log2(log2(n)))
    primes[1] = 1
    primes[2] = 2
    j = 4
    while j < 1000000:
        primes[j] = 2
        j += 2
    j = 3
    while j < 1000000:
        if primes[j] == 0:
            primes[j] = j
            i = j * j
            k = j << 1
            while i < 1000000:
                primes[i] = j
                i += k
        j += 2


def possiblepermutations(lis):
    return itertools.permutations(lis)


sieve = False
if sieve:
    primes = [0] * 1000000

# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     arr = list(map(int, input().split(" ")))

def solve(n,k):
    for i in range(0, n + 1):
        if i * 2 + 4 * (n - i) == k:
            return("Yes")
    return ("No")

n,k=map(int, input().split(" "))
print(solve(n,k))

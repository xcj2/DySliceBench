import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
# from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')
from decimal import Decimal
# from fractions import Fraction
# sys.setrecursionlimit(100000)
INF = float('inf')
mod = int(1e9) + 7

n=int(data())
a = mdata()
N=10**6 + 1
lpf = [0 for i in range(N)]
mobius = [0 for i in range(N)]


# Function to calculate least
# prime factor of each number
def least_prime_factor():
    for i in range(2, N):

        # If it is a prime number
        if (lpf[i] == 0):

            for j in range(i, N, i):

                # For all multiples which are not
                # visited yet.
                if (lpf[j] == 0):
                    lpf[j] = i

                # Function to find the value of Mobius function


# for all the numbers from 1 to n
def Mobius():
    for i in range(1, N):

        # If number is one
        if (i == 1):
            mobius[i] = 1
        else:

            # If number has a squared prime factor
            if (lpf[(i // lpf[i])] == lpf[i]):
                mobius[i] = 0

            # Multiply -1 with the previous number
            else:
                mobius[i] = -1 * mobius[i // lpf[i]]

            # Function to find the number of pairs


# such that gcd equals to 1
def gcd_pairs(a, n):
    # To store maximum number
    maxi = 0

    # To store frequency of each number
    fre = [0 for i in range(N)]

    # Find frequency and maximum number
    for i in range(n):
        fre[a[i]] += 1
        maxi = max(a[i], maxi)

    least_prime_factor()
    Mobius()

    # To store number of pairs with gcd equals to 1
    ans = 0

    # Traverse through the all possible elements
    for i in range(1, maxi + 1):
        if (mobius[i] == 0):
            continue

        temp = 0
        for j in range(i, maxi + 1, i):
            temp += fre[j]

        ans += temp * (temp - 1) // 2 * mobius[i]

        # Return the number of pairs
    return ans


# Driver code


# Function call
g=a[0]
for i in range(n):
    g=math.gcd(g,a[i])
    if g==1:
        break
if gcd_pairs(a, n) == (n*(n-1))//2:
    out("pairwise coprime")
elif g==1:
    out("setwise coprime")
else:
    out("not coprime")
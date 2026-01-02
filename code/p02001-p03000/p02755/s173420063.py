from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

# List of ints
def LI(): return list(map(int, sys.stdin.readline().split()))

# Single int
def I(): return int(sys.stdin.readline())

# List, which contains Lists of chars (not strings)
def LS():return list(map(list, sys.stdin.readline().split()))

# Single List of chars (not strings)
def S(): return list(sys.stdin.readline())[:-1]

# List of "n" integers from "n" lines.
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
# List of "n" Lists of integers
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LS()
    return l


# Runtime Complexity: O(?)
# Space Complexity: O(?)
# Solution
A, B = LI()

low = 0
high = A * 12.5 + B * 10

min_price = float('inf')

while low <= high:
    mid = low + ((high - low) // 2)

    a = math.floor(mid * 0.08)
    b = math.floor(mid * 0.1)

    if a < A or b < B:
        low = mid + 1
    elif a == A and b == B:
        min_price = mid
        high = mid - 1
    elif a > A or b > B:
        high = mid - 1

if min_price == float('inf'):
    print(-1)
else:
    print(int(min_price))
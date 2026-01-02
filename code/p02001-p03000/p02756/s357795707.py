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
s = sys.stdin.readline().split()[0]
lines_count = I()

chars = deque(s)

def prepend(chars, ch):
    chars.appendleft(ch)

def append(chars, ch):
    chars.append(ch)

actions = {
    1: prepend,
    2: append
}

for i in range(lines_count):
    line = LS()

    if len(line) == 1:
        actions[1], actions[2] = actions[2], actions[1]
    else:
        if line[1][0] == '1':
            actions[1](chars, line[2][0])
        else:
            actions[2](chars, line[2][0])

chars = list(chars)
if actions[1] == append:
    chars.reverse()

print(''.join(chars))
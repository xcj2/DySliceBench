
import sys

readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return tuple(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))


n = readint()
p = readints()
q = readints()

from itertools import permutations

a = 0
b = 0

for i,x in enumerate(permutations(range(1,n+1),n)):
    if x == p:
        a = i
    if x == q:
        b = i
print(abs(a-b))
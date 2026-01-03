import sys
import math

INF = 10**9+7

def k(i):
    if(i == 1):
        return 1
    else:
        return(i * k(i-1))

def comb(n, r):
    if(n == r or r == 1):
        return 1
    else:
        return k(n) / (k(n-r) * k(r))

stdin = sys.stdin
def na(): return map(int, stdin.readline().split())
def ns(): return stdin.readline().strip()
def nsl(): return list(stdin.readline().strip())
def ni(): return int(stdin.readline())
def nil(): return list(map(int, stdin.readline().split()))

a = ns()
b = ns()


an = len(a)
bn = len(b)


if(an > bn):
    print("GREATER")
    exit()
elif(an < bn):
    print("LESS")
    exit()

for i in range(an):
    if(a[i] > b[i]):
        print("GREATER")
        exit()
    elif(b[i] > a[i]):
        print("LESS")
        exit()

print("EQUAL")

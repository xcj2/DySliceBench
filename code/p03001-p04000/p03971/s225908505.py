import sys, itertools, fractions, math, collections, heapq
sys.setrecursionlimit(10**7)
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

n, a, b = LI()
s = list(input())

aq, bq = 0, 0
for ss in s:
    if ss=='a':
        if aq + bq < a+b:
            print('Yes')
            aq+=1
        else:
            print('No')
    if ss=='b':
        if aq + bq < a+b and bq+1<=b:
            print('Yes')
            bq+=1
        else:
            print('No')
    if ss=='c':
        print('No')

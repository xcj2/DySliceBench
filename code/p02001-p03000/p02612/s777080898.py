from sys import stdin, setrecursionlimit, stdout
#setrecursionlimit(1000000) #use "python" instead of "pypy" to avoid MLE
#from collections import deque
#from math import sqrt, floor, ceil, log, log2, log10, pi, gcd, sin, cos, asin
#from heapq import heapify, heappop, heappush, heapreplace, heappushpop
def ii(): return int(stdin.readline())
def fi(): return float(stdin.readline())
def mi(): return map(int, stdin.readline().split())
def fmi(): return map(float, stdin.readline().split())
def li(): return list(mi())
def si(): return stdin.readline().rstrip()
def lsi(): return list(si())
#mod=1000000007
res=['YES', 'NO']





test_case=1
while test_case:
    test_case-=1




    n=ii()+999
    x=n//1000
    print(x*1000-n+999)
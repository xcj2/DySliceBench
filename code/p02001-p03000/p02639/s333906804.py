from sys import stdin
#, setrecursionlimit, stdout
#setrecursionlimit(1000000)
#from collections import deque
#from math import sqrt, floor, ceil, log, log2, log10, pi, gcd, sin, cos, asin
def ii(): return int(stdin.readline())
def fi(): return float(stdin.readline())
def mi(): return map(int, stdin.readline().split())
def fmi(): return map(float, stdin.readline().split())
def li(): return list(mi())
def si(): return stdin.readline().rstrip()
def lsi(): return list(si())
#mod=1000000007
res=['Yes', 'No']
############# CODE STARTS HERE #############

test_case=1
while test_case:
    test_case-=1

    a=li()
    print(a.index(0)+1)
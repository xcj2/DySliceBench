#https://agc023.contest.atcoder.jp/submissions/2429958
import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def main():
    n,x = LI()
    m = [I() for _ in range(n)]
    r = x
    for i in range(n):
        r = r - m[i]
    r = r // (min(m)) + n

    return r

print(main())
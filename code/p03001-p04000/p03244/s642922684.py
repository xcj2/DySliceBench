import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys

sys.setrecursionlimit(10**7)
mod = 10**9+7
inf = 10**20

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def counter_top(c,exclude):
    for a in c.most_common():
        if a[0]!=exclude:
            return a
    return (object(),0)

def conv_seq(seq,exclude = None):
    c = collections.Counter(seq)
    mc = counter_top(c,exclude)
    return sum(c.values()) - mc[1],mc[0]

N = I()
V = LI()

s1,a = conv_seq(V[::2])
s2,b = conv_seq(V[1::2])


if s1!=s2:
    print(s1+s2)
else:
    s1_new,_ = conv_seq(V[::2],exclude=b)
    s2_new,_ = conv_seq(V[1::2],exclude=a)
    print(min(s1_new+s2,s1+s2_new))

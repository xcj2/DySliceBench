import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def time_to_zero(n, carry):
    ans = 0
    amari = 0
    if n % carry:
        amari = 1
    return n // carry + amari

def main():
    N = I()
    l = []
    ans = 0
    for i in range(5):
        al = I()
        l.append(al)
    A, B, C, D, E = l
    m = min(l)
    minute = 0
    if N % m != 0:
        minute += 1
    minute += N // m
    minute += 4
    print(minute)
    # city_capa = N
    # prev_tr_capa = A
    # for tr_capa, next_tr_capa in zip(l, l[1:]+[0]):
    #     t = time_to_zero(city_capa, tr_capa)
    #     city_capa = city_capa - (t-1) * min(tr_capa, next_tr_capa)
    #     ans += t
    # print(ans)
main()


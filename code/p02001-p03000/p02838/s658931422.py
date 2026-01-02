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
     
def main():
    N = I()
    A = LI()
    digit_count_one = [0] * 61
    nums = N * (N-1) // 2
    cnt = 0
    for a in A:
        for i in range(61):
            c = (a >> i) & 1
            if c == 1:
                digit_count_one[i] += 1
    for ix, count in enumerate(digit_count_one):
        freq = count * (N - count)
        cnt += ((1 << ix) * freq) % mod
        cnt %= mod
    print(cnt % mod)
main()


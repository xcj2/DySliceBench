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

def get_yakusu_list(N):
    yakusu = []
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            yakusu.append(i)
            if N // i != i:
                yakusu.append(N//i)
    yakusu = sorted(yakusu)
    return yakusu

def main():
    N, M = LI()
    yakusu = get_yakusu_list(M)
    for ko in yakusu[::-1]:
        if M // ko >= N:
            break
    print(ko)

main()


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

def fillzerostr(n):
    s = str(n)
    while len(s) < 6:
        s = '0' + s
    return s

def main():
    N, M = LI()
    py = []
    py_original = []
    memo = {}
    for _ in range(M):
        P, Y = LI()
        py.append((P, Y))
        py_original.append((P, Y))

    py = sorted(py, key=lambda x: (x[0], x[1]))
    prev_ken = 0
    order = 1
    for i in range(M):
        ken = py[i][0]
        year = py[i][1]
        if prev_ken == ken:
            order += 1
        else:
            order = 1
        memo[py[i]] = fillzerostr(ken) + fillzerostr(order)
        prev_ken = ken

    for i in range(M):
        print(memo[py_original[i]])

main()


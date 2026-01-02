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
    H, W = LI()
    a = []
    excrow = set()
    exccol = set()
    for _ in range(H):
        a.append(S())
    for row in range(H):
        all_white = True
        for c in a[row]:
            if c == '#':
                all_white = False
                break
        if all_white:
            excrow.add(row)

    for col in range(W):
        all_white = True
        for r in range(H):
            if a[r][col] == '#':
                all_white = False
                break
        if all_white:
            exccol.add(col)

    newA = []
    for row in range(H):
        if row in excrow:
            continue
        newA.append(a[row])

    newnewA = []
    for row in range(len(newA)):
        string = ''
        for col in range(W):
            if col in exccol:
                continue
            string += newA[row][col]
        newnewA.append(string)
    print('\n'.join(newnewA))


main()


from collections import *
from heapq import *
import sys

sys.setrecursionlimit(10 ** 5)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]
dij = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def main():
    s=SI()
    cnt0=s.count("0")
    cnt1=len(s)-cnt0
    print(min(cnt0,cnt1)*2)

main()

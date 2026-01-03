import sys
from heapq import *

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n,k=MI()
    hp=[]
    for _ in range(n):
        a,b=MI()
        heappush(hp,[a,b])
    s=0
    while 1:
        a,b=heappop(hp)
        s+=b
        if s>=k:
            print(a)
            break
main()
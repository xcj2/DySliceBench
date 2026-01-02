import sys
from collections import Counter

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n=II()
    aa=LI()
    ac=Counter(aa)
    s=sum(c*(c-1)//2 for a,c in ac.items())
    for a in aa:
        c=ac[a]
        print(s-c*(c-1)//2+(c-1)*(c-2)//2)

main()
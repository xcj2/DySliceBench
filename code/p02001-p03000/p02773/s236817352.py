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
    ss=[SI() for _ in range(n)]
    cnt=Counter(ss)
    pv=-1
    for s,v in sorted(cnt.items(),key=lambda x:(-x[1],x[0])):
        if v!=pv and pv!=-1:break
        print(s)
        pv=v

main()
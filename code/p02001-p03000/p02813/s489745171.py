import sys
import itertools

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def TI(): return tuple(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n=II()
    p=TI()
    q=TI()
    for i,s in enumerate(itertools.permutations(range(1,n+1))):
        if s==p:a=i
        if s==q:b=i
    print(abs(b-a))
main()
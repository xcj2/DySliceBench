import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

from collections import Counter
def main():
    n=II()
    aa=LI()
    cnt=Counter(aa)
    even=0
    ans=0
    for v in cnt.values():
        if v&1==0:even+=1
        ans+=v//2
    ans-=even//2
    print(n-ans*2)

main()
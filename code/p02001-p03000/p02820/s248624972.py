import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n,k=MI()
    r,s,p=MI()
    t=input()
    ans=0
    for m in range(k):
        pc="a"
        for c in t[m::k]:
            if c==pc:
                pc="a"
                continue
            if c=="r":ans+=p
            if c=="s":ans+=r
            if c=="p":ans+=s
            pc=c
    print(ans)

main()
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n,a,b=MI()
    xx=LI()
    now=xx[0]
    ans=0
    for x in xx[1:]:
        if (x-now)*a<b:ans+=(x-now)*a
        else:ans+=b
        now=x
    print(ans)

main()
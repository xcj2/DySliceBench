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
    n=II()
    aa=LI()
    s=sum(aa)
    if n%2:
        if s%2:ans="First"
        else:ans="Second"
    else:
        mn=min(aa)
        if s%2==0 and mn%2==0:ans="Second"
        else:ans="First"
    print(ans)

main()

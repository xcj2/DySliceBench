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
    def f(a,b):return max(len(str(a)),len(str(b)))
    n=II()
    if n==1:
        print(1)
        exit()
    ans=100
    for d in range(1,n):
        if d**2>n:break
        if n%d==0:
            ans=min(ans,f(d,n//d))
    print(ans)

main()
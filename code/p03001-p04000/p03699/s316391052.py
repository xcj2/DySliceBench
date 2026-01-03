import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n=int(input())
    ss=[int(input()) for _ in range(n)]
    ans=sum(ss)
    if ans%10==0:
        ss.sort()
        for s in ss:
            if s%10:
                ans-=s
                break
        else:
            ans=0
    print(ans)

main()
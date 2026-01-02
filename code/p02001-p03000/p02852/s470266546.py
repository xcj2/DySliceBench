import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n,m=MI()
    s=input()[::-1]
    now=0
    ans=[]
    while now<n:
        for d in range(m,0,-1):
            if now+d>n:continue
            if s[now+d]=="0":
                now+=d
                ans.append(d)
                break
        else:
            print(-1)
            exit()
    print(*ans[::-1])

main()
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n=int(input())
    aa=[int(input())-1 for _ in range(n)]
    b=0
    fin=set()
    ans=0
    for _ in range(n):
        if b in fin:
            print(-1)
            exit()
        if b==1:break
        fin.add(b)
        b=aa[b]
        ans+=1
    print(ans)

main()
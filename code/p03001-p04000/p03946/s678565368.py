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
    n,t=MI()
    aa=LI()
    mn=10**10
    pp=[]
    for a in aa:
        pp.append(a-mn)
        mn=min(mn,a)
    #print(pp)
    ans=pp.count(max(pp))
    print(ans)

main()
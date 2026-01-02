import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def solve(ai,aj,bi,bj):
    s=pow(3,30)
    dist=abs(ai-bi)+abs(aj-bj)
    while s>1:
        s//=3
        si,sj,ti,tj=ai//s,aj//s,bi//s,bj//s
        if si!=ti:
            return dist
        if abs(sj-tj)>1 and si%3==1:
            up=s*si-1
            down=s*(si+1)
            return min(min(ai,bi)-up,down-max(ai,bi))*2+dist
    return dist

def main():
    q=II()
    for _ in range(q):
        ai,aj,bi,bj=MI1()
        if abs(ai-bi)>abs(aj-bj):ai,aj,bi,bj=aj,ai,bj,bi
        print(solve(ai,aj,bi,bj))

main()
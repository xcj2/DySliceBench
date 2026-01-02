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
    k=II()
    run=list(range(1,10))
    cur=list(range(1,10))
    while len(run)<k:
        nxt=[]
        for r in cur:
            e=r%10
            nxt.append(r*10+e)
            run.append(r*10+e)
            if e!=0:
                nxt.append(r*10+e-1)
                run.append(r*10+e-1)
            if e!=9:
                nxt.append(r*10+e+1)
                run.append(r*10+e+1)
        cur=nxt
    run.sort()
    print(run[k-1])

main()
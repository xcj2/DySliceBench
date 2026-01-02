import sys

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n,k=MI()
    a=LI()
    for _ in range(k):
        na=[0]*(n+1)
        for i in range(n):
            l=max(0,i-a[i])
            r=min(n,i+a[i]+1)
            na[l]+=1
            na[r]-=1
        if na[0]==n and na[-1]==-n:
            a=[n]*n
            break
        for i in range(n):
            na[i+1]+=na[i]
        a=na
    print(*a[:n])

main()
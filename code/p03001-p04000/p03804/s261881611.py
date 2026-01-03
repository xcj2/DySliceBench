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
    def ok(i,j):
        for ii in range(m):
            if aa[ii+i][j:j+m]!=bb[ii]:return False
        return True

    n,m=MI()
    aa=[[c=="#" for c in input()] for _ in range(n)]
    bb=[[c=="#" for c in input()] for _ in range(m)]
    for i in range(n-m+1):
        for j in range(n-m+1):
            if ok(i,j):
                print("Yes")
                exit()
    print("No")

main()
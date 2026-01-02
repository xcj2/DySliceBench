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
    def bingo():
        for row in t:
            if sum(row)==3:return True
        for col in zip(*t):
            if sum(col)==3:return True
        if sum(t[i][i] for i in range(3)) == 3: return True
        if sum(t[i][2-i] for i in range(3)) == 3: return True
        return False

    atoij={}
    aa=LLI(3)
    for i in range(3):
        for j in range(3):
            a=aa[i][j]
            atoij[a]=(i,j)
    t=[[False]*3 for _ in range(3)]
    n=II()
    for _ in range(n):
        a=II()
        if a in atoij:
            i,j=atoij[a]
            t[i][j]=True
    if bingo():print("Yes")
    else:print("No")

main()
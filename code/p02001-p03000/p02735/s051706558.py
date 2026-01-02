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
    inf=10**9
    h,w=MI()
    ss=[SI() for _ in range(h)]
    cc=[[0]*w for _ in range(h)]
    if ss[0][0]=="#":cc[0][0]=1
    for i in range(h):
        for j in range(w):
            if (i,j)==(0,0):continue
            u=l=inf
            if i-1>=0:
                u=cc[i-1][j]
                if ss[i][j]=="#" and ss[i-1][j]==".":u+=1
            if j-1>=0:
                l=cc[i][j-1]
                if ss[i][j]=="#" and ss[i][j-1]==".":l+=1
            cc[i][j]=min(u,l)
    print(cc[h-1][w-1])

main()
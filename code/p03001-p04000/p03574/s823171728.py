import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    h, w = MI()
    t = [["."] * (w + 2)] + [["."] + list(input()) + ["."] for _ in range(h)] + [["."] * (w + 2)]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if t[i][j] == "#": continue
            cnt=0
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    if t[ii][jj]=="#":cnt+=1
            t[i][j]=cnt

    for tk in t[1:1+h]:
        print(*tk[1:1+w],sep="")

main()

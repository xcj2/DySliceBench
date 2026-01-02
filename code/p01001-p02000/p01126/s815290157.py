import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    while 1:
        n,m,a=MI()
        if (n,m,a)==(0,0,0):break
        to={}
        max_h=0
        for _ in range(m):
            h,p,q=MI()
            max_h=max(max_h,h)
            to[(h,p)]=q
            to[(h,q)]=p
        i=max_h+1
        j=a
        while i>0:
            i-=1
            if (i,j) in to:j=to[(i,j)]
        print(j)

main()

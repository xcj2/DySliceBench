from collections import deque
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
    n=II()
    t=x=y=0
    for _ in range(n):
        nt,nx,ny=MI()
        d=abs(x-nx)+abs(y-ny)
        dt=nt-t
        if d&1!=dt&1 or d>dt:
            print("No")
            exit()
        t,x,y=nt,nx,ny
    print("Yes")

main()
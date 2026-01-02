import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    prime=[0,1]*500000
    prime[2]=1
    for x in range(3,500000):
        if prime[x]:
            for y in range(x**2,1000000,x):
                prime[y]=0
    x=II()
    for y in range(x,1000000):
        if prime[y]:
            print(y)
            break


main()
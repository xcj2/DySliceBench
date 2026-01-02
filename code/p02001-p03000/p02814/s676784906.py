import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def gcd(x,y):
    while y:x,y=y,x%y
    return x

def lcm(x,y):
    g=gcd(x,y)
    return x*y//g

def main():
    n,m=MI()
    aa=LI()
    aa=[a>>1 for a in aa]
    l=1
    for a in aa:l=lcm(l,a)
    for a in aa:
        if l//a%2==0:
            print(0)
            exit()
    print((m//l+1)//2)

main()
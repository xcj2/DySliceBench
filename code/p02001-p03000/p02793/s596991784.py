import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def gcd(a,b):
    while b:a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def main():
    md=10**9+7
    n=II()
    aa=LI()
    l=1
    for a in aa:
        l=lcm(l,a)
    bb=[]
    for a in aa:
        bb.append(l//a)
    print(sum(bb)%md)

main()
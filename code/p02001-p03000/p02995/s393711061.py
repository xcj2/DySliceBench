import sys
input = sys.stdin.readline
def linput():
    return list(map(int, input().split()))

def gcd(n,m):
    while m:
        n,m = m, n%m
    return n

def lcm(n,m):
    return n*m//gcd(n,m)

def main():
    # N = int(input())
    A,B,C,D = linput()
    # vA = linput()
    # S = input()
    # mX = [linput() for _ in [0,]*N]
    U = B-A+1
    E = lcm(C, D)
    tC = (B//C - A//C) + (A%C==0)
    tD = (B//D - A//D) + (A%D==0)
    tE = (B//E - A//E) + (A%E==0)

    # res = 0
    # res = -(-N//M)

    res = U - tC - tD + tE
    print(res)

main()

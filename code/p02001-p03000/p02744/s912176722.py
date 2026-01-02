import sys
input = sys.stdin.readline

from collections import deque

def linput():
    return list(map(int, input().split()))

def gcd(n,m):
    while m:
        n,m = m, n%m
    return n

def lcm(n,m):
    return n*m//gcd(n,m)

def main():
    N = int(input())
    # N,M = linput()
    # vA = linput()
    # S = input()
    # mX = [linput() for _ in [0,]*N]

    # vR = []
    # vR_app = vR.append

    pp = "a"

    vQ = deque([])
    vQ_app = vQ.append

    vQ_app(pp)
    while vQ:
        pp = vQ.popleft()
        if len(pp)>=N: break
        ma = max(ord(s) for s in pp)
        for i in range(ord('a'), ma+2):
            vQ_app(pp + chr(i))

    # res = 0
    # res = -(-N//M)
    vQ.appendleft("a" * N)

    res = vQ
    print(*sorted(res), sep="\n")

main()

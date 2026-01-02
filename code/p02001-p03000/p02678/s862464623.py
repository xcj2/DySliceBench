import sys
input = sys.stdin.readline

from collections import deque

def linput(_t=int):
    return list(map(_t, input().split()))

def gcd(n,m):
    while m: n,m = m, n%m
    return n

def lcm(n,m): return n*m//gcd(n,m)

def main():

    N,M = linput()
    # res = 0
    # print(N)
    mG = [[] for _ in [0,]*(N+1)]

    for _ in [0,]*M:
        a,b = linput()
        mG[a].append(b)
        mG[b].append(a)

    vR = [0,] * (N+1)
    vR[1] = 1

    vQ = deque([])
    vQ.append((mG[1],1))

    while vQ:
        vG, pp = vQ.popleft()
        # print(vG,pp,"vQ_pop")

        for g in vG:
            if vR[g] == 0:
                vR[g] = pp
                vQ.append((mG[g],g))

    print("Yes")
    print(*(r for r in vR[2:]), sep="\n")
    # print(res)
    # print(("No","Yes")[res%2])


main()

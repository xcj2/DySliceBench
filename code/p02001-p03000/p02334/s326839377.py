import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def combMod(n, r, p):
    numer = 1
    denom = 1
    for i in range(1, r+1):
        numer = numer * (n-r+i) % p
        denom = denom * i % p
    return numer * pow(denom, p-2, p) % p

def resolve():
    n, k = LI()

    ans = combMod(n + k - 1, n, MOD)

    print(ans)

if __name__ == '__main__':
    resolve()


import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, V = LI()
    a = LI()
    b = LI()
    c = LI()
    d = LI()

    ab = [i+j for i, j in itertools.product(a, b)]
    cd = [i+j for i, j in itertools.product(c, d)]
    ab.sort()
    cd.sort()

    ans = 0
    for i in ab:
        idx_l = bisect.bisect_left(cd, V - i)
        idx_r = bisect.bisect_right(cd, V - i)
        ans += idx_r - idx_l

    print(ans)

if __name__ == '__main__':
    resolve()


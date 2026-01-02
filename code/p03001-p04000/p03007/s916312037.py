import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def YesNo(x): return 'Yes' if x else 'No'
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
from bisect import bisect

def main():
    N = II()
    A = LI()
    A.sort()
    zero = 1 + bisect(A[1:-1], 0)
    ans = sum(A[zero:]) - sum(A[:zero])
    print(ans)
    x = A[0]
    for i in A[zero:-1]:
        print(x, i)
        x -= i
    y = A[-1]
    print(y, x)
    y -= x
    for i in A[1:zero]:
        print(y, i)
        y -= i
    return

main()
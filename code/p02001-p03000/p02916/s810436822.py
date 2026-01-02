import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def LILI(n): return [LI() for _ in range(n)]
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main(): 
    N = II()
    A = LI()
    B = LI()
    C = LI()


    prev = A[0]
    manzoku = B[prev-1]
    for i in range(1,N):
        ryouri = A[i]
        manzoku += B[ryouri-1]
        if prev+1 == A[i]:
            manzoku += C[prev-1]
        prev = A[i]

    print(manzoku)


main()
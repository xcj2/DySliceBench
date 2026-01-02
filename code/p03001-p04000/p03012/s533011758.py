import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main(): 
    N = II()
    W_li = LI()

    D_S_min = INF
    for i in range(N+1):
        S1 = sum(W_li[:i])
        S2 = sum(W_li[i:])
        D_S_min = min(D_S_min, abs(S1-S2))

    print(D_S_min)

main()
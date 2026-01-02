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
    B = LI()

    A = [B[0], ]
    for i in range(N-2):
        A.append( min(B[i], B[i+1]))
    A.append(B[N-2])
    print(sum(A))

main()
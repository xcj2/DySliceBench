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
    P= LI()

    P_sort = sorted(P)

    diff = 0
    for i,j in zip(P, P_sort):
        if i != j:
            diff += 1
    if diff ==0 or diff ==2:
        print('YES')
    else:
        print('NO')

main()
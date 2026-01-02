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

debug = True
#debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def solve():
    N = II()

    # 5桁以上
    if N == 10**5:
        print(90909)
        return
    # 5桁
    if N > 9999:
        print(N-10000+1+909)
        return

    # 4桁
    if N > 999:
        print(900+9)
        return

    # 3桁
    if N > 99:
        print(N-100+1 + 9)
        return

    # 2桁
    if N > 9:
        print(9)
        return

    # 1桁
    print(N)


solve()
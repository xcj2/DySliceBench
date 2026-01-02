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
    h_list = LI()

    mn = 10**10
    for h in reversed(h_list):
        if h >= mn + 2:
            print('No')
            return
        if h < mn:
            mn = h

    print('Yes')
solve()
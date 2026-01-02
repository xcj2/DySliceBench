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
    k, x = LI()

    mx = x + k - 1
    mn = x - k + 1
    print(' '.join([str(c) for c in list(range(mn, mx+1))]))

solve()
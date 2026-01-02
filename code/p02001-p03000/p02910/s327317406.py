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
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def solve():
    s = SI()

    odd = s[0::2]
    even = s[1::2]
    dprint(even, odd)
    if set(even) - set(['L', 'U', 'D']) == set() and set(odd) - set(['R', 'U', 'D']) == set():
        print('Yes')
    else:
        print('No')

solve()
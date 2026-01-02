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
    a_list = LI()
    b_list = LI()
    c_list = LI()

    base = 0
    add = 0
    past = -10
    for i in range(N):
        a = a_list[i]
        base += b_list[a-1]
        if a == past + 1:
            add += c_list[past-1]
        past = a
    print(add+base)
solve()
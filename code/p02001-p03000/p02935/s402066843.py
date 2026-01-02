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
    N = II()
    v_list = LI()

    v_list = sorted(v_list)

    while True:
        if len(v_list) <= 2:
            break
        newv = (v_list[0] + v_list[1]) / 2
        v_list = [newv] + v_list[2:]
        v_list = sorted(v_list)

    print((v_list[0]+v_list[1])/2)

solve()
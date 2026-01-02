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
    b_list = LI()

    a_list = [0 for i in range(N)]
    for i in range(N):
        # i桁目はi-1とiのminで決めればいい
        if i == 0:
            a_list[i] = b_list[i]
        elif i == N-1:
            a_list[i] = b_list[i-1]
        else:
            a_list[i] = min(b_list[i], b_list[i-1])

    print(sum(a_list))

solve()
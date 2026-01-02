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
    N, K = LI()
    S = SI()


    point = 0
    for i in range(N):
        if i != 0:
            if S[i] == S[i-1]:
                point += 1

    rest_len = N-point
    # rest_len_aft_k = rest_len - 2*K
    # dprint(rest_len, rest_len_aft_k)
    # if rest_len_aft_k <= 1:
    #     print(N)
    # else:
    print(min(point + 2*K, N-1))

solve()
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
    N, K, Q = LI()
    a_list = []
    for i in range(Q):
        a_list.append(II())

    score_list = [K-Q for i in range(N)]

    for i in range(Q):
        a = a_list[i]
        aidx = a - 1
        score_list[aidx] += 1

    for score in score_list:
        if score <= 0:
            print('No')
        else:
            print('Yes')
solve()
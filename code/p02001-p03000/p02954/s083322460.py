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

#debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def solve():
    S = SI()

    head = 0
    g_list = []
    while True:
        next = S.find('LR') + 1
        if next == 0:
            break
        g_list.append(S[:next])
        head = next
        S = S[head:]
        dprint(head, next, g_list)
    g_list.append(S)

    dprint(g_list)

    ans = []
    for g in g_list:
        lidx = g.find('L')
        rcnt = 0
        lcnt = 0
        for i in range(lidx):
            if (lidx-i+1)%2 == 0:
                rcnt += 1
            else:
                lcnt += 1
        for i in range(lidx, len(g)):
            if (lidx - i)%2 == 0:
                lcnt += 1
            else:
                rcnt += 1

        for i in range(len(g)):
            if i == lidx - 1:
                ans.append(rcnt)
            elif i == lidx:
                ans.append(lcnt)
            else:
                ans.append(0)

    print(' '.join([str(a) for a in ans]))
solve()
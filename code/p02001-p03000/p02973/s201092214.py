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

def main():
    N = II()
    a_list = []

    for i in range(N):
        a = II()
        a_list.append(a)


    from bisect import bisect_left
    from collections import deque
    g = deque()

    for i in range(N):
        a = a_list[i]
        if len(g) == 0:
            g.appendleft(a)
        else:
            pos = bisect_left(g, a)
            dprint(g, a, pos)
            if pos >= 1:
                g[pos-1] = a
            else:
                #g.insert(0, a)
                g.appendleft(a)
    dprint(g)
    print(len(g))
main()
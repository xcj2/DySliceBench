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
    a_list = []
    for i in range(N):
        a = II()
        a_list.append(a)

    from collections import Counter
    c = Counter(a_list)
    mx = max(a_list)

    k = c.keys()
    second = None
    if len(k) > 1:
        second = sorted(k, reverse=True)[1]

    for i in range(N):
        a = a_list[i]
        if a != mx:
            # これがmax出ない場合
            print(mx)
        else:
            if c[a] == 1:
                # maxが唯一で、これの場合
                print(second)
            else:
                # maxがこれでも複数ある場合
                print(mx)


solve()
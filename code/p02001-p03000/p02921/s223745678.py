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
    s = SI()
    t = SI()

    cnt = 0
    if s[0] == t[0]:
        cnt += 1
    if s[1] == t[1]:
        cnt += 1
    if s[2] == t[2]:
        cnt += 1
    print(cnt)

solve()
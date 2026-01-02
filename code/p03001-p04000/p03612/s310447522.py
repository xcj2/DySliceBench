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

def main(): 
    N = II()
    p_li = LI()

    ans = 0
    skip_next = False
    for i, p in enumerate(p_li):
        if skip_next:
            skip_next = False
            continue
        if p == (i+1):
            ans += 1
            skip_next = True
    print(ans)

main()
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
    v_li = LI()

    v_li.sort()

    ans = 0
    for i, v in enumerate(v_li):
        if i == 0:
            ans += (v / (2**(N-1)))
        else:
            ans += (v / (2**(N-i)))

    print(ans)


main()
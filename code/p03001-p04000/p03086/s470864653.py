import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

def main():
    S = SI()
    ans = 0
    tmp = 0
    for s in S:
        if s in 'ACGT':
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
    ans = max(ans, tmp)

    return ans

print(main())
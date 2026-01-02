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
    N = II()
    S = SI()
    global ans
    ans = 1
    from collections import Counter
    cnt = Counter(S)
    for n in cnt.values():
        ans = (ans * (n + 1)) % MOD

    ans -= 1
    return ans

print(main())
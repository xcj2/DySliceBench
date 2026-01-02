import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def YesNo(x): return 'Yes' if x else 'No'
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

def main():
    N, L = LI()
    li = list(range(L, N + L))
    if 0 in li:
        ans = sum(li)
    elif li[-1] < 0:
        ans = sum(li[:-1])
    else:
        ans = sum(li[1:])
    return ans

print(main())
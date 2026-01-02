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
from collections import Counter

def main():
    N = II()
    SP = []
    for i in range(1, N + 1):
        s, p = LS()
        p = int(p)
        SP.append([s + '{:06}'.format(100 - p), i])
    SP.sort()
    for _, id in SP:
        print(id)
    return

main()
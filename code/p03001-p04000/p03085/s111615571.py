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
    b = SI()
    if b == 'A':
        ans = 'T'
    elif b == 'T':
        ans = 'A'
    elif b == 'G':
        ans = 'C'
    else:
        ans = 'G'

    return ans

print(main())
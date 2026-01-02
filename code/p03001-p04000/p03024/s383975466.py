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
    rem = 15 - len(S)
    cnt = 8
    for s in S:
        if s == 'o':
            cnt -= 1
    ans = 'YES' if rem >= cnt else 'NO'
    return ans

print(main())
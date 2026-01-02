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
    a = int(S[:2])
    b = int(S[2:])
    if 1 <= a <= 12 and 1 <= b <= 12:
        ans = 'AMBIGUOUS'
    elif 1 <= a <= 12:
        ans = 'MMYY'
    elif 1 <= b <= 12:
        ans = 'YYMM'
    else:
        ans = 'NA'
    return ans

print(main())
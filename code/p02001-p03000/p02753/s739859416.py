import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
INF = float('inf')
LINF = 2**63-1
NIL = -LINF
MOD = 10**9+7
MGN = 4
def II(): return int(input())
def IF(): return float(input())
def IS(): return str(input())
def ILCI(n: int): return [II() for _ in range(n)]
def ILCF(n: int): return [IF() for _ in range(n)]
def ILI(): return list(map(int, input().split()))
def ILLI(n: int): return [[int(j) for j in input().split()] for i in range(n)]
def ILF(): return list(map(float, input().split()))
def ILLF(n: int): return [[float(j) for j in input().split()] for i in range(n)]
def LTOS(lst: list, sep: str = ' '): return sep.join(map(str, lst))
def DEC(lst: list): return list(map(lambda x: x-1, lst))
def INC(lst: list): return list(map(lambda x: x+1, lst))


def main():
    S = IS()

    ans = "Yes"
    if S[0] == S[1] and S[1] == S[2]:
        ans = "No"
    
    print(ans)


if __name__ == '__main__':
    main()

import sys

def input(): return sys.stdin.readline()[:-1]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def MATINT(h): return [list(map(int, input().split())) for _ in range(h)]
def MATSTR(h): return [input() for _ in range(h)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
inf = float('inf')
mod = 10 ** 9 + 7

def main():
    S = input()
    for i in range(len(S)):
        if S[i] == "L" and (i + 1) % 2 == 1:
            No()
            exit()
        if S[i] == "R" and (i + 1) % 2 == 0:
            No()
            exit()
    Yes()

if __name__ == '__main__':
    main()

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
    N = INT()
    C = [LIST() for i in range(N)]
    C.sort(key=lambda x:x[1])
    sum = 0
    for i in range(N):
        sum += C[i][0]
        if sum > C[i][1]:
            No()
            exit()
    Yes()

if __name__ == '__main__':
    main()

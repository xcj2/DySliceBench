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
    M, D = MAP()
    count = 0
    for mm in range(1, M+1):
        for dd in range(1, D+1):
            d1 = dd % 10
            d10 = dd // 10
            if d1 > 1 and d10 > 1:
                if d1 * d10 == mm:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()

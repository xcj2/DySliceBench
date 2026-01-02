import sys
import math

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
    minv = 10
    sumv = 0
    for i in range(5):
        tmp = INT()
        if tmp % 10 > 0:
            minv = min(minv, tmp%10)
        sumv += math.ceil(tmp/10) * 10
    print(sumv - 10 + minv)



if __name__ == '__main__':
    main()

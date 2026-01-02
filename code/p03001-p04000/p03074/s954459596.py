import sys
from collections import deque

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
    N, K = MAP()
    S = input() + 'e'

    num = []
    count = []
    tmp0 = 0
    tmp1 = 0
    for i in range(N):
        if S[i] == '0':
            tmp0 += 1
            if S[i + 1] == '1' or S[i + 1] == 'e':
                num += [0]
                count += [tmp0]
                tmp0 = 0
        else:
            tmp1 += 1
            if S[i + 1] == '0' or S[i + 1] == 'e':
                num += [1]
                count += [tmp1]
                tmp1 = 0
    if num[0] == 0:
        num = [1] + num
        count = [0] + count
    if num[-1] == 0:
        num += [1]
        count += [0]
    k = 0
    sumv = sum(count[:2*K+1])
    maxv = sumv
    l = 0
    r = 2*K+1
    for j in range(1, len(num)//2 - K + 1):
        sumv += sum(count[r:r+2])
        sumv -= sum(count[l:l+2])
        r += 2
        l += 2
        maxv = max(maxv, sumv)
    print(maxv)

if __name__ == '__main__':
    main()

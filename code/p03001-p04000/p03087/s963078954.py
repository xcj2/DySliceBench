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
    N, Q = MAP()
    S = input()
    t = [0] * (N + 1)
    for i in range(N - 1):
        if S[i:i+2] == 'AC':
            t[i + 1] = t[i] + 1
        else:
            t[i + 1] = t[i]
    ans = []
    for i in range(Q):
        l, r = MAP()
        ans.append(t[r - 1] - t[l - 1])
    for i in range(Q):
        print(ans[i])

if __name__ == '__main__':
    main()

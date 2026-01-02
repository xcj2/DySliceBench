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
    X, Y, Z, K = MAP()
    A = sorted(LIST(), reverse=True)
    B = sorted(LIST(), reverse=True)
    C = sorted(LIST(), reverse=True)
    tmp = []
    for aa in range(X):
        for bb in range(Y):
            for cc in range(Z):
                if (aa + 1) * (bb + 1) * (cc + 1) <= K:
                    tmp.append(A[aa] + B[bb] + C[cc])
                else:
                    break
    tmp.sort(reverse=True)
    for kk in range(K):
        print(tmp[kk])

if __name__ == '__main__':
    main()

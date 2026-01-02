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
    N, K = MAP()
    A = LIST()
    count = 0
    if K % 2 == 0:
        tmp1 = int(K / 2)
        tmp2 = K - 1
    else:
        tmp1 = K
        tmp2 = int((K - 1) / 2)
    for i in range(N):
        count_all = 0
        count_ = 0
        for j in range(N):
            if A[i] > A[j]:
                count_all += 1
                if i < j:
                    count_ += 1
        count += count_ * K % mod
        count += (((tmp1 * tmp2) % mod) * count_all) % mod
        count = count % mod
        # import pdb; pdb.set_trace()
    print(int(count) % mod)

if __name__ == '__main__':
    main()

import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, K, L, R = LI()
    a = LI()

    N_half_A = N // 2
    A_sum = [[] for _ in range(N_half_A + 1)]
    for i in range(2 ** N_half_A):
        sum = 0
        num = 0
        for j in range(N_half_A):
            if (i >> j) & 1:
                sum += a[j]
                num += 1
        A_sum[num].append(sum)

    N_half_B = N - N_half_A
    B_sum = [[] for _ in range(N_half_B + 1)]
    for i in range(2 ** N_half_B):
        sum = 0
        num = 0
        for j in range(N_half_B):
            if (i >> j) & 1:
                sum += a[N_half_A + j]
                num += 1
        B_sum[num].append(sum)
    for i in B_sum:
        i.sort()

    ans = 0
    for i in range(N_half_A + 1):
        if 0 <= K - i <= N_half_B:
            for j in A_sum[i]:
                idx_l = bisect.bisect_left(B_sum[K-i], L - j)
                idx_r = bisect.bisect_right(B_sum[K-i], R - j)
                ans += idx_r - idx_l

    print(ans)


if __name__ == '__main__':
    resolve()


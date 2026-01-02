import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
F = sorted(list(map(int, input().split())))


def binary_search(min_n, max_n):

    while max_n - min_n != 1:
        tn = (min_n + max_n) // 2
        if judge(tn):
            max_n = tn
        else:
            min_n = tn

    return max_n


def judge(tn):

    k = 0
    for i in range(N):
        if A[i] * F[i] > tn:
            k += A[i] - (tn // F[i])
        if k > K:
            return False

    return True


def solve():

    ans = binary_search(-1, 10**12)
    print(ans)


if __name__ == '__main__':
    solve()

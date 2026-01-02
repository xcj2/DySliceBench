

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M, K = read_ints()
    A = read_ints()
    B = read_ints()
    A_read = 0
    B_read = M
    B_sum = sum(B)
    A_sum = 0
    max_read = 0
    for A_read in range(N+1):
        if A_read > 0:
            A_sum += A[A_read-1]
        while B_read > 0 and A_sum+B_sum > K:
            B_read -= 1
            B_sum -= B[B_read]
        if A_sum+B_sum <= K:
            max_read = max(max_read, A_read+B_read)
    return max_read


if __name__ == '__main__':
    print(solve())

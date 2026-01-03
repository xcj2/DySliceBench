

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, x = read_ints()
    A = read_ints()
    answer = 0
    for i in range(1, N):
        if A[i-1]+A[i] > x:
            eat = A[i]+A[i-1]-x
            if eat <= A[i]:
                A[i] -= eat
                answer += eat
            else:
                eat -= A[i]
                answer += A[i]
                A[i] = 0
                A[i-1] -= eat
                answer += eat
    return answer


if __name__ == '__main__':
    print(solve())

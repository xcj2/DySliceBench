from collections import deque


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    A = [read_int() for _ in range(N)]
    A.sort()
    i, j = 0, N-2
    left = right = N-1 # points to left and right side of array
    answer = 0
    while i <= j:
        d, i, j, left, right = max([(abs(A[left]-A[i]), i+1, j, i, right),
                                    (abs(A[left]-A[j]), i, j-1, j, right),
                                    (abs(A[right]-A[i]), i+1, j, left, i),
                                    (abs(A[right]-A[j]), i, j-1, left, j)])
        answer += d
    return answer


if __name__ == '__main__':
    print(solve())

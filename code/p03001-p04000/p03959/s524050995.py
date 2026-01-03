from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve2() -> Any:
    N = read_int()
    T = read_ints()
    A = read_ints()
    upper = [0]*N
    lower = [0]*N
    upper[0] = lower[0] = T[0]
    for i in range(1, N):
        if T[i] > T[i-1]:
            upper[i] = lower[i] = T[i]
        else:
            upper[i] = T[i]
            lower[i] = 1
    if A[N-1] > upper[N-1] or A[N-1] < lower[N-1]:
        return 0
    upper[N-1] = lower[N-1] = A[N-1]
    for i in range(N-2, -1, -1):
        if A[i] > A[i+1]:
            if A[i] > upper[i] or A[i] < lower[i]:
                return 0
            upper[i] = lower[i] = A[i]
        else:
            # 1..A[i]
            if lower[i] > A[i]:
                return 0
            upper[i] = min(upper[i], A[i])
            lower[i] = min(lower[i], A[i])
    answer = 1
    modulo = 10**9+7
    for i in range(N):
        answer = (answer*(upper[i]-lower[i]+1))%modulo
    return answer



if __name__ == '__main__':
    print(solve2())


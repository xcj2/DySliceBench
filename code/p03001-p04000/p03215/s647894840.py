from typing import List, Dict

INF = 10**9+1


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))

def remove_if_gt(a, b):
    if a >= b:
        return a-b
    return a

def solve() -> int:
    N, K = read_ints()
    A = read_ints()
    S = []
    for i in range(N):
        prefix = 0
        for j in range(i, N):
            prefix += A[j]
            S.append(prefix)
    S.sort(reverse=True)
    highest_bit = 40
    answer = 0
    while highest_bit >= 0:
        while 1<<highest_bit > S[0]:
            highest_bit -= 1
            if highest_bit < 0:
                return answer
        highest_bit_val = 1<<highest_bit
        count = 0
        for i in range(len(S)):
            if S[i] >= highest_bit_val:
                count += 1
            else:
                break
        if count < K:
            S = [remove_if_gt(s, highest_bit_val) for s in S]
        else:
            answer += highest_bit_val
            S = [remove_if_gt(s, highest_bit_val) for s in S if s >= highest_bit_val]
        S.sort(reverse=True)
    return answer


if __name__ == '__main__':
    print(solve())

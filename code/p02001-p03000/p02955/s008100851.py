#!/usr/bin/env python3
import sys
INF = float("inf")


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


def solve(N: int, K: int, A: "List[int]"):
    tot = sum(A)
    divs = make_divisors(sum(A))

    m = 1
    for cand in divs[1:]:
        modA = sorted([a % cand for a in A])
        counter = 0
        left = 0
        while left < N and modA[left] == 0:
            left += 1
        right = N-1
        while left < right:
            smaller = min(modA[left], cand - modA[right])
            modA[left] -= smaller
            modA[right] += smaller
            counter += smaller
            if modA[left] == 0:
                left += 1
            if modA[right] == cand:
                right -= 1
        if counter <= K:
            m = cand

    print(m)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)


if __name__ == '__main__':
    main()

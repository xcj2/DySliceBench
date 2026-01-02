import math
from typing import List, Counter, Tuple
from collections import Counter
from itertools import permutations, zip_longest, groupby


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))

modulo = 10**9+7


def merge(A, start, end, divisors):
    if start == end:
        return Counter(divisors[A[start]])
    mid = start+(end-start)//2
    left = merge(A, start, mid, divisors)
    right = merge(A, mid+1, end, divisors)
    for r in right:
        left[r] = max(left[r], right[r])
    return left

def solve() -> int:
    N = read_int()
    A = read_ints()
    M = 10**6+1
    divisors: List[List[int]] = [[] for _ in range(M)]
    for i in range(2, M):
        if len(divisors[i]) == 0:
            for j in range(i, M, i):
                temp = j
                while temp%i == 0:
                    divisors[j].append(i)
                    temp //= i
    lcd_counter = merge(A, 0, N-1, divisors)
    lcd = 1
    for k in lcd_counter:
        lcd = (lcd*pow(k, lcd_counter[k], modulo))%modulo
    answer = 0
    for a in A:
        answer = (answer+(lcd*pow(a, modulo-2, modulo))%modulo)%modulo
    return answer


if __name__ == '__main__':
    print(solve())

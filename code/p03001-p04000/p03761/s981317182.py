import math
from collections import Counter


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    counts = {k: math.inf for k in alphabets}
    counters = []
    answer = []
    for _ in range(N):
        counters.append(Counter(input().strip()))
    for k in alphabets:
        is_in_all = True
        count = math.inf
        for counter in counters:
            if counter[k] == 0:
                is_in_all = False
                break
            count = min(count, counter[k])
        if is_in_all:
            answer += [k]*count
    return ''.join(answer)


if __name__ == '__main__':
    print(solve())

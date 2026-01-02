import math
from collections import Counter


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    A = []
    pair_count = Counter()
    for _ in range(N):
        line = input().strip()
        if '.' in line:
            a, b = line.split('.')
            d = 10**len(b)
            c = int(a)*d+int(b)
        else:
            c = int(line)
            d = 1
        gcd = math.gcd(c, d)
        c //= gcd
        d //= gcd
        pow2, pow5 = 0, 0
        while c and c%2 == 0:
            pow2 += 1
            c //= 2
        while c and c%5 == 0:
            pow5 += 1
            c //= 5
        while d and d%2 == 0:
            pow2 -= 1
            d //= 2
        while d and d%5 == 0:
            pow5 -= 1
            d //= 5
        pair_count[(pow2, pow5)] += 1
    answer = 0
    for pair0 in pair_count:
        for pair1 in pair_count:
            if pair0 < pair1 and pair0[0]+pair1[0] >= 0 and pair0[1]+pair1[1] >= 0:
                answer += pair_count[pair0]*pair_count[pair1]
            elif pair0 == pair1 and pair0[0] >= 0 and pair0[1] >= 0:
                answer += pair_count[pair0]*(pair_count[pair0]-1)//2
    return answer


if __name__ == '__main__':
    print(solve())

import math
from itertools import product
from collections import Counter


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def sums(a, N):
    ans = ((N//a)*((N//a)+1)//2)*a
    return ans


colors = ['R', 'G', 'B']

def complement(A, B):
    for color in colors:
        if A != color and B != color:
            return color
    

def solve():
    N = read_int()
    S = input().strip()
    right = Counter(S)
    left = Counter()
    total = 0
    for i in range(N):
        take = S[i]
        right[take] -= 1
        #
        for j in range(i):
            if S[j] != S[i]:
                color = complement(S[j], S[i])
                k = 2*i-j
                total += right[color]
                if k < N and S[k] == color:
                    total -= 1
        #
        left[take] += 1
    return total


if __name__ == '__main__':
    print(solve())

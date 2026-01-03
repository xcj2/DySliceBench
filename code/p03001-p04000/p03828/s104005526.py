from collections import Counter


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    1 2 3 4 5 6
    """
    N = read_int()
    divisors = [[] for _ in range(N+1)]
    modulo = 10**9+7
    for i in range(2, N+1):
        if len(divisors[i]) == 0: # if prime
            for j in range(i, N+1, i):
                divisors[j].append(i)
    counter = Counter()
    for i in range(1, N+1):
        j = 0
        temp = i
        while temp != 1 and j < len(divisors[i]):
            if temp%divisors[i][j] == 0:
                counter[divisors[i][j]] += 1
                temp //= divisors[i][j]
            else:
                j += 1
    answer = 1
    for v in counter.values():
        answer = (answer*(v+1))%modulo
    return answer


if __name__ == '__main__':
    print(solve())

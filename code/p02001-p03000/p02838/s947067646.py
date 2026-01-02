

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    size = 60
    digits = [[0, 0] for _ in range(size)]
    for a in read_ints():
        for i in range(size-1, -1, -1):
            digits[i][a&1] += 1
            a >>= 1
    p = 1
    answer = 0
    modulo = 10**9+7
    for i in range(size-1, -1, -1):
        answer = (answer+p*digits[i][0]*digits[i][1])%modulo
        p *= 2
    return answer


if __name__ == '__main__':
    print(solve())

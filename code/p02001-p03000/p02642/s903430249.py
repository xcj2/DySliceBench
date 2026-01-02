

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    A = read_ints()
    max_A = max(A)
    is_divisible = [False]*(max_A+1)
    A.sort()
    answer = 0
    last_a = None
    for a in A:
        if a == last_a:
            is_divisible[a] = True
        for step in range(2*a, max_A+1, a):
            is_divisible[step] = True
        last_a = a
    return sum([not is_divisible[a] for a in A])


if __name__ == '__main__':
    print(solve())

import heapq


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    Circle

    left with [A, B] and A < B

    _ _ A B _

    _ _ B A _

    """
    N = read_int()
    A = read_ints()
    A.sort()
    A_max = A.pop()
    ranges = [(-A_max, -A_max)]
    score = 0
    while A:
        a = A.pop()
        left, right = heapq.heappop(ranges)
        score += -left
        heapq.heappush(ranges, (-a, left))
        heapq.heappush(ranges, (-a, right))
    return score


if __name__ == '__main__':
    print(solve())

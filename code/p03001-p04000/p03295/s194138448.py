import sys
import itertools
input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def main():
    N, M = read_values()
    Q = [read_list() for _ in range(M)]
    Q.sort()

    res = 0
    end = 10 ** 6
    for q in Q:
        if q[0] >= end:
            res += 1
            end = q[1]
        else:
            end = min(end, q[1])
    
    res += 1
    print(res)


if __name__ == "__main__":
    main()

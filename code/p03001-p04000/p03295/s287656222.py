import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, M, inputs):
    requests = list(map(lambda x: string_to_int(x), inputs))
    requests = sorted(requests, key=lambda x: x[1])

    deleted = []
    last = 0

    for request in requests:
        if request[0] > last:
            deleted.append(request[1] - 1)
            last = deleted[-1]

    return len(deleted)


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(M))
    print(ret)

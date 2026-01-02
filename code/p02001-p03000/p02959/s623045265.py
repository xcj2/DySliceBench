import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [N] = string_to_int(inputs[0])
    A = string_to_int(inputs[1])
    B = string_to_int(inputs[2])

    count = 0
    for i in range(0, N):
        j = i+1
        if A[i] <= B[i]:
            B[i] -= A[i]
            count += A[i]
            A[i] = 0
        else:
            A[i] -= B[i]
            count += B[i]
            B[i] = 0

        if A[j] <= B[i]:
            B[i] -= A[j]
            count += A[j]
            A[j] = 0
        else:
            A[j] -= B[i]
            count += B[i]
            B[i] = 0

    return count


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(3))
    print(ret)

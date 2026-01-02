import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = inputs[0]
    n = len(S)
    is_even = True if n % 2 == 0 else False

    if is_even:
        front = S[:n//2]
        back = S[n//2:]
    else:
        front = S[:n//2+1]
        back = S[n//2:]
    count = 0

    for i, c in enumerate(reversed(back)):
        if front[i] != c:
            count += 1
    return count


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)

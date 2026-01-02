import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    restaurants = []
    for i, s in enumerate(inputs):
        s = s.split()
        restaurants.append((i+1, s[0], int(s[1])))
    restaurants.sort(key=lambda x: x[2], reverse=True)
    restaurants.sort(key=lambda x: x[1])

    ret = list(map(lambda r: r[0], restaurants))

    return ret


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N] = string_to_int(input())
    ret = solve(inputs(N))
    # print(ret)

    for r in ret:
        print(r)

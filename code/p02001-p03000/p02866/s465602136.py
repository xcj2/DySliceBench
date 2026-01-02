import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    SSSS = 998244353
    D = string_to_int(inputs[0])
    # {distance: numbers}
    nodes = {}
    for i, d in enumerate(D):
        i += 1
        if d not in nodes:
            nodes[d] = [i]
        else:
            nodes[d].append(i)

    if 0 not in nodes:
        return 0

    prev = -1
    prev_num = -1
    count = 0
    for d in sorted(nodes.keys()):
        if d == 0:
            if not (len(nodes[d]) == 1 and nodes[d][0] == 1):
                return 0
            count = 1
            prev_num = 1
            prev = d
            continue
        if abs(d - prev) != 1:
            return 0

        count *= prev_num ** len(nodes[d])
        prev_num = len(nodes[d])
        prev = d
    return count % SSSS


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)

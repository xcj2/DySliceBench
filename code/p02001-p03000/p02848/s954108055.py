import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    N = int(inputs[0])
    S = inputs[1]
    new_s = []
    ord_a = ord('A')
    ord_z = ord('Z')
    for c in S:
        ordc = ord(c)
        ordc += N
        if ordc > ord_z:
            d = ordc - ord_z - 1
            ordc = ord_a + d
        new_s.append(chr(ordc))
    return "".join(new_s)


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)

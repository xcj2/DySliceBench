import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    all_remark = []
    for i in inputs:
        all_remark.append(list(map(string_to_int, i)))
    n = len(all_remark)
    max_pattern = 2**n

    max_shojiki = 0
    for p in range(max_pattern):
        bits = list(bin(p)[2:])
        bits = ['0' for i in range(n-len(bits))] + bits
        shojiki = 0
        for b in bits:
            if b == '1':
                shojiki += 1

        for i, remarks in enumerate(all_remark):
            is_possible = True
            if bits[i] == '1':
                for r in remarks:
                    target = r[0]
                    w = r[1]
                    if bits[target - 1] != str(w):
                        is_possible = False
                        break
                if is_possible is False:
                    break
        if is_possible and max_shojiki < shojiki:
            max_shojiki = shojiki
    return max_shojiki


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    N = int(input())
    arg = []
    for i in range(N):
        A = int(input())
        arg.append(inputs(A))
    ret = solve(arg)
    print(ret)

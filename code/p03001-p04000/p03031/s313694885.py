import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def create_bin_string(data, num):
    c_bin = "{:b}".format(data)
    switches = c_bin
    for _ in range(0, num-len(c_bin)):
        switches = "0" + switches
    return switches


def solve(N, M, data, Ps):
    lamp_sw_comb = list(map(lambda x: string_to_int(x), data))
    lamp_sw_p = string_to_int(Ps)

    count = 0
    for c in range(0, 2**N):
        switches = create_bin_string(c, N)

        are_all_light = True
        for i, lamp_sw in enumerate(lamp_sw_comb):
            on_num = 0
            for j, sw in enumerate(lamp_sw):
                if j == 0:
                    continue
                if switches[sw-1] == "1":
                    on_num += 1
            if on_num % 2 != lamp_sw_p[i]:
                are_all_light = False
                break

        if are_all_light:
            count += 1
    return count


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    data = inputs(M)
    Ps = input()
    ret = solve(N, M, data, Ps)
    print(ret)

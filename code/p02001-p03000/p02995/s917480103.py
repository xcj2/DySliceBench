import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def euclid(a, b):
    if a > b:
        large = a
        small = b
    else:
        large = b
        small = a

    while small != 0:
        r = large % small
        large = small
        small = r

    return large


def solve(inputs):
    [A, B, C, D] = string_to_int(inputs[0])
    cd_gcd = euclid(C, D)
    cd_lcm = (C*D) // cd_gcd

    a_c = (A-1) // C
    a_d = (A-1) // D
    a_cd = (A-1) // cd_lcm

    b_c = B // C
    b_d = B // D
    b_cd = B // cd_lcm

    under_a = int((A-1) - a_c - a_d + a_cd)
    under_b = int(B - b_c - b_d + b_cd)

    return under_b - under_a


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)

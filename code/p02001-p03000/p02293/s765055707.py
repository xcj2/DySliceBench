# coding=utf-8


def vector_product(vect1, vect2):
    return [el1 * el2 for el1, el2 in zip(vect1, vect2)]


def inner_product(vect1, vect2):
    return sum(vector_product(vect1, vect2))


def cross_product(vect1, vect2):
    return vect1[0]*vect2[1] - vect1[1]*vect2[0]


def vector_minus(vect1, vect2):
    return [el1 - el2 for el1, el2 in zip(vect1, vect2)]


def line_slope(line_from, line_to):
    try:
        slope = (line_to[1] - line_from[1])/(line_to[0] - line_from[0])
    except ZeroDivisionError:
        slope = "未定義"
    return slope


"""
def is_parallel(l_from1, l_to1, l_from2, l_to2):
    slope1 = line_slope(l_from1, l_to1)
    slope2 = line_slope(l_from2, l_to2)
    if slope1 == slope2:
        return 1
    return 0
"""


def is_parallel(l_from1, l_to1, l_from2, l_to2):
    line1 = vector_minus(l_to1, l_from1)
    line2 = vector_minus(l_to2, l_from2)
    if cross_product(line1, line2) == 0:
        return 1
    return 0


def is_orthogonal(l_from1, l_to1, l_from2, l_to2):
    line1 = vector_minus(l_to1, l_from1)
    line2 = vector_minus(l_to2, l_from2)
    if inner_product(line1, line2) == 0:
        return 1
    return 0


if __name__ == '__main__':
    Q = int(input())

    for i in range(Q):
        all_list = list(map(int, input().split()))
        p0_list = all_list[:2]
        p1_list = all_list[2:4]
        p2_list = all_list[4:6]
        p3_list = all_list[6:]

        if is_parallel(p0_list, p1_list, p2_list, p3_list):
            print("2")
        elif is_orthogonal(p0_list, p1_list, p2_list, p3_list):
            print("1")
        else:
            print("0")


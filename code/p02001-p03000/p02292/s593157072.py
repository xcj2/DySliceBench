# coding=utf-8


def cross_product(vect1, vect2):
    return vect1[0]*vect2[1] - vect1[1]*vect2[0]


def vector_plus(vect1, vect2):
    return [el1 + el2 for el1, el2 in zip(vect1, vect2)]


def vector_minus(vect1, vect2):
    return [el1 - el2 for el1, el2 in zip(vect1, vect2)]


def vector_product(vect1, vect2):
    return [el1 * el2 for el1, el2 in zip(vect1, vect2)]


def vector_divide(vect1, vect2):
    return [el1 / el2 for el1, el2 in zip(vect1, vect2)]


def which_place(origin, line_to1, line_to2):
    line1 = vector_minus(line_to1, origin)
    line2 = vector_minus(line_to2, origin)
    judge = cross_product(line1, line2)

    if judge > 0:
        return "COUNTER_CLOCKWISE"
    if judge < 0:
        return "CLOCKWISE"
    if judge == 0:
        try:
            judge2 = line2[0]/line1[0]
        except ZeroDivisionError:
            judge2 = line2[1]/line1[1]
        
        if judge2 < 0:
            return "ONLINE_BACK"
        if judge2 > 1:
            return "ONLINE_FRONT"
        else:
            return "ON_SEGMENT"


if __name__ == '__main__':
    xy_list = list(map(int, input().split()))
    p0_list = xy_list[:2]
    p1_list = xy_list[2:]
    Q = int(input())

    for i in range(Q):
        p2_list = list(map(int, input().split()))
        place = which_place(p0_list, p1_list, p2_list)
        print(place)


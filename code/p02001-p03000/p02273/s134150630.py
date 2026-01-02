# coding=utf-8
import math


def divide_segment(left, right):
    """divide segment

    Args:
        left: left edge coordinate
        right: right edge coordinate

    Returns:
        divided points
    """
    delta_x_quarter = (right[0] - left[0]) / 3.0
    delta_y_quarter = (right[1] - left[1]) / 3.0

    delta_x_quarter_rotated = (delta_x_quarter - math.sqrt(3) * delta_y_quarter) / 2.0
    delta_y_quarter_rotated = (math.sqrt(3) * delta_x_quarter + delta_y_quarter) / 2.0

    s = [left[0] + delta_x_quarter, left[1] + delta_y_quarter]
    t = [left[0] + delta_x_quarter * 2.0, left[1] + delta_y_quarter * 2.0]
    u = [s[0] + delta_x_quarter_rotated, s[1] + delta_y_quarter_rotated]

    return s, t, u


def make_coch_curve(depth, left, right):
    """make coch curve with depth iteration_number between point left, right
    each vertices positions are printed

    Args:
        depth: depth
        left: left edge point
        right: right edge point

    Returns:
        None
    """
    print("{0:2.8f} {1:2.8f}".format(left[0], left[1]))
    if depth == 0:
        print("{0:2.8f} {1:2.8f}".format(right[0], right[1]))
    else:
        make_coch_curve_recursively(depth-1, left, right)


def make_coch_curve_recursively(depth, left, right):
    """recursion part of coch curve

    Args:
        depth: depth
        left: left edge coordinate
        right: right edge coordinate

    Returns:
        None
    """
    # get coordinate of divided points
    s, t, u = divide_segment(left, right)

    if depth == 0:
        print("{0:2.8f} {1:2.8f}".format(s[0], s[1]))
        print("{0:2.8f} {1:2.8f}".format(u[0], u[1]))
        print("{0:2.8f} {1:2.8f}".format(t[0], t[1]))
        print("{0:2.8f} {1:2.8f}".format(right[0], right[1]))
    else:
        make_coch_curve_recursively(depth - 1, left, s)
        make_coch_curve_recursively(depth - 1, s, u)
        make_coch_curve_recursively(depth - 1, u, t)
        make_coch_curve_recursively(depth - 1, t, right)


def main():
    depth = int(input().strip())
    make_coch_curve(depth, left=[0.0, 0.0], right=[100.0, 0.0])


if __name__ == '__main__':
    main()
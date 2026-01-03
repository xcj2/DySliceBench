import re
import functools

class IO_for_Contest(object):
    @staticmethod
    def my_input():
        #return raw_input()
        return input()

    @staticmethod
    def read_from_input():
        n, m = IO_for_Contest.read_n_int(2)
        x, y = [], []
        for i in range(m):
            xx, yy = IO_for_Contest.read_n_int(2)
            x.append(xx)
            y.append(yy)
        return n, x, y

    @staticmethod
    def read_line():
        return IO_for_Contest.my_input().strip()

    @staticmethod
    def read_int():
        return int(IO_for_Contest.my_input().strip())

    @staticmethod
    def read_n_int(n):
        return list(map(int, re.split('\W+', IO_for_Contest.my_input().strip())))[ : n]

def solve():
    n, x, y = IO_for_Contest.read_from_input()
    m = len(x)
    print(count_boxes_can_have_red_ball(n, m, x, y))

def count_boxes_can_have_red_ball(n, m, x, y):
    """
    >>> n, m, x, y = 3, 2, [1, 2], [2, 3]
    >>> count_boxes_can_have_red_ball(n, m, x, y)
    2
    """
    balls = [0]
    red_ball_can_exist = [None]
    for i in range(n):
        if i == 0:
            red_ball_can_exist.append(True)
        else:
            red_ball_can_exist.append(False)
        balls.append(1)
    for i in range(m):
        f, t = x[i], y[i]
        balls[f] -= 1
        balls[t] += 1
        if red_ball_can_exist[f]:
            if balls[f] <= 0:
                red_ball_can_exist[f] = False
            red_ball_can_exist[t] = True
        else:
            pass
        #print('{0:d}, {1:s}, {2:s}'.format(i, str(balls), str(red_ball_can_exist)))
    return red_ball_can_exist.count(True)

if __name__ == '__main__':
    #import doctest
    #doctest.testmod()
    solve()
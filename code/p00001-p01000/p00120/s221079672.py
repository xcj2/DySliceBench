# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0120

"""
import sys
from sys import stdin
input = stdin.readline


def calc_width(cakes):
    # ??±????????????????????????(?????????)????????????????????????????????????????¨??????????
    if len(cakes) == 1:
        return cakes[0]*2

    prev_r = cakes[0]
    width = prev_r

    for r in cakes[1:]:
        h_diff = abs(prev_r - r)
        if h_diff == 0:
            width += prev_r
            width += r
        else:
            w = ((prev_r + r)**2 - h_diff**2)**0.5
            width += w
        prev_r = r
    width += cakes[-1]

    return width


def main(args):
    for line in sys.stdin:
        data = [int(x) for x in line.strip().split()]
        box_size = data[0]
        temp = data[1:]
        temp.sort()

        min_width = float('inf')
        cake = []
        if len(temp) < 3:
            cakes = temp[:]
        elif len(temp) == 3:
            cakes = [temp[1], temp[2], temp[0]]
        else:
            cakes = [temp[1] ,temp[-1], temp[0]]
            temp = temp[2:-1]
            tail = True
            small = False
            while temp:
                if tail:
                    if small:
                        cakes.append(temp[0])
                        temp = temp[1:]
                        tail = False
                    else:
                        cakes.append(temp[-1])
                        temp = temp[:-1]
                        tail = False
                else:
                    if small:
                        cakes.insert(0, temp[0])
                        temp = temp[1:]
                        small = False
                        tail = True
                    else:
                        cakes.insert(0, temp[-1])
                        temp = temp[:-1]
                        small = True
                        tail = True

        result = calc_width(cakes)
        min_width = min(result, min_width)

        temp = data[1:]
        temp.sort()
        cake = []
        if len(temp) < 3:
            cakes = temp[:]
        elif len(temp) == 3:
            cakes = [temp[1], temp[0], temp[2]]
        else:
            cakes = [temp[-2] ,temp[0], temp[-1]]
            temp = temp[1:-2]
            tail = True
            small = True
            while temp:
                if tail:
                    if small:
                        cakes.append(temp[0])
                        temp = temp[1:]
                        tail = False
                    else:
                        cakes.append(temp[-1])
                        temp = temp[:-1]
                        tail = False
                else:
                    if small:
                        cakes.insert(0, temp[0])
                        temp = temp[1:]
                        small = False
                        tail = True
                    else:
                        cakes.insert(0, temp[-1])
                        temp = temp[:-1]
                        small = True
                        tail = True
        result = calc_width(cakes)
        min_width = min(result, min_width)



        if min_width <= box_size:
            print('OK')
        else:
            print('NA')


from itertools import permutations
def main2(args):
    data = [3, 3, 3, 10, 10]

    p = permutations(data, len(data))


    best_fit = float('inf')
    for cakes in p:
        result = calc_width(cakes)
        if result < best_fit:
            best_fit = result
            print(cakes)
            print(result)


if __name__ == '__main__':
    main(sys.argv[1:])
    
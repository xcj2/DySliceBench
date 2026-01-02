# -*- coding: utf-8 -*-
figures = {
    'A': [['1', '1'], ['1', '1']],
    'B': [['1'], ['1'], ['1'], ['1']],
    'C': [['1', '1', '1', '1']],
    'D': [['0', '1'], ['1', '1'], ['1', '0']],
    'E': [['1', '1', '0'], ['0', '1', '1']],
    'F': [['1', '0'], ['1', '1'], ['0', '1']],
    'G': [['0', '1', '1'], ['1', '1', '0']],
}


def f1(lines):
    for n, figure in figures.items():
        found = f2(lines, figure)
        if found:
            print(n)
            break


def f2(lines, figure):
    height = len(figure)
    width = len(figure[0])
    for h in range(8 - height + 1):
        for w in range(8 - width + 1):
            found = f3(lines, figure, height, width, h, w)
            if found:
                return True


def f3(lines, figure, height, width, h, w):
    _figure = [[lines[h+_h][w+_w] for _w in range(width)]
               for _h in range(height)]
    if figure == _figure:
        return True


try:
    while True:
        f1([list(input()) for _ in range(8)])
        input()
except EOFError:
    pass
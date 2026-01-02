# -*- coding: utf-8 -*-

def input_int_array():
    return map(int, input().split())


class Board:
    def __init__(self, w, h, parent):
        self.w = w
        self.h = h
        self.parent = parent


def answer(n, q):
    min_board = Board(n-2, n-2, None)
    black = (n - 2) * (n - 2)
    for i in range(q):
        a, pos = input_int_array()
        pos -= 1
        board = min_board
        use_min = True
        if a == 1:
            while pos > board.w:
                board = board.parent
                use_min = False
            black -= board.h
            if use_min:
                b = Board(pos - 1, board.h, board)
                min_board = b
        else:
            while pos > board.h:
                board = board.parent
                use_min = False
            black -= board.w
            if use_min:
                b = Board(board.w, pos - 1, board)
                min_board = b
    print(black)


n, q = input_int_array()
answer(n, q)

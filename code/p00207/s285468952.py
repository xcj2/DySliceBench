""" Created by Jieyi on 9/20/16. """


def block(board, w, h, direction, color):
    # horizontal.
    if direction == 0:
        for i in range(2):
            for j in range(4):
                board[h + i][w + j] = color
    # vertical.
    elif direction == 1:
        for i in range(2):
            for j in range(4):
                board[h + j][w + i] = color


def print_board(board):
    for i in range(len(board)):
        print(board[i])


direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_goable(board, w, h, color):
    for x, y in direct:
        if board[h + x][w + y] == color:
            return True
    return False


def go_maze(board, s_w, s_h, g_w, g_h):
    place = board[s_h][s_w]
    if place == 0:
        return 'NG'
    w, h = s_w, s_h
    stack = []

    while True:
        board[h][w] = place + 1
        is_no_way = True
        for x, y in direct:
            if board[h + x][w + y] == place:
                w, h = w + y, h + x
                stack.append((w, h))
                is_no_way = False
                break

        if is_no_way:
            if len(stack) == 0 and not is_goable(board, w, h, place):
                return 'NG'
            (w, h) = stack.pop()
        if w == g_w and h == g_h:
            return 'OK'


def main():
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        board = [[0 for _ in range(110)] for _ in range(110)]
        s_w, s_h = map(int, input().split())
        g_w, g_h = map(int, input().split())
        for _ in range(int(input())):
            color, direction, w, h = map(int, input().split())
            block(board, w, h, direction, color)

        # print_board(board)
        print(go_maze(board, s_w, s_h, g_w, g_h))


if __name__ == '__main__':
    main()
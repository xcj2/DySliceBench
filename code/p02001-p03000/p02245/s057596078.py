# -*- coding: utf-8 -*-
import sys
from itertools import chain


def get_completed_board(height, width):
    return [str((i + 1) % (width * height)) for i in range(width * height)]


def serialize_board(board):
    return ":".join(board)


def get_empty_pos(board, width, height):
    for i, cell in enumerate(board):
        if cell == "0":
            return i


def get_all_possible_next_boards(board, height, width, empty_pos=None):
    if empty_pos is None:
        empty_pos = get_empty_pos(board, height, width)
    next_boards = []
    x, y = empty_pos % width, empty_pos // height
    # 左との入れ替え
    if x > 0:
        next_board = []
        next_board.extend(board)
        dest_pos = empty_pos - 1
        next_board[empty_pos], next_board[dest_pos] = next_board[dest_pos], next_board[empty_pos]
        next_boards.append((next_board, dest_pos))
    # 右との入れ替え
    if x < width - 1:
        next_board = []
        next_board.extend(board)
        dest_pos = empty_pos + 1
        next_board[empty_pos], next_board[dest_pos] = next_board[dest_pos], next_board[empty_pos]
        next_boards.append((next_board, dest_pos))
    # 上との入れ替え
    if y > 0:
        next_board = []
        next_board.extend(board)
        dest_pos = empty_pos - height
        next_board[empty_pos], next_board[dest_pos] = next_board[dest_pos], next_board[empty_pos]
        next_boards.append((next_board, dest_pos))
    # 下との入れ替え
    if y < height - 1:
        next_board = []
        next_board.extend(board)
        dest_pos = empty_pos + height
        next_board[empty_pos], next_board[dest_pos] = next_board[dest_pos], next_board[empty_pos]
        next_boards.append((next_board, dest_pos))

    return next_boards


def resolve(board, height, width):
    # 既知の盤面を保存
    known_serialized_boards = set([serialize_board(board)])
    # 正解の盤面を保存
    completed_board = get_completed_board(width, height)
    known_serialized_completed_boards = set([serialize_board(completed_board)])
    if known_serialized_boards & known_serialized_completed_boards:
        return 0
    current_boards = [(board, None)]
    current_completed_boards = [(get_completed_board(width, height), None)]
    step_count = 1
    while step_count <= 45:
        # インプット側の盤面を一つ進める
        next_boards = []
        for board, empty_pos in current_boards:
            # 次のステップでの現れ得る局面を全て取得
            tmp_next_boards = get_all_possible_next_boards(board, height, width, empty_pos)
            filtered_next_board = []
            for board, empty_pos in tmp_next_boards:
                serialized_board = serialize_board(board)
                if serialized_board not in known_serialized_boards:
                    known_serialized_boards.add(serialized_board)
                    filtered_next_board.append((board, empty_pos))
            next_boards.extend(filtered_next_board)

        if known_serialized_boards & known_serialized_completed_boards:
            return step_count

        step_count = step_count + 1
        current_boards = next_boards

        # 正解盤面側を１つ進める
        next_completed_boards = []
        for board, empty_pos in current_completed_boards:
            # 次のステップでの現れ得る局面を全て取得
            tmp_next_boards = get_all_possible_next_boards(board, height, width, empty_pos)
            filtered_next_board = []
            for board, empty_pos in tmp_next_boards:
                serialized_board = serialize_board(board)
                if serialized_board not in known_serialized_completed_boards:
                    known_serialized_completed_boards.add(serialized_board)
                    filtered_next_board.append((board, empty_pos))
            next_completed_boards.extend(filtered_next_board)

        if known_serialized_boards & known_serialized_completed_boards:
            return step_count
        step_count = step_count + 1
        current_completed_boards = next_completed_boards

    return None


def main():
    inputStr = sys.stdin.read()
    lines = inputStr.split("\n")
    lines = filter(lambda line: line, lines)
    board = list(map(lambda line: line.split(" "), lines))
    height = len(board)
    width = len(board[0])
    board = list(chain.from_iterable(board))
    print(resolve(board, height, width))


if __name__ == '__main__':
    main()

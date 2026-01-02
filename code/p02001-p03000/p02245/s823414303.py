import copy
from typing import List, Tuple


def _generate_goal() -> List[List[int]]:
    goal = [[0] * 3 for _ in range(3)]
    for row in range(3):
        for col in range(3):
            if 9 == 3 * row + col + 1:
                goal[row][col] = 0
            else:
                goal[row][col] = 3 * row + col + 1
    return goal


def _find_zero_pos(board: List[List[int]]) -> Tuple[int, int]:
    for row in range(3):
        for col in range(3):
            if 0 == board[row][col]:
                return (row, col)
    # Never reaches here.
    return (-1, -1)


def _swappable_cand(zero_pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    row, col = zero_pos[0], zero_pos[1]
    cand_pos_list: List[Tuple[int, int]] = []
    if 0 != row:
        cand_pos_list.append((row - 1, col))
    if 2 != row:
        cand_pos_list.append((row + 1, col))
    if 0 != col:
        cand_pos_list.append((row, col - 1))
    if 2 != col:
        cand_pos_list.append((row, col + 1))

    return cand_pos_list


def solve_8puzzle(board: List[List[int]]) -> int:
    goal = _generate_goal()
    if board == goal:
        return 0
    generated_boards = {tuple(sum(board, [])): 0, tuple(sum(goal, [])): 1}
    steps = {tuple(sum(board, [])): 0, tuple(sum(goal, [])): 0}
    step = 0
    state = [(board, 0), (goal, 1)]
    while state:
        state_copied = copy.deepcopy(state)
        state = []
        step += 1
        for s2, d in state_copied:
            zero_row, zero_col = _find_zero_pos(s2)
            cand_pos_list = _swappable_cand((zero_row, zero_col))
            for (row, col) in cand_pos_list:
                s1 = copy.deepcopy(s2)
                s1[zero_row][zero_col], s1[row][col] = s1[row][col], 0
                key = tuple(sum(s1, []))
                if key in generated_boards:
                    if generated_boards[key] != d:
                        return step + steps[key]
                    continue
                state.append((s1, d))
                generated_boards[key] = d
                steps[key] = step
    # Never reaches here.
    return -1


if __name__ == "__main__":
    board = [[0] * 3 for _ in range(3)]

    for row in range(3):
        input_nums = list(map(lambda x: int(x), input().split()))
        for col in range(3):
            # if 0 == input_nums[col]:
            #     zero_pos = (row, col)
            board[row][col] = input_nums[col]

    print(f"{solve_8puzzle(board)}")


from collections import deque
board = [int(s) for _ in range(3) for s in input().split()]
end = [1, 2, 3, 4, 5, 6, 7, 8, 0]
table = set()
def print_board(board):
    for i in range(0, 9, 3):
        print(*board[i:i + 3])

def swap(q, step_q, step, board):
    key = tuple(board)
    if key in table:
        return
    else:
        table.add(key)

    empty = board.index(0)
    def _swap(q, step_q, step, board, k, s):
        b = board.copy()
        b[k], b[s] = b[s], b[k]
        q.append(b)
        step_q.append(step + 1)

    if empty % 3 != 2:
        _swap(q, step_q, step, board, empty, empty + 1)
    if empty % 3 != 0:
        _swap(q, step_q, step, board, empty, empty - 1)
    if empty // 3 < 2:
        _swap(q, step_q, step, board, empty, empty + 3)
    if empty // 3 > 0:
        _swap(q, step_q, step, board, empty, empty - 3)


q = deque([board])
step_q = deque([0])
# print_board(board)
while q[0] != end:
    b = q.popleft()
    step = step_q.popleft()
    swap(q, step_q, step, b)
# print_board(q.popleft())
print(step_q.popleft())

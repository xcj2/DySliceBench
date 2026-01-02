# 幅優先探索 #双方向探索
import sys
import queue

SPACE = 0

adjacents_list = (
    (1, 3),       # 0
    (0, 2, 4),    # 1
    (1, 5),       # 2
    (0, 4, 6),    # 3
    (1, 3, 5, 7), # 4
    (2, 4, 8),    # 5
    (3, 7),       # 6
    (4, 6, 8),    # 7
    (5, 7)        # 8
)

class State:
    def __init__(self, board, space, prev):
        self.board = board
        self.space = space
        self.prev = prev

def mininum_steps(start, goal):
    if start == goal:
        return 0
    q = queue.Queue()
    q.put(State(start, start.index(0), None))
    history = {}
    history[tuple(start)] = True
    while not q.empty():
        state = q.get()
        for adjacent in adjacents_list[state.space]:
            board = state.board[:]
            board[state.space] = board[adjacent]
            board[adjacent] = SPACE
            if tuple(board) in history:
                 continue
            if board == goal:
                return go_back(state)
            history[tuple(board)] = True
            next_state = State(board, adjacent, state)
            q.put(next_state)

step = 0
def go_back(state):
    global step
    if state is not None:
        step += 1
        go_back(state.prev)
    return step


initial_board = list(map(int, sys.stdin.read().split()))
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

print(mininum_steps(initial_board, goal))


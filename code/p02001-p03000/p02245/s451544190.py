class Queue:
    '''
    パズルオブジェクトを格納するキュークラス
    '''
    def __init__(self, puzzle):
        self.puzzle_list = []

        self.puzzle_list.append(puzzle)

    def enqueue(self, puzzle):
        self.puzzle_list.append(puzzle)

    def dequeue(self):
        return self.puzzle_list.pop(0)
    def is_empty(self):
        return len(self.puzzle_list) == 0


class _8Puzzle:
    def __init__(self, panel_list, state_list, size):
        self.panel_list = panel_list

        self.state_list = state_list
        self.state_list.append(panel_list)

        self.size = size

    # パネルの0を左右上下に移動させたときのパネル配置を返すジェネレーター
    def gene_next_panel(self, puzzle):
        zero_pos = puzzle.panel_list.index(0)
        col = zero_pos // self.size
        raw = zero_pos % self.size

        def __get_next_panel():
            panel_list = puzzle.panel_list[:]
            n = panel_list[next_pos]
            panel_list[next_pos] = 0
            panel_list[zero_pos] = n
            return panel_list

        if self.size > col + 1:
            next_pos = (col + 1) * self.size + raw
            panel_list = __get_next_panel()
            yield tuple(panel_list)

        if col - 1 >= 0:
            next_pos = (col - 1) * self.size + raw
            panel_list = __get_next_panel()
            yield tuple(panel_list)

        if self.size > raw + 1:
            next_pos = col * self.size + raw + 1
            panel_list = __get_next_panel()
            yield tuple(panel_list)

        if raw - 1 >= 0:
            next_pos = col * self.size + raw - 1
            panel_list = __get_next_panel()
            yield tuple(panel_list)

    def result_print(self):
        i = 0
        for s in self.state_list:
            i += 1

        print(i-1)

def breadth_first(size, goal, panel_list):
    puzzle = _8Puzzle(panel_list, [], size)
    queue = Queue(puzzle)
    checked_dict = {}

    while queue.is_empty() is False:
        puzzle = queue.dequeue()
        num = 0
        for next_panel in puzzle.gene_next_panel(puzzle):
            next_puzzle = _8Puzzle(list(next_panel), puzzle.state_list[:], size)

            if next_panel in checked_dict:
                continue

            if list(next_panel) == goal:

                return next_puzzle

            checked_dict[next_panel] = True
            queue.enqueue(next_puzzle)

if __name__ == '__main__':
    size = 3
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    input_puzzle = []
    for i in range(3):
        _in1, _in2, _in3 = (int(z) for z in input().split())
        input_puzzle.append(_in1)
        input_puzzle.append(_in2)
        input_puzzle.append(_in3)

    if goal == input_puzzle:
        print(0)
        exit()

    puzzle = breadth_first(size, goal, input_puzzle)

    puzzle.result_print()


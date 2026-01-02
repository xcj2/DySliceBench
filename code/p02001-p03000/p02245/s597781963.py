from heapq import heappop, heappush
from copy import deepcopy


class Board:
    def __init__(self, size, nums):
        self.size = size
        self.nums = nums
        self.code = self._code()

    def __eq__(self, other):
        return self.code == other.code

    def __lt__(self, other):
        return self.code < other.code

    def __gt__(self, other):
        return self.code > other.code

    def __hash__(self):
        nums = tuple(self.nums[i][j]
                     for i in range(self.size)
                     for j in range(self.size))
        return hash(nums)

    def same(self, other):
        if other is None:
            return False
        if self.__class__ != other.__class__:
            return False

        for i in range(self.size):
            for j in range(self.size):
                if self.nums[i][j] != other.nums[i][j]:
                    return False
        return True

    def solved(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) != self._validpos(self.nums[i][j]):
                    return False
        return True

    def _validpos(self, num):
        if num > 0:
            return ((num-1) // self.size, (num-1) % self.size)
        else:
            return (self.size-1, self.size-1)

    def _code(self):
        code = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.nums[i][j] != 0:
                    vi, vj = self._validpos(self.nums[i][j])
                    code += abs(vi - i) + abs(vj - j)
        return code

    def find(self, num):
        for i in range(self.size):
            for j in range(self.size):
                if self.nums[i][j] == num:
                    return (i, j)
        raise IndexError()

    def move(self, p1, p2):
        i1, j1 = p1
        i2, j2 = p2
        nums = deepcopy(self.nums)
        nums[i1][j1], nums[i2][j2] = nums[i2][j2], nums[i1][j1]
        return self.__class__(self.size, nums)

    def moves(self):
        i, j = self.find(0)
        if i > 0:
            yield self.move((i, j), (i-1, j))
        if j > 0:
            yield self.move((i, j), (i, j-1))
        if i < self.size-1:
            yield self.move((i, j), (i+1, j))
        if j < self.size-1:
            yield self.move((i, j), (i, j+1))

    def __str__(self):
        s = ''
        for i in range(self.size):
            for j in range(self.size):
                s += ' {}'.format(self.nums[i][j])
            s += '\n'
        return s


class EightPuzzle:
    def __init__(self, board):
        self.board = Board(3, board)
        self.steps = 0

        if not self.board.solved():
            self._solve()

    def _solve(self):
        bs = []
        checked = {}
        heappush(bs, (self.board.code, self.board, 0))

        while len(bs) > 0:
            w, b, step = heappop(bs)
            if 0 < self.steps <= step:
                continue
            checked[b] = step
            for nb in b.moves():
                if nb.solved():
                    self.steps = step+1
                    return
                elif nb in checked and checked[nb] <= step:
                    continue
                else:
                    heappush(bs, (nb.code + step + 1, nb, step+1))


def run():
    board = []
    for i in range(3):
        board.append([int(i) for i in input().split()])

    eight_puzzle = EightPuzzle(board)
    print(eight_puzzle.steps)


if __name__ == '__main__':
    run()


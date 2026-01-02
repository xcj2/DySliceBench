from copy import deepcopy


class EightQueen:
    NQUEENS = 8
    SIZE = 8

    class Board:
        def __init__(self, size):
            self.queens = []
            self.size = size

        def place(self, i, j):
            self.queens.append((i, j))

        def count(self):
            return len(self.queens)

        def ok(self, i, j):
            for qi, qj in self.queens:
                if qi == i:
                    return False
                if qj == j:
                    return False
                if i - j == qi - qj:
                    return False
                if i + j == qi + qj:
                    return False
            return True

        def __str__(self):
            result = []
            for i in range(self.size):
                s = ''
                for j in range(self.size):
                    if (i, j) in self.queens:
                        s += "Q"
                    else:
                        s += "."
                result.append(s)
            return '\n'.join(result)

    def __init__(self):
        self.board = self.Board(self.SIZE)

    def add_queen(self, i, j):
        self.board.place(i, j)

    def solve(self):
        def _solve(board, si, sj):
            if board.count() == self.NQUEENS:
                return board

            for i, j in _from_pos(si, sj):
                if board.ok(i, j):
                    b = deepcopy(board)
                    b.place(i, j)
                    result = _solve(b, i, j)
                    if result is not None:
                        return result
            else:
                return None

        def _from_pos(i, j):
            for n in range(i*self.SIZE + j, self.SIZE*self.SIZE):
                yield (n // self.SIZE, n % self.SIZE)

        self.board = _solve(self.board, 0, 0)

    def __str__(self):
        if self.board is None:
            return 'no solution'
        else:
            return str(self.board)


def run():
    n = int(input())
    q = EightQueen()

    for _ in range(n):
        i, j = [int(i) for i in input().split()]
        q.add_queen(i, j)

    q.solve()
    print(q)


if __name__ == '__main__':
    run()


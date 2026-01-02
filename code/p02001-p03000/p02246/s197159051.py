
from heapq import heappop, heappush
from functools import lru_cache


@lru_cache(maxsize=None)  
def manhattan(size, i, n):
    if n == 0:
        return 0
    else:
        dn, mn = divmod(n-1, size)
        di, mi = divmod(i, size)
        return abs(dn-di) + abs(mn-mi)


class Board:
    __slots__ = ('size', 'nums', 'code', '_hash')

    def __init__(self, size, nums, code=None):
        self.size = size  
        self.nums = nums  
        self._hash = hash(nums)
        if code is None:  
            self.code = sum([manhattan(self.size, i, n)
                             for i, n in enumerate(self.nums) if n != i+1])
        else:
            self.code = code

    def __eq__(self, other):
        return self.code == other.code

    def __lt__(self, other):
        return self.code < other.code

    def __gt__(self, other):
        return self.code > other.code

    def __hash__(self):   
        return self._hash 

    def same(self, other):
        if other is None: 
            return False  
        if self.__class__ != other.__class__:
            return False

        for i in range(self.size * self.size):
            if self.nums[i] != other.nums[i]:
                return False
        return True

    def solved(self):
        for i in range(self.size * self.size):
            if self.nums[i] > 0 and self.nums[i] - 1 != i:
                return False
        return True

    def find(self, num):
        for i in range(self.size * self.size):
            if self.nums[i] == num:
                return i
        raise IndexError()

    def move(self, p1, p2):
        nums = list(self.nums)
        v1, v2 = nums[p1], nums[p2]
        code = (self.code - manhattan(self.size, p1, v1)
                - manhattan(self.size, p2, v2)
                + manhattan(self.size, p2, v1)
                + manhattan(self.size, p1, v2))
        nums[p1], nums[p2] = v2, v1
        return self.__class__(self.size, tuple(nums), code)

    def moves(self):
        i = self.find(0)
        if i > self.size-1:
            yield self.move(i, i-self.size)
        if i % self.size > 0:
            yield self.move(i, i-1)
        if i < self.size*(self.size-1):
            yield self.move(i, i+self.size)
        if (i+1) % self.size > 0:
            yield self.move(i, i+1)

    def __str__(self):
        s = ''
        for i in range(self.size*self.size):
            s += ' {}'.format(self.nums[i])
            if (i + 1) % self.size == 0:
                s += '\n'
        return s

class FifteenPuzzle:
    def __init__(self, board, maxmove):
        self.board = board
        self.maxmove = maxmove
        if not board.solved():
            self.steps = self._solve()
        else:
            self.steps = 0

    def _solve(self):
        bs = []
        checked = set()
        i = 0
        heappush(bs, (self.board.code, self.board.code, i, self.board, 0))

        while len(bs) > 0:
            w, _, _, b, step = heappop(bs)
            checked.add(b)
            step += 1
            for nb in b.moves():
                if nb.solved():
                    return step
                elif self.maxmove < nb.code + step:
                    continue
                elif nb in checked:
                    continue
                else:
                    i += 1
                    heappush(bs, (nb.code + step, nb.code, i, nb, step))
        return -1


def run():
    ns = []
    for i in range(4):
        ns.extend([int(i) for i in input().split()])

    board = Board(4, tuple(ns))
    puzzle = FifteenPuzzle(board, 45)
    print(puzzle.steps)


if __name__ == '__main__':
    run()




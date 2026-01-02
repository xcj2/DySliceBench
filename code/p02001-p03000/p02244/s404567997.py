from collections import namedtuple

State = namedtuple("State", "queen row col dpos dneg")


def put_queen(s, r, c):
    s.queen[r] = c
    s.row[r] = s.col[c] = s.dpos[r + c] = s.dneg[r - c + 8 - 1] = True


def unput_queen(s, r, c):
    s.queen[r] = None
    s.row[r] = s.col[c] = s.dpos[r + c] = s.dneg[r - c + 8 - 1] = False


def read_board(s):
    k = int(input())
    for _ in range(k):
        r, c = [int(x) for x in input().split()]
        put_queen(s, r, c)
    return s


def print_board(s):
    for r in range(8):
        for c in range(8):
            print("Q" if s.queen[r] == c else ".", end="")
        print()


def eight_queens(s):
    def rec(r, s):
        if r == 8:
            return s
        elif s.queen[r] is not None:
            return rec(r + 1, s)
        else:
            for c in range(8):
                if s.col[c] or s.dpos[r + c] or s.dneg[r - c + 8 - 1]:
                    continue
                new_s = State(
                    s.queen[:], s.row[:], s.col[:], s.dpos[:], s.dneg[:]
                )
                put_queen(new_s, r, c)
                result = rec(r + 1, new_s)
                if result:
                    return result
            return False

    return rec(0, s)


def main():
    s = State(
        [None] * 8,
        [False] * 8,
        [False] * 8,
        [False] * (2 * 8 - 1),
        [False] * (2 * 8 - 1),
    )

    print_board(eight_queens(read_board(s)))


main()


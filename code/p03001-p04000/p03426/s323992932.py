#!/usr/bin/env pypy3

import itertools


class CumulativeSum(object):
    """Constructs the cumulative sum of the elements in the given sequence.

    :param sequence: The sequence to be processed.
    :type sequence: sequence
    """

    def __init__(self, sequence):
        self.cumulative_sum = [0]
        self.cumulative_sum.extend(itertools.accumulate(sequence))

    def partial_sum(self, first, last):
        """Computes the partial sum of the sequence.

        :param first: The index representing the first element of the
                      subsequence.
        :type first: int
        :param last: The index representing the last element of the
                     subsequence.
        :return: The partial sum.
        """
        return self.cumulative_sum[last + 1] - self.cumulative_sum[first]


def prepare(h, w, d, board):
    val2pos = [None for _ in range(h * w + 1)]
    for r, c in itertools.product(range(h), range(w)):
        val2pos[board[r][c]] = (r, c)
    max_e = h * w // d
    cumsums = []
    for m in range(d):
        max_e = (h * w - m) // d
        costs = []
        for e in range(max_e + 1):
            if e == 0:
                costs.append(0)
            else:
                x0 = (e - 1) * d + m
                if x0 != 0:
                    r0, c0 = val2pos[x0]
                    x1 = e * d + m
                    r1, c1 = val2pos[x1]
                    cost = abs(r1 - r0) + abs(c1 - c0)
                else:
                    cost = 0
                costs.append(cost)
        cumsums.append(CumulativeSum(costs))
    return cumsums


def main():
    h, w, d = (int(x) for x in input().split())
    board = [[int(b) for b in input().split()] for _ in range(h)]
    cumsums = prepare(h, w, d, board)
    q = int(input())
    for _ in range(q):
        l, r = (int(x) for x in input().split())
        dl, ml = divmod(l, d)
        dr, mr = divmod(r, d)
        res = cumsums[ml].partial_sum(dl + 1, dr)
        # print(cumsums[ml].cumulative_sum)
        # print(dl + 1, dr)
        print(res)


if __name__ == '__main__':
    main()

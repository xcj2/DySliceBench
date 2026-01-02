#!/usr/bin/env python3
import sys
import heapq


class Reverse:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return repr(self.val)


class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            for i in range(len(arr)):
                arr[i] = Reverse(arr[i])
        self.desc = desc
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        if self.desc:
            return heapq.heappop(self.hq).val
        else:
            return heapq.heappop(self.hq)

    def push(self, a):
        if self.desc:
            heapq.heappush(self.hq, Reverse(a))
        else:
            heapq.heappush(self.hq, a)

    def top(self):
        if self.desc:
            self.hq[0].val
        else:
            return self.hq[0]


def solve(N: int, M: int, A: "List[int]"):
    hq = Heapq(A, desc=True)
    while M > 0:
        MD = hq.pop()
        M -= 1
        hq.push((MD//2))
        if MD <= 0:
            break
    ans = 0
    while A:
        a = hq.pop()
        ans += a
    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == '__main__':
    main()

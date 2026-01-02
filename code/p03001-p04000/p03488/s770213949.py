#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def can_make(steps, t, init):
    cur = {init}
    for s in steps:
        nex = set()
        for c in cur:
            nex.add(c + s)
            nex.add(c - s)
        cur = nex
    if t in cur:
        return True
    return False


def solve(s: str, x: int, y: int):
    steps = [[], []]
    flg = 0
    tmp = 0
    for c in s:
        if c == 'T':
            steps[flg].append(tmp)
            flg = (flg + 1) % 2
            tmp = 0
        else:
            tmp += 1
    steps[flg].append(tmp)
    #print(steps)
    init_x = steps[0][0] if len(steps[0]) > 0 else 0
    if can_make(steps[0][1:], x, init_x) and can_make(steps[1], y, 0):
        ret = YES
    else:
        ret = NO
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(s, x, y)

if __name__ == '__main__':
    main()

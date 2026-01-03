# https://beta.atcoder.jp/contests/abc065/tasks/abc065_b

import sys


def model():
    e = list(map(int, sys.stdin))
    cur = e[1]
    for i in range(e[0]):
        if cur == 2:
            print(i + 1)
            break
        cur = e[cur]
    else:
        print(-1)


def input_lines():
    """hell?"""
    lines = sys.stdin.readlines()
    for i in range(1, int(lines[0])+1):
        yield i, int(lines[i].strip())


def solve():
    d = {i: button for i, button in input_lines()}
    count = 1
    index = 1

    while True:
        try:
            prev = index
            index = d[index]

            if index is None:
                print(-1)
                exit()
            elif index == 2:
                print(count)
                exit()
            d[prev] = None
            count += 1
        except KeyError:
            print(-1)
            exit()


if __name__ == '__main__':
    solve()
    # model()

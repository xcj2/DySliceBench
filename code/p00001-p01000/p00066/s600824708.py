# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0066
"""
import sys


def prepare_board(size=3):
    return [[1]*size for _ in range(size)]


def check_horizontal(status):
    dp = prepare_board()
    for y in range(len(status)):
        for x in range(1, len(status[0])):
            if status[y][x] == status[y][x-1]:
                dp[y][x] = dp[y][x-1] + 1
                if dp[y][x] == 3:
                    if status[y][x] != 's':
                        return status[y][x]
    return 'd'


def check_vertical(status):
    dp = prepare_board()
    for y in range(1, len(status)):
        for x in range(len(status[0])):
            if status[y][x] == status[y-1][x]:
                dp[y][x] = dp[y-1][x] + 1
                if dp[y][x] == 3:
                    if status[y][x] != 's':
                        return status[y][x]
    return 'd'


def check_diagonal(status):
    # ????????????????????????????§??????????????????§??????
    dp = prepare_board()
    for y in range(1, len(status)):
        for x in range(1, len(status[0])):
            if status[y][x] == status[y-1][x-1]:
                dp[y][x] = dp[y-1][x-1] + 1
                if dp[y][x] == 3:
                    if status[y][x] != 's':
                        return status[y][x]

    # ????????????????????????????§??????????????????§??????
    dp = prepare_board()
    for y in range(1, len(status)):
        for x in range(len(status[0])-2, -1, -1):
            if status[y][x] == status[y-1][x+1]:
                dp[y][x] = dp[y-1][x+1] + 1
                if dp[y][x] == 3:
                    if status[y][x] != 's':
                        return status[y][x]
    return 'd'


def solve(status):
    result = check_horizontal(status)
    if result != 'd':
        return result
    result = check_vertical(status)
    if result != 'd':
        return result
    return check_diagonal(status)


def main(args):
    for line in sys.stdin:
        # ??\???????????????3x3?????¶????????????????????????????§£?????¢??°?????????
        status = []
        line = line.strip()
        status.append(list(line[:3]))
        status.append(list(line[3:6]))
        status.append(list(line[6:]))
        result = solve(status)

        # ?????????????¨?
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])
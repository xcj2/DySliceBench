#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()

    statements = []
    for _ in range(N):
        a = II()
        statement = []
        for _ in range(a):
            hatugen = LI()
            statement.append(hatugen)
        statements.append(statement)

    ans = 0
    for i in range(2**N):
        flag = True
        i_str = format(i, f"0{N}b")
        for n in range(N):
            if i_str[n] == '0':
                continue

            for statement in statements[n]:
                target = statement[0]
                seisitu = statement[1]

                if i_str[target - 1] != str(seisitu):
                    flag = False

        if flag:
            tmp = 0
            for n in range(N):
                tmp += int(i_str[n])

            ans = max(ans, tmp)

    print(ans)


main()

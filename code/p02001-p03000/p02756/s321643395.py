import sys
# sys.setrecursionlimit(100000)
from collections import deque


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    s = deque(list(input()))
    q = input_int()
    inverse = False
    for _ in range(q):
        data = input().split()
        if len(data) == 1:
            inverse = not inverse
        else:
            if (data[1] == "1" and not inverse) or (data[1] == "2" and inverse):
                s.appendleft(data[2])
            else:
                s.append(data[2])
    if inverse:
        print("".join(reversed(s)))
    else:
        print("".join(s))
    return


if __name__ == "__main__":
    main()

# import sys
# input = sys.stdin.readline
import collections
import itertools

def main():
    h, w = input_list()
    maze = [list(input()) for _ in range(h)]
    ans = []
    blacks = [False] * w
    for m in maze:
        for i, v in enumerate(m):
            if v == "#":
                blacks[i] = True
    for m in maze:
        f = True
        new_row = []
        for i, b in enumerate(blacks):
            if b:
                new_row.append(m[i])
        for i, v in enumerate(new_row):
            if v == "#":
                f = False
                break
        if f:
            continue
        ans.append(new_row)
    for a in ans:
        print("".join(a))


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()

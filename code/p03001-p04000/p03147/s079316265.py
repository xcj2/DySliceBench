# import sys
# input = sys.stdin.readline
import collections

def main():
    n = int(input())
    h = input_list()
    count = 0
    while True:
        if list(set(h)) == [0]:
            break
        count += 1
        f = False
        for i, v in enumerate(h):
            if v == 0:
                if f:
                    break
            if v > 0:
                h[i] -= 1
                f = True
    print(count)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()

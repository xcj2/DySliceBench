import math


def inputIntList():
    return [int(s) for s in input().split()]


def inputInt():
    return int(input())


def main():
    N = inputInt()
    S = [int(s) for s in input()]

    ret = 0
    for i in range(1000):
        code = [int(i / 10 ** j) % 10 for j in range(2, -1, -1)]
        # print(code)
        j = 0
        for s in S:
            if code[j] == s:
                j += 1
            if j == 3:
                break
        if j == 3:
            ret += 1
    return ret


if __name__ == "__main__":
    print(main())

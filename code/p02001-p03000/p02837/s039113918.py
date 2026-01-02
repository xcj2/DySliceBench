import math


def inputIntList():
    return [int(s) for s in input().split()]


def inputInt():
    return int(input())


def main():
    N = inputInt()
    A = [[] for _ in range(N)]
    for i in range(N):
        for _ in range(inputInt()):
            A[i].append(inputIntList())
    ret = 0
    for i in range(2 ** N):
        bits = [i >> j & 1 for j in range(N)]
        for i, a in enumerate(A):
            if bits[i] == 0:
                continue
            for x, y in a:
                # print(bits, bits[x - 1], y)
                if bits[x - 1] == y:
                    continue
                break
            else:
                continue
            break
        else:
            ret = max(ret, sum(bits))
    return ret


if __name__ == "__main__":
    print(main())

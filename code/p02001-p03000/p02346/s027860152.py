import sys

BIT = []
n = 0


def init():
    # 初期化
    global BIT, n

    BIT = [0] * (n + 1)  # BIT は 最初のインデックスは 1(0001)


def add(i, x):

    global BIT, n

    # A[i] に x を加える動作
    while i < n + 1:
        BIT[i] += x
        i += (i & -i)  # i & -i は最下位ビットを取り出す動作


def sum(i):
    # i までの和

    global BIT, n

    _sum = 0
    while i > 0:
        _sum += BIT[i]
        i -= (i & -i)  # i & -i は最下位1ビットを表す

    return _sum


def main():

    global BIT, n
    n, q = map(int, sys.stdin.readline().rstrip().split())

    init()

    # print(n, len(BIT), BIT)

    for _ in range(q):
        com, x, y = map(int, sys.stdin.readline().rstrip().split())

        if com == 0:
            add(x, y)
            # print("add", BIT)
        else:
            # print(BIT)
            print(sum(y) - sum(x - 1))


main()


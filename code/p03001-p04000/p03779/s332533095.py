def limit():
    """
    i=44721

    全探索
    0 = [0]
    1 = [1,-1,0]と0の組合せ
    2 = [2,-2,0]と1の組合せ
    3**44721 => 無理
    """
    s = 0
    x = 10 ** 9
    for i in range(x):
        s += i
        if s >= x:
            print(i)
            break


def TLE(X):
    """
    11
    1 {0, 1, -1}
    2 {0, 1, 2, 3, -3, -1, -2}
    3 {0, 1, 2, 3, 4, 5, 6, -6, -5, -4, -3, -1, -2}
    4 {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -1, -2}
    ans: 5
    """
    from itertools import product
    pos = set([0])
    for i in range(1, X + 1):
        for x, y in product(pos, (i, -i, 0)):
            if x + y == X:
                return i
            pos.add(x + y)
        print(i, pos)


def main():
    X = int(input())

    s = 0
    for i in range(1, X + 1):
        s += i
        if X <= s:
            print(i)
            break

if __name__ == '__main__':
    main()

import sys
input = sys.stdin.readline


def readstr():
    return input().strip()


def readint():
    return int(input())


def readnums():
    return map(int, input().split())


def readstrs():
    return input().split()


def main():
    x, y = readnums()
    '''
    x <= yかx > yか
    x, yの正負
    x, yの差
    x, y
    1, 3 2
    -1, 3 3
    1, -3 3
    -1, -3 4
    3, 1 4
    -3, 1 3
    3, -1 3
    -3, -1 2

    10, 0 11
    -10, 0 10
    0, 10 10
    0, -10 11
    '''
    ans = 0
    if x == 0 or y == 0:
        ans = abs(x - y) if x < 0 or y > 0 else abs(x - y) + 1
    elif (x >= 0 and y >= 0) or (x < 0 and y < 0):
        ans = y - x if x <= y else abs(abs(x) - abs(y)) + 2
    else:
        ans = abs(abs(y) - abs(x)) + 1
    print(ans)


if __name__ == "__main__":
    main()

def main():
    x1, y1, x2, y2 = map(int, input().split())

    ans = editorial(x1, y1, x2, y2)
    # assert ans == twi(x1, y1, x2, y2)
    print(*ans)


def twi(x1, y1, x2, y2):
    """
    https://twitter.com/akensho/status/1035924165205716992
    https://twitter.com/hogeover30/status/1035903937830764545
    """
    import math
    cos90 = int(math.cos(math.pi / 2))
    sin90 = int(math.cos(math.pi / 2))

    x = x2 - x1
    y = y2 - y1
    x4 = x * cos90 - y * sin90 + x1
    y4 = x * sin90 + y * cos90 + y1

    x = x1 - x4
    y = y1 - y4
    x3 = x * cos90 - y * sin90 + x4
    y3 = x * sin90 + y * cos90 + y4

    return x3, y3, x4, y4


def editorial(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1

    x3 = x2 - y
    y3 = y2 + x
    x4 = x1 - y
    y4 = y1 + x

    return x3, y3, x4, y4


if __name__ == '__main__':
    main()

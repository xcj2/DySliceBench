def main():
    x, y = map(int, input().split())

    ans = f(x, y)
    print(ans)


def f(x, y):
    if x == y:
        ans = 0
    elif x >= 0 and y >= 0:
        if x < y:
            # x:0, y:3
            ans = y - x
        elif y == 0:
            # x:3, y:0 -> x:-3,-2,-1,0
            ans = 1 + x
        else:
            # x:3, y:1 -> x:-3,-2,-1,1
            ans = 1 + abs(y - x) + 1
    elif x < 0 and y < 0:
        if x < y:
            # x:-3, y:0
            ans = y - x
        else:
            # x:-2, y:-3 -> x:  2,3,-3
            ans = 1 + abs(y - x) + 1
    elif x < 0 and y == 0:
        # x:-5, y:0 -> x:-4,-3,-2,-1,0
        ans = abs(x)
    elif x < 0 < y:
        if abs(x) <= y:
            # x:-1, y:4 -> x:1,2,3,4
            ans = 1 + y + x
        else:
            # x:-5, y:4 -> x:-4,4
            ans = abs(y + x) + 1
    elif x == 0 and y < 0:
        # x:0, y:-4 -> x:1,2,3,4,-4
        ans = abs(y) + 1
    elif x > 0 > y:
        if x >= abs(y):
            # x:3, y:-1 -> x:-3,-2,-1
            ans = 1 + x + y
        else:
            # x:3, y:-4 -> x:      4,-4
            ans = abs(y + x) + 1

    return ans


def note():
    """
    x,yについて =0,<0,0> の全列挙
    3*3=9
    例外:x == y

    x == 0 and y == 0(例外に含まれる)
    x == 0 and y >  0
    x == 0 and y <  0

    x >  0 and y == 0
    x >  0 and y >  0
    x >  0 and y <  0

    x <  0 and y == 0
    x <  0 and y >  0
    x <  0 and y <  0

    実装しやすさによって、<=,>=を変更
    """


if __name__ == '__main__':
    main()

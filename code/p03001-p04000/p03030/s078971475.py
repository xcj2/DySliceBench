def make_guide():
    num = int(input())
    lst = [(i + 1, input().split()) for i in range(num)]
    # TODO fix
    # 同じものが存在したら、っていう条件のもとでないとダメ
    # あと数字は降順
    lst = sorted(lst, key=lambda t: int(t[1][1]), reverse=True)
    lst = sorted(lst, key=lambda t: t[1][0])
    return lst


def test_display():
    lst = make_guide()
    for i, guides in lst:
        print(str(i) + " " + guides[0] + " " + guides[1])


def display():
    lst = make_guide()
    for i, guides in lst:
        print(i)


if __name__ == "__main__":
    display()

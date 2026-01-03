def main(a, b, x):
    if x > b:
        return 0
    elif x == b:
        return 1

    minimum, maximum = None, None

    for i in range(a, b + 1):
        if i % x == 0:
            minimum = i
            break

    for i in range(b, a - 1, -1):
        if i % x == 0:
            maximum = i
            break

    if minimum != None or maximum != None:
        if minimum != None and maximum != None:
            # 普通の / 除算だと3で割ったときに大きくずれる。
            return (maximum - minimum) // x + 1
        else:
            return 1
    else:
        return 0


def main_b(a, b, x):
    """解説を読んだ。単純なことだった。
    """
    def count(n):
        if n == -1:
            return 0
        else:
            return n // x + 1

    return count(b) - count(a-1)


if __name__ == "__main__":
    a, b, x = [int(x) for x in input().split()]
    print(main_b(a, b, x))

def layers(n):
    result = 1
    for _ in range(0, n):
        result = result * 2 + 3
    return result


def meat(n):
    result = 1
    for _ in range(0, n):
        result = result * 2 + 1
    return result


def calc(n, x):
    before_layer = layers(n - 1)
    before_meat = meat(n - 1)
    if x == 1:
        return 1 if n == 0 else 0
    elif x <= 1 + before_layer:
        return calc(n - 1, x - 1)
    elif x == 2 + before_layer:
        return 1 + before_meat
    elif x <= 2 + 2 * before_layer:
        return 1 + before_meat + calc(n - 1, x - 2 - before_layer)
    elif x == 3 + 2 * before_layer:
        return 2 * before_meat + 1


def main():
    n, x = map(int, input().split())
    print(calc(n, x))


if __name__ == '__main__':
    main()


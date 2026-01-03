from sys import stdin


def main():
    w = next_int()
    h = next_int()
    n = next_int()
    arr = [[1] * w for _ in range(h)]

    for i in range(n):
        xi, yi, a = map(int, input().split())

        for y in range(h):
            for x in range(w):
                if a == 1:
                    if x < xi:
                        arr[y][x] = 0
                if a == 2:
                    if x >= xi:
                        arr[y][x] = 0
                if a == 3:
                    if y < yi:
                        arr[y][x] = 0
                if a == 4:
                    if y >= yi:
                        arr[y][x] = 0

    ans = 0
    for y in range(h):
        ans += sum(arr[y])
    print(ans)


def next_int():
    return int(next_str())


def next_str():
    result = ""
    while True:
        tmp = stdin.read(1)
        if tmp.strip() != "":
            result += tmp
        elif tmp != '\r':
            break
    return result


if __name__ == '__main__':
    main()
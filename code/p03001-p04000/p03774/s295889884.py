from sys import stdin
from sys import maxsize


def main() -> int:
    n = next_int()
    m = next_int()

    students = [tuple(map(int, input().split())) for _ in range(n)]
    check_points = [tuple(map(int, input().split())) for _ in range(m)]

    for i in range(n):
        index = 0
        value = maxsize
        for j in range(m):
            x1 = students[i][0]
            y1 = students[i][1]
            x2 = check_points[j][0]
            y2 = check_points[j][1]
            calc_result = calc(x1, x2, y1, y2)

            if calc_result < value:
                index = j
                value = calc_result
        print(index + 1)
    return 0


def calc(x1, x2, y1, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def next_int() -> int:
    return int(next_str())


def next_str() -> str:
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
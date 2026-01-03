import sys

ans = []


def main() -> None:
    x, y = [int(next_str()) for _ in range(2)]

    for i in range(4):
        solve(i, x, y)

    print(min(ans))


def solve(i: int, x: int, y: int) -> None:
    global ans
    t = 0

    if i % 2 > 0:
        x *= -1
        t += 1

    if i < 2:
        y *= -1
        t += 1

    if x <= y:
        t += y - x
        ans.append(t)


def next_str() -> str:
    result = ""
    while True:
        tmp = sys.stdin.read(1)
        if tmp.strip() != "":
            result += tmp
        elif tmp != '\r':
            break
    return result


if __name__ == '__main__':
    main()
import sys


def next_str() -> str:
    result = ""
    while True:
        tmp = sys.stdin.read(1)
        if tmp.strip() != "":
            result += tmp
        elif tmp != '\r':
            break
    return result


def next_int() -> int:
    return int(next_str())


def main() -> None:
    n = next_int()
    od = 0
    ev = 0

    for i in range(n):
        a = next_int()
        if a % 2 == 0:
            ev += 1
        else:
            od += 1

        if od == 2:
            od = 0
            ev += 1

        if ev == 2:
            ev = 1
    
    print("YES" if ev + od == 1 else "NO")


if __name__ == '__main__':
    main()
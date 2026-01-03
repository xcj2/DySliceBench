from sys import stdin


def main() -> int:
    a = next_str()
    b = next_str()
    print(("GREATER", "LESS", "EQUAL")[judge(a, b)])
    return 0


def judge(a: str, b: str) -> int:
    case = len(a) - len(b)
    if case > 0:
        return 0
    elif case < 0:
        return 1
    else:
        for i in range(len(a)):
            case = ord(a[i]) - ord(b[i])
            if case > 0:
                return 0
            elif case < 0:
                return 1
    return 2


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
from sys import stdin


def main() -> None:
    s = next_str()
    print(("WA", "AC")[judge(s)])


def judge(s: str) -> bool:
    flg = False
    n = len(s)

    for i in range(n):
        if i == 0:
            if s[i] != 'A':
                return False
        elif 2 <= i < n - 1 and s[i] == 'C' and not flg:
            flg = True
        elif s[i] != s[i].lower():
            return False

    if not flg:
        return False
    return True


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
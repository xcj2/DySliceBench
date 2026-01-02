import sys
from collections import namedtuple


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
    sword = namedtuple('sw', ('wield', 'throw'))
    n, h = map(int, input().split())
    swords = [sword(next_int(), next_int()) for _ in range(n)]
    cnt = 0

    swords.sort(key=lambda x: x.throw, reverse=True)
    swords.sort(key=lambda x: x.wield)
    main_sword = swords.pop()
    swords.sort(key=lambda x: x.throw)

    while h > 0:
        cnt += 1
        if main_sword.throw >= h:
            h -= main_sword.throw
        elif len(swords) > 0 and main_sword.wield < swords[-1].throw:
            h -= swords.pop().throw
        else:
            h -= main_sword.throw
            cnt += 1 + (h - 1) // main_sword.wield
            break

    print(cnt)


if __name__ == "__main__":
    main()

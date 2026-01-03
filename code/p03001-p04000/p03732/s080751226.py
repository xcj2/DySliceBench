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


item = namedtuple("itm", ("w", "v"))
n, W = map(int, input().split())
items = [item(next_int(), next_int()) for i in range(n)]
dic = dict()


def rec_dp(i: int, w: int) -> int:
    if (i, w) in dic:
        return dic[(i, w)]

    result = 0
    if i == n:
        pass
    elif w - items[i].w < 0:
        result = rec_dp(i + 1, w)
    else:
        result = max(
            rec_dp(i + 1, w),
            rec_dp(i + 1, w - items[i].w) + items[i].v
        )
    dic[(i, w)] = result
    return result


def main() -> None:
    print(rec_dp(0, W))


if __name__ == "__main__":
    main()

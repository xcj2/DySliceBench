import sys
from collections import namedtuple


def next_str() -> str:
    result = ""
    while True:
        tmp = sys.stdin.read(1)
        if tmp.strip() != "":
            result += tmp
        elif tmp != "\r":
            break
    return result


def next_int() -> int:
    return int(next_str())


query = namedtuple('qry', ('l', 'r'))
Q = next_int()
queries = [query(next_int(), next_int()) for i in range(Q)]
right = -sys.maxsize
left = sys.maxsize


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def main() -> None:
    global left, right
    for q in queries:
        left = min(left, q.l)
        right = max(right, q.r)

    dp = [0] * ((right - left) // 2 + 1)

    for i in range(left, right + 1, 2):
        j = (i - left) // 2
        if j != 0:
            dp[j] = dp[j - 1]
        if is_prime(i) and is_prime((i + 1) // 2):
            dp[j] += 1

    for q in queries:
        ans = 0
        ans += dp[(q.r - left) // 2]
        if q.l != left:
            ans -= dp[(q.l - left) // 2 - 1]

        print(ans)


if __name__ == "__main__":
    main()

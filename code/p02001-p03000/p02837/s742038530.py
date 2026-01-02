import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def is_nth_bit_set(x, n):
    if x & (1 << n):
        return True
    else:
        return False


def main():
    N = int(input())

    comments = [[] for _ in range(N)]
    for i in range(N):
        A = int(input())
        for _ in range(A):
            x, y = map(int, input().split())
            x -= 1
            comments[i].append((x, y))

    total = 2 ** N
    ans = 0
    for pattern in range(total):
        flag = True
        tmp = 0
        for i in range(N):
            if is_nth_bit_set(pattern, i):
                tmp += 1
                for x, y in comments[i]:
                    if is_nth_bit_set(pattern, x) == bool(y):
                        continue
                    else:
                        flag = False
                        break
            else:
                continue

            if not flag:
                break

        if flag:
            if tmp > ans:
                ans = tmp

    print(ans)


if __name__ == "__main__":
    main()

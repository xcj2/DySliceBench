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
    N, M = map(int, input().split())
    xyz = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        xyz.append((x, y, z))

    ans = 0
    for i in range(8):
        arr = []
        for x, y, z in xyz:
            tmp = 0
            if is_nth_bit_set(i, 0):
                tmp += x
            else:
                tmp -= x

            if is_nth_bit_set(i, 1):
                tmp += y
            else:
                tmp -= y

            if is_nth_bit_set(i, 2):
                tmp += z
            else:
                tmp -= z
            arr.append(tmp)

        arr.sort(reverse=True)
        ans = max(sum(arr[:M]), ans)

    print(ans)


if __name__ == "__main__":
    main()

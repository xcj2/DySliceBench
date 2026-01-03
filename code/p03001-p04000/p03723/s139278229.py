import sys
input = sys.stdin.readline


def readstr():
    return input().strip()


def readint():
    return int(input())


def readnums():
    return map(int, input().split())


def readstrs():
    return input().split()


def main():
    A, B, C = readnums()
    if A == B and B == C:
        if A == 1:
            print(0)
        else:
            print(-1)
    else:
        ans = 0
        while all([not A % 2, not B % 2, not C % 2]):
            A, B, C = (B + C) // 2, (A + C) // 2, (A + B) // 2
            ans += 1

        print(ans)


if __name__ == "__main__":
    main()

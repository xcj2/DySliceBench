from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def f(n):
    if n < 2:
        return 1
    else:
        return n * f(n - 2)


def solve(N):
    result = f(N)
    count = 0
    for x in str(result)[::-1]:
        if x == '0':
            count += 1
        else:
            break
    return count


def solve2(N):
    if N % 2 == 1:
        return 0
    if N == 0:
        return 0

    a = N // 50
    b = N // 10

    ans = a + b

    for i in range(2, 100000000000):
        x = (5 ** i) * 10
        y = N // x
        if y == 0:
            break
        ans += y

    return ans

    # c = N // 250
    # d = N // 1250
    # e = N // 6250
    # return b + a + c + d + e


def main():
    N = int(stdin.readline().rstrip())
    result = solve2(N)
    print(result)

    # result = solve(N)
    # print(result)

    # ans = []
    # for x in range(1, 300):
    #     result = solve(x)
    #     ans.append((x, result))

    # for x in ans:
    #     a, b = x
    #     print(a, b)

    # current = 0
    # count = 0
    # for x in ans:
    #     a, b = x
    #     if a % 2 == 1:
    #         continue
    #     if b == current:
    #         count += 1
    #     elif b == current + 1:
    #         print(current, count)
    #         current = b
    #         count = 0
    #     else:
    #         print(current, count)
    #         print(current + 1, 0)
    #         current = b
    #         count = 0


if __name__ == "__main__":
    main()

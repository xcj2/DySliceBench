# coding: utf-8
def II(): return int(input())
def ILI(): return list(map(int, input().split()))


def read():
    N = II()
    return (N,)


def solve(N):
    ans = []
    for h in range(1, 3501):
        flag = False
        for n in range(1, 3501):
            if 4 * h * n - N * h - N * n == 0:
                continue
            div, mod = divmod(N * h * n, 4 * h * n - N * h - N * n)
            if mod == 0 and div > 0:
                ans = [h, n, div]
                flag = True
                break
        if flag:
            break
    ans = " ".join(map(str, ans))
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()

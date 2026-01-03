def main():
    S = input()

    AC(S)


def AC(S):
    n = len(S)
    a = [0] * (n-1)

    def rec(i, n):
        ans = 0
        if i == n:
            ss = list(S)
            for j, x in enumerate(a):
                if x == 1:
                    ss[j] = ss[j] + "+"
            #print("".join(ss))
            for x in "".join(ss).split("+"):
                ans += int(x)
            return ans

        a[i] = 1
        ans += rec(i + 1, n)
        a[i] = 0
        ans += rec(i + 1, n)
        return ans
    ans = rec(0, n-1)
    print(ans)


def WA(S):
    ans = 0
    for n in range(len(S)):
        x = f(S, n)
        ans += x

    print(ans)


def f(S, n):
    ans = 0
    if n == 0:
        ans = int(S)
    elif len(S) - 1 == n:
        ans = sum(map(int, S))
    elif n == 1:
        for i in range(len(S)-1):
            x = int(S[:i+1]) + int(S[i+1:])
            ans += x
            print(S, n, i, x)
    else:
        for i in range(len(S)-1):
            x = S[:i+1]
            y = S[i+1:]
            if len(y) > n - 1:
                ans += int(x) + f(y, n-1)

    print(S, n, ans, sep="\t")
    return ans


if __name__ == '__main__':
    main()

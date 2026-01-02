from sys import stdin


def main():
    K = int(stdin.readline().rstrip())

    def check(x):
        s = str(x)
        for i in range(len(s) - 1):
            if 1 < abs(int(s[i]) - int(s[i + 1])):
                return False
        return True

    if K <= 100:
        count = 0
        i = 1
        while True:
            if check(i):
                count += 1
            if count == K:
                print(i)
                return
            i += 1
    else:
        def inner(n):
            s = str(n)
            for idx in range(len(s) - 1, 0, -1):
                c1 = int(s[idx])
                c2 = int(s[idx - 1])
                if c1 != 9 and ((c2 - 1) == c1 or c2 == c1):
                    c1 += 1
                    new_s = s[:idx] + str(c1)
                    for _ in range(len(s) - len(new_s)):
                        new_s += str(max(int(new_s[-1]) - 1, 0))
                    return int(new_s)
            if int(s[0]) != 9:
                new_s = str(int(s[0]) + 1)
                for _ in range(len(s) - len(new_s)):
                    new_s += str(max(int(new_s[-1]) - 1, 0))
                return int(new_s)
            else:
                new_s = '1'
                for _ in range(len(s)):
                    new_s += str(max(int(new_s[-1]) - 1, 0))
                return int(new_s)

        ans = 878
        for i in range(101, K + 1):
            ans = inner(ans)
        print(ans)


if __name__ == "__main__":
    main()

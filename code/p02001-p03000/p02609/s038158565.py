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
    N = readint()
    X = readstr()
    s = sum(tuple(map(int, X)))
    s1 = s + 1
    s2 = s - 1 if s != 1 else 1
    m1 = int(X, 2) % s1
    m2 = int(X, 2) % s2
    t1 = [1]
    t2 = [1]
    for i in range(N):
        t1.append(t1[i] * 2 % s1)
        t2.append(t2[i] * 2 % s2)
    for i in range(N):
        ans = 0
        if X[i] == '0':
            x = (m1 + t1[(N - i - 1)]) % s1
        else:
            if s == 1:
                print(0)
                continue
            else:
                x = (m2 - t2[(N - i - 1)]) % s2
        d = sum(tuple(map(int, bin(x)[2:])))
        ans += 1
        while x:
            x %= d
            d = sum(tuple(map(int, bin(x)[2:])))
            ans += 1
        print(ans)


if __name__ == "__main__":
    main()

from sys import stdin


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


def main():
    A, B, C, D = [int(x) for x in stdin.readline().rstrip().split()]
    min_c = A // C if A % C == 0 else A // C + 1
    max_c = B // C if B % C == 0 else B // C
    min_d = A // D if A % D == 0 else A // D + 1
    max_d = B // D if B % D == 0 else B // D
    cd = lcm(C, D)
    min_cd = A // cd if A % cd == 0 else A // cd + 1
    max_cd = B // cd if B % cd == 0 else B // cd

    print((B - A + 1) - ((max_c + 1 - min_c) + (max_d + 1 - min_d) - (max_cd + 1 - min_cd)))


if __name__ == "__main__":
    main()

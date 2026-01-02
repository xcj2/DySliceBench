def int_values(slr):
    l, r = map(lambda s: int(s), slr)
    return l, r


def conv_digits(N, digits):
    for i in range(N):
        if digits[i] is None:
            digits[i] = '0' if i > 0 or N == 1 else '1'

    return ''.join(digits)


def main():
    N, M = int_values(input().split())
    digits = [None] * N
    valid = True

    for i in range(M):
        ss = input().split()
        s = int(ss[0])
        c = ss[1]
        if N > 1 and s == 1 and c == '0':
            valid = False
        elif digits[s - 1] is None:
            digits[s - 1] = c
        else:
            valid = digits[s - 1] == c

    if valid:
        print(conv_digits(N, digits))
    else:
        print('-1')


if __name__ == "__main__":
    main()

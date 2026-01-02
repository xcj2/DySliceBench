# https://atcoder.jp/contests/abc150/tasks/abc150_c
# TODO: try


def generate_pattern(pattern, current, n):
    c = current[:]
    remain = n - len(c)
    if remain > 0:
        for i in range(1, n + 1):
            if i not in c:
                c.append(i)
                generate_pattern(pattern, c, n)
                c.pop()
    else:
        pattern.append(c)


def main():
    n = int(input())
    array_a = [int(s) for s in input().split(" ")]
    array_b = [int(s) for s in input().split(" ")]
    pattern = []
    a = -1
    b = -1
    for i in range(n):
        generate_pattern(pattern, [i + 1], n)
    for i, v in enumerate(pattern):
        if array_a == v:
            a = i
        if array_b == v:
            b = i
        if a != -1 and b != -1:
            break
    print(abs(a - b))


def get_num(array, i, n):
    t = abs(array[i - 1] - (i - 1))
    t = t ** (n - i -1)
    return t


if __name__ == '__main__':
    main()

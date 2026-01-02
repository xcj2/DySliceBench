def make_list(a, n):
    res = [1]
    i = 1
    while pow(a, i) <= n:
        res.append(pow(a, i))
        i += 1
    return res[::-1]


def find_withdraw_times(n, w):
    res = 0
    for ww in w:
        res += n // ww
        n %= ww
    return res


def main():
    n = int(input())
    answer = float("inf")
    way_6 = make_list(6, n)
    way_9 = make_list(9, n)
    for i in range(n + 1):
        answer = min(answer, find_withdraw_times(i, way_6) + find_withdraw_times(n - i, way_9))
    print(answer)


if __name__ == '__main__':
    main()


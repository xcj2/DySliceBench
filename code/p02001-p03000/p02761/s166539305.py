n, m = map(int, input().strip().split())
conditions = [list(map(int, input().strip().split()))
              for _ in range(m)]


def check(number):
    str_num = str(number)
    if len(str_num) != n:
        return False
    for s, c in conditions:
        if len(str_num) < s:
            return False
        if str_num[s - 1] != str(c):
            return False

    return True


def check_all():
    for number in range(1000):
        if check(number):
            return number

    else:
        return -1


def main():
    ans = check_all()
    print(ans)


if __name__ == '__main__':
    main()

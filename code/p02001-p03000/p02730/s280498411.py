def check1(s):
    if len(s) % 2 == 1:
        return True
    else:
        return False


def helper(s):
    if len(s) % 2 == 0:
        return _helper_even(s)
    else:
        return _helper_odd(s)


def _helper_odd(s):
    center = int(len(s) / 2)
    s1 = s[:center]
    s2 = s[center + 1:]
    s2 = s2[::-1]

    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            return False
    else:
        return True


def _helper_even(s):
    center = int(len(s) / 2)
    s1 = s[:center]
    s2 = s[center:]
    s2 = s2[::-1]

    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            return False
    else:
        return True


def check2(s):
    if not helper(s):
        return False

    s1 = s[:int((len(s) - 1) / 2)]
    s2 = s[int((len(s) + 3) / 2) - 1:]

    if not helper(s1):
        return False
    if not helper(s2):
        return False

    return True


def main():
    s = input().strip()

    if check1(s) and check2(s):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-


def rli():
    return list(map(int, input().split()))


def check2(s):
    l = len(s) // 2
    if len(s) % 2 == 0:
        if s[:l] != s[:l-1:-1]:
            return False
    else:
        if s[:l] != s[:l:-1]:
            return False
    return True


def check(s):
    l = len(s) // 2
    if s[:l] != s[:l:-1]:
        return False
    if check2(s[:l]) and check2(s[l+1:]):
        return  True
    return False


def main():
    s = input()
    if check(s):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()

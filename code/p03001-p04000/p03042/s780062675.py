#!/usr/bin/python3
# vim: set fileencoding=utf-8:

import sys


def main():
    S = input()
    AA = int(S[:2])
    BB = int(S[2:])

    ay = is_year(AA)
    am = is_month(AA)
    by = is_year(BB)
    bm = is_month(BB)

    ans = "Error"
    if (ay and bm) == True and (by and am) == False:
        ans = "YYMM"
    elif (ay and bm) == False and (by and am) == True:
        ans = "MMYY"
    elif (ay and bm) == True and (by and am) == True:
        ans = "AMBIGUOUS"
    else:
        ans = "NA"

    print(ans)


def is_year(num):
    return True


def is_month(num):
    ret = False
    if 1 <= num <= 12:
        ret = True

    return ret


if __name__ == "__main__":
    main()

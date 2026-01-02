#!/usr/bin/env python3

def main():
    S = input()
    zenhan = int(S[0] + S[1])
    kouhan = int(S[2] + S[3])

    judgeZenhan = judge12(zenhan)
    judgeKouhan = judge12(kouhan)

    print(judgeFormat(judgeKouhan, judgeZenhan))


def judgeFormat(judgeKouhan, judgeZenhan):
    if judgeZenhan and judgeKouhan:
        return 'AMBIGUOUS'
    elif judgeZenhan and not judgeKouhan:
        return 'MMYY'
    elif not judgeZenhan and judgeKouhan:
        return 'YYMM'
    else:
        return 'NA'


def judge12(num):
    if num < 13 and num > 0:
        return True
    return False


if __name__ == "__main__":
    main()

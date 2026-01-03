from enum import Enum


class Judge(Enum):
    OK        = 1
    END_ODD   = 2
    END_INF   = 3


def judge_cookie(X):
    if X % 2 == 0:
        result = True
    else:
        result = False

    return result


def devide_cookie(X):
    return X//2


def exchange_cookie(A, B, C):
    if judge_cookie(A) and judge_cookie(B) and judge_cookie(C):
        # OK
        AA = devide_cookie(B) + devide_cookie(C)
        BB = devide_cookie(A) + devide_cookie(C)
        CC = devide_cookie(A) + devide_cookie(B)

        if A == AA and B == BB and C == CC:
            result = Judge.END_INF
        else:
            result = Judge.OK

    else:
        # NG
        AA = BB = CC = 0
        result = Judge.END_ODD

    return result, AA, BB, CC


A, B, C = map(int, input().split())

Count = 0
while True:
    J, AA, BB, CC = exchange_cookie(A, B, C)
    if J == Judge.OK:
        Count += 1
        A = AA
        B = BB
        C = CC
    elif J == Judge.END_INF:
        Ans = -1
        break
    else:
        Ans = Count
        break

print(Ans)

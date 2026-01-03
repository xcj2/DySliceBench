def check_jp(passed, A, B):
    return passed < A + B


def check_foreign(passed, A, B, passed_b):
    return passed < A + B and passed_b < B


def resolve():
    N, A, B = map(int, input().split())
    S = list(input())

    passed = 0
    passed_b = 0
    for i, p in enumerate(S):
        if p == "a":
            if check_jp(passed, A, B):
                print("Yes")
                passed += 1
            else:
                print("No")
        elif p == "b":
            if check_foreign(passed, A, B, passed_b):
                print("Yes")
                passed += 1
                passed_b += 1
            else:
                print("No")
        else:
            print("No")

resolve()
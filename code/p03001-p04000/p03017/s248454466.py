import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, A, B, C, D = [int(x) for x in input().split()]
    S = input().strip()

    def rock_check(start, end):
        for a, b in zip(S[start:end], S[start + 1:end]):
            if a == b == "#":
                return False
        else:
            return True

    def three_space_check(start, end):
        start -= 2
        end += 1
        for a, b, c in zip(S[start:end], S[start + 1:end], S[start + 2:end]):
            if a == b == c == ".":
                return True
        else:
            return False

    bfirst = False
    if C < D:
        bfirst = True

    if bfirst:
        if A > B:
            if rock_check(B, D) and rock_check(A, C) and three_space_check(A, C):
                print("Yes")
            else:
                print("No")
        else:
            if rock_check(B, D) and rock_check(A, C):
                print("Yes")
            else:
                print("No")
    else:
        if B > A:
            if rock_check(B, D) and rock_check(A, C) and three_space_check(B, D):
                print("Yes")
            else:
                print("No")
        else:
            if rock_check(B, D) and rock_check(A, C):
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    main()

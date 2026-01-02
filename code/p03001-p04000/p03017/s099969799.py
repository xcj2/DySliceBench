import sys
sys.setrecursionlimit(10 ** 7)


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def SI(): return input()


def main():
    _, A, B, C, D = LI()
    S = SI()

    M = [0 for _ in range(A)]
    a = 0
    for s in S[A:max(C, D)]:
        if s == ".":
            a = 0
            M.append(0)
        else:
            if a == 1:
                print("No")
                return
            a = 1
            M.append(1)
    if D > C:
        print("Yes")
        return
    if M[B-2] == 0 and M[B] == 0:
        print("Yes")
        return
    if M[D-2] == 0 and M[D] == 0:
        print("Yes")
        return
    a = 0
    for m in range(B-1, D):
        if M[m-1]+M[m]+M[m+1] == 0:
            print("Yes")
            return
    print("No")


main()

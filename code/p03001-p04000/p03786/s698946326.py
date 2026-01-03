# coding: utf-8
def getLnInputs():
    return input().split()


def getLnIntInputs():
    return list(map(int, getLnInputs()))


def main():
    N = getLnIntInputs()[0]
    A = sorted(getLnIntInputs())

    eatables = []
    eatables_sum = 0

    for c in range(N):
        if len(eatables) <= c:
            eatables.append(A[c])
            eatables_sum += A[c]

        for idx in range(len(eatables), N):
            s = A[idx]
            if s > 2 * eatables_sum:
                break
            eatables.append(s)
            eatables_sum += s

        if len(eatables) == N:
            print(N - c)
            break

    return


main()

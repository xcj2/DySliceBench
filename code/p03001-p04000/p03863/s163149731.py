import sys

def check(S):
    even = set()
    odd = set()
    for i in range(len(S)):
        if i % 2 == 0:
            odd.add(S[i])
        else:
            even.add(S[i])

    return len(even) == len(odd) == 1


def can_checkmate(S):
    chrs = set(S)
    if len(chrs) != 3:
        return False

    for c in chrs:
        S_ = S
        S_.remove(c)
        if check(S_):
            return True

    return False


def main():
    input = sys.stdin.readline
    S = [c for c in input().strip()]

    if check(S):
        return 'Second'

    if S[0] == S[-1]:
        if len(S) % 2 == 0 or can_checkmate(S):
            return 'First'

        else:
            return 'Second'
    else:
        if len(S) % 2 == 1:
            return 'First'

        else:
            return 'Second'


if __name__ == '__main__':
    print(main())

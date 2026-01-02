from collections import Counter  # https://note.nkmk.me/python-scipy-connected-components/
import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    def main():
        N = int(input())
        D = list(map(int, input().split()))
        M = int(input())
        T = list(map(int, input().split()))

        DD = Counter(D)
        TT = Counter(T)

        for key, value in TT.items():
            if DD[key] < value:
                return 'NO'
        return 'YES'

    print(main())


resolve()
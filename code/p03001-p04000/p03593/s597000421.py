# ノートに考察メモあり。
from collections import Counter, deque  # https://note.nkmk.me/python-scipy-connected-components/
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()


def resolve():
    def main():
        gg = Counter([])
        H, W = map(int, input().split())
        grid = [[_ for _ in input()] for _ in range(H)]
        for g in grid:
            gg.update(Counter(g))

        if H % 2 == 0 and W % 2 == 0:
            for i in gg.values():
                if i % 4 != 0:
                    return 'No'
            return 'Yes'

        elif H % 2 == 0 and W % 2 == 1:
            cnt = 0
            for i in gg.values():
                if i % 4 == 2:
                    cnt += 2
                elif i % 4 == 1 or i % 4 == 3:
                    return 'No'

            if cnt <= H:
                return 'Yes'
            else:
                return 'No'

        elif H % 2 == 1 and W % 2 == 0:
            cnt = 0
            for i in gg.values():
                if i % 4 == 2:
                    cnt += 2
                elif i % 4 == 1 or i % 4 == 3:
                    return 'No'

            if cnt <= W:
                return 'Yes'
            else:
                return 'No'

        else:
            cnt1 = 0
            cnt2 = 0
            for i in gg.values():
                if i % 4 == 1:
                    cnt1 += 1
                elif i % 4 == 2:
                    cnt2 += 2
                elif i % 4 == 3:
                    cnt2 += 2
                    cnt1 += 1
            if cnt1 == 1 and cnt2 <= (H + W - 2):
                return 'Yes'
            else:
                return 'No'

    print(main())


resolve()
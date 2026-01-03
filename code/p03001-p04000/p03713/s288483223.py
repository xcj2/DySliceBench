import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    def main():
        H, W = map(int, input().split())
        if H % 3 == 0 or W % 3 == 0:
            return 0
        else:
            ans = 10**18

            for h in range(H):
                A = h*W
                B = ((H-h)//2)*W
                C = (H-h-(H-h)//2)*W
                ans = min(max(A, B, C) -
                          min(A, B, C), ans)

                B = (W//2)*(H-h)
                C = (W-(W//2))*(H-h)
                ans = min(max(A, B, C) -
                          min(A, B, C), ans)

            for w in range(W):
                A = w*H
                B = ((W-w)//2)*H
                C = (W-w-(W-w)//2)*H
                ans = min(max(A, B, C) -
                          min(A, B, C), ans)

                B = (H//2)*(W-w)
                C = (H-(H//2))*(W-w)
                ans = min(max(A, B, C) -
                          min(A, B, C), ans)
            return ans
    print(main())


resolve()
import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
MOD = 10 ** 9 + 7

def main(): 
    N, Q = LI()
    STX = []
    for _ in range(N):
        STX.append(LI())
    D = []
    for _ in range(Q):
        D.append(II())

    STX.sort(key=lambda x:x[2])

    ans = [-1] * Q
    skip = [-1] * Q

    from bisect import bisect_left
    for s, t, x in STX:
        left = bisect_left(D, s-x)  # s-x を超える最小のdの位置
        right = bisect_left(D, t-x)  # t-x を超える最小のdの位置

        while left < right:
            if skip[left] == -1:  # 未踏
                ans[left] = x
                skip[left] = right  # つぎにここにきた際は、rightまで見るのをスキップしてよい。
                left += 1
            else:  # 来たことがある
                left = skip[left]  # 以前覚えておいた right まで見るのをスキップする。

    for i in ans: print(i)

main()
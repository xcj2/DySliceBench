def main():
    """
    端の最適解は決定している
        idx= 0~ 1:sumがx以下になるようにがA[ 1]を減らす、それでもx以下にならないならA[ 0]を減らす
        idx=-2~-1:sumがx以下になるようにがA[-2]を減らす、それでもx以下にならないならA[-1]を減らす

        -> 左端は決定しているので右端まで減らす
        -> 右端から行っても減らす数は変わらない
        -> 端から2番目を優先に減らせばどちらでもよい？
    """
    N, x = map(int, input().split())
    A = list(map(int, input().split()))

    ans = f(N, x, A)
    print(ans)


def f(N, x, A):
    ans = 0
    for i in range(1, N):
        s = sum(A[i - 1:i + 1])
        if s > x:
            # 引き過ぎない
            n = min(s - x, A[i])
            A[i] -= n
            ans += n

            s = sum(A[i - 1:i + 1])
            if s > x:
                n = min(s - x, A[i - 1])
                A[i - 1] -= n
                ans += n

    return ans


def WA(N, x, A):
    ans = 0
    for i in range(N // 2):
        s = sum(A[i:i + 2])
        if x <= s:
            n = s - x
            A[i + 1] -= n
            ans += n

            s = sum(A[i:i + 2])
            if x <= s:
                n = s - x
                A[i] -= n
                ans += n

        if i == 0:
            # slice(-2, 0) -> []
            s = sum(A[-2:])
        else:
            s = sum(A[-(i + 2):-i])
        if x <= s:
            n = s - x
            A[-(i + 2)] -= n
            ans += n

            if i == 0:
                s = sum(A[-2:])
            else:
                s = sum(A[-(i + 2):-i])
            if x <= s:
                n = s - x
                A[-(i + 1)] -= n
                ans += n

    return ans

if __name__ == '__main__':
    main()

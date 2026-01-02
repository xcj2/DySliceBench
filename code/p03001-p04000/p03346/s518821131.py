def main():
    N = int(input())
    P = [int(input()) for _ in range(N)]

    #f1(N, P)
    editorial(N, P)


def editorial(N, P):
    """
    入力例3
        N=8
        P=63127485
         |6   7 8 |
         | 3   4 5|
         |  12    |
        上記の3つの列は要素ai+1=aiである部分列
            連続する列が長いほど、移動しなくて済む要素は多い
            連続するためには、最小未満は左・最大より大きいものは末尾に移動する
        部分列(wikipediaより)
            残った要素がもとの数列における相対的な序列を保つ
            与えられた列からいくつかの要素を取り去ることによって得られる列
    ksomemo様にお借りしました
    """
    if N == 1:
        print(0)
        return

    # WA(N, P)
    a = [0] * (N+1)
    for i, p in enumerate(P):
        a[p] = i

    tmp = 1
    max_len = 1
    for i in range(1, N):
        if a[i] < a[i+1]:
            tmp += 1
            max_len = max(max_len, tmp)
        else:
            tmp = 1
    ans = N - max_len
    print(ans)


def WA(N, P):
    tmp = 0
    ans = 0
    for i, p in enumerate(P):
        if i == 0 or P[i-1] + 1 == p:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 1

    print(N - ans)


if __name__ == '__main__':
    main()

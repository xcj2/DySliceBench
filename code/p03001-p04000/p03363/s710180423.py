def main():
    """
    Aの空でない連続する部分列であって、
    その総和が 0になるものの個数を求めてください。
    ただし、ここで数えるのは 部分列の取り出し方 であることに注意してください。
    つまり、ある2つの部分列が列として同じでも、
    取り出した位置が異なるならば、それらは別々に数えるものとします。

    制約
        1 ≤ N ≤ 2×10^5
        −10^9 ≤ Ai ≤ 10^9
    """
    N = int(input())
    *A, = map(int, input().split())

    f2(N, A)


def f1(N, A):
    """
    愚直にやる場合: O(N^2),TLE
    0-0,0-1,0-2,...0-N_1
        1-1,1-2,...1-N_1
                ...
                   N_2-N_1
                   N_1-N_1
    """
    ans = 0
    for i in range(N):
        s = 0
        for j in range(i, N):
            s += A[j]
            print(i, j, s, sep="\t")
            if s == 0:
                ans += 1

    print(ans)


def f2(N, A):
    """
    累積和をとるだけではO(N^2)
    i=0,ループ
    i=1,ループs[i]-A[0]

    i=0,s[i]-0    ->          0の個数
    i=1,s[i]-s[0] -> -A[0]     の個数
    i=2,s[i]-s[1] -> -A[0]+A[1]の個数

    i=0
        A:0,1,-1
        s:0,1,0
    i=1
        A:1,-1,1
        s0:1,0,1
        s1:x,-1,0

        →自身が含まれるので-1してカウント
        →本来は、ずらしながらカウントするので消費したら-1
        Nループだけ,O(N)
    """
    s = [None] * N
    s[0] = A[0]
    for i in range(1, N):
        s[i] = s[i-1] + A[i]

    from collections import Counter
    c = Counter(s)
    ans = c[0]
    for i in range(1, N):
        ans += c[s[i]] - 1
        c[s[i]] -= 1

    print(ans)


if __name__ == '__main__':
    main()

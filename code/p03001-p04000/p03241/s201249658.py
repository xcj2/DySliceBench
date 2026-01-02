def main():
    """
    input:
        1 <= N <= 10^5
        N <= M <= 10^9

        a1 + a2 + ... + aN = M
        1 <= ai

    output:
        数列の項の最大公約数の最大値
    """
    N, M = map(int, input().split())

    # ans = f(N, M)
    ans = editorial(N, M)
    print(ans)


def f(N, M):
    """
    最大公約数1:
        1が含まれる
        互いに素

    最大公約数2:
        すべて2の倍数

    N=M: すべて1
    M=奇数: 最大公約数は奇数
    まず1ずつ配る
        M -= N

    N,M: 0は偶数、1は奇数
    0 0: 配ってもMは偶数のまま
    0 1: 配ってもMは奇数のまま
         1余るので配る時に２回分配る、余りはどれかに割り当てて偶数にする
    1 0: 奇数回目の配るときには奇数、偶数回目のときは偶数
    1 1: 配ってもMは奇数のまま、01と同じパターン

    """
    if N == 1:
        return M

    if N == M or M < N * 2:
        return 1

    # 1回は確実に配れる
    ans = 1
    d = 1
    M -= M
    while M >= N:
        # 配る
        M -= N
        d += 1

        # 残りをいい感じに分配したときに、今まで配った回数の最大公約数を維持できるか?
        if True:
            ans = d

    return ans


def editorial(N, M):
    """
    すべての項がK倍なら、最大公約数は最低でもKであり、それらの和であるMもKの倍数
    Mの約数は、M=A*B=B*A の対称性より
        最大 root(10^9) まで試せば良いのでTLEしない
    N=1,M=10^9のとき、最初の考えではTLEになる
    """
    ans = 1
    a_max = int(M ** 0.5)
    for a in range(1, a_max + 1):
        if M % a != 0:
            continue

        # aで割り切れるので、もう片方も試す
        b = M // a

        # e.g. N=5, M=120, a=15, M = (N + x) * a,  xは正負ゼロどれか
        # 15 + 15 + 15 + 15 + 15 = 15 * 5 = 75, rest=45 = 15 * 3
        # a * N はaの倍数、Mもaの倍数、より残りもaの倍数なのでどれかの項に配ればよい
        if a * N <= M:
            ans = max(ans, a)
        if b * N <= M:
            ans = max(ans, b)

    return ans


if __name__ == '__main__':
    main()

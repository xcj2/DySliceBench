# 解説を見た

def solve(N: int, M: int, V: int, P: int, A: 'list[int]') -> int:
    """
    入れてよい票 < M*V
        M*V投票するとjを超えるスコアを持つ問題数がP以上になり、不可能

    入れてよい票 >= M*V
        可能

        次の条件を満たせば可能といえる
        # 各問題への投票数は許容範囲内
        # すべてのjudgeがV投票
        # すべてのjudgeが同じ問題に2度以上投票していない
        投票してよい問題abc...zを
        許容される投票数だけ連続させた列(最大M=すべてのjudgeが投票した場合)
        aaaabbbcc...z
        仮定より長さMV以上なので,
        冒頭の区間(長さMV)に対し,judgeを0...M-1,0...M-1,...と割り当てることができる
        この割り当ては,3つの条件を満たす
    """

    from itertools import accumulate

    def is_ok(j):
        if j < P:
            return True
            # P位以内にM回加点

        X = A[j] + M  # 加点後のj位のスコアX
        if X < A[P]:
            return False
            # A[j]にM回加点、P位に加点なしでも勝てん

        return (j - P) * X - (acc[j - 1] - acc[P - 1]) >= M * (V - (P + N - j))
        # return (P - 1 + 1 + N - j) * M + sum(X - A[k] for k in range(P, j)) >= M * V
        # (P-1)位以内,j位以降にM回加点
        # P位～(j-1)位は,加点後のj位を超えない範囲で加点
        # X>=A[P]>=A[k]
        # なので,各kに対し,0点以上加点できる
        # 移項して,累積和でオーダーを落とした

    def binary_search():
        ok = 1
        ng = N + 1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    *A, = sorted(A, reverse=True)
    A = [0] + A  # 0-indexed -> 1-indexed
    acc = tuple(accumulate(A))
    return binary_search()


def main():
    import sys
    input = sys.stdin.readline

    N, M, V, P = map(int, input().split())
    A = map(int, input().split())
    print(solve(N, M, V, P, A))


if __name__ == '__main__':
    main()

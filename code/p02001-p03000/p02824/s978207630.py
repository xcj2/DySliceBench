def solve(N: int, M: int, V: int, P: int, A: 'list[int]') -> int:
    from itertools import accumulate

    def is_ok(j):
        from math import ceil

        X = A[j]
        always_add = (P - 1) + 1 + j  # この区間は、すべてのjudgeから加算を受ける

        if V <= always_add:
            return A[N - P] <= X + M

        flat_distribute_block = N - always_add  # A[j]+Mを超過しないように分配する区間
        count_per_judge = V - always_add  # 各judgeが加点する問題数

        block_sum = acc[N - P + 1] - acc[j + 1]  # [j+1,N-P](0-indexed)
        without_exceed = A[N - P] * flat_distribute_block - block_sum  # A[N-P]を超過せずに処理できる投票数
        vote_piled_up = M * count_per_judge - without_exceed

        if vote_piled_up <= 0:
            return A[N - P] <= X + M
        else:
            to_add = ceil(vote_piled_up / flat_distribute_block)
            return A[N - P] + to_add <= X + M

    def binary_search():
        ok = N - 1
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    *A, = sorted(A)
    acc = (0,) + tuple(accumulate(A))
    return N - binary_search()


def main():
    import sys
    input = sys.stdin.readline

    N, M, V, P = map(int, input().split())
    A = map(int, input().split())
    print(solve(N, M, V, P, A))


if __name__ == '__main__':
    main()

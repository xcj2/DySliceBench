class Solution:
    def solve(self, N: int, F, P) -> int:

        answer = - 10**10

        def list2int(li) -> int:

            base = 1
            ret = 0
            for b in li:
                ret += base * b
                base *= 2
            return ret

        def int2list(i: int):
            ret = []
            for _ in range(10):
                ret.append(i % 2)
                i //= 2

            return ret

        F_int = [list2int(f) for f in F]

        for j in range(1, 1024):
            s = 0
            for n, f in enumerate(F_int):
                cn = sum(int2list(j & f))
                s += P[n][cn]

            answer = max(answer, s)

        return answer


if __name__ == '__main__':

    # standard input
    N = int(input())
    F = []
    for _ in range(N):
        F.append(list(map(int, input().split())))
    P = []
    for _ in range(N):
        P.append(list(map(int, input().split())))

    # solve
    solution = Solution()
    print(solution.solve(N, F, P))

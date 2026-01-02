class Solver():
    def __init__(self, N, costs, K):
        self.dp = [99999999999] * N
        self.dp[0] = 0
        self.K = K
        self.costs = costs

    def solve(self):
        for i in range(0, len(self.costs)):
            for k in range(1, self.K + 1):
                if i >= k:
                    self.dp[i] = min(
                        self.dp[i - k] + abs(self.costs[i] - self.costs[i-k]), self.dp[i])
        return self.dp[-1]


def main():
    N, K = [int(i) for i in input().split()]
    costs = [int(i) for i in input().split()]
    solver = Solver(N, costs, K)
    print(solver.solve())


if __name__ == "__main__":
    main()

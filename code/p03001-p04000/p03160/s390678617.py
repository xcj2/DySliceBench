class Solver():
    def __init__(self, N, costs):
        self.dp = [-1] * N
        self.dp[0] = 0
        self.costs = costs

    def solve(self):
        for i in range(1, len(self.costs)):
            if i == 1:
                self.dp[i] = abs(self.costs[i]-self.costs[i-1])
                continue
            self.dp[i] = min(self.dp[i - 1] + abs(self.costs[i] - self.costs[i-1]),
                        self.dp[i - 2] + abs(self.costs[i] - self.costs[i-2]))

        return self.dp[-1]


def main():
    N = int(input())
    costs = [int(i) for i in input().split()]
    solver = Solver(N, costs)
    print(solver.solve())


if __name__ == "__main__":
    main()

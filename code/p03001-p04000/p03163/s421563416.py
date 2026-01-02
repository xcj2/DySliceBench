class Solver():
    def __init__(self, N, W, items):
        self.N = N
        self.W = W
        self.items = items

    def solve(self):
        dp = [[0 for _ in range(self.W+1)] for _ in range(self.N+1)]
        for i in range(self.N):
            for w in range(self.W+1):
                if w - self.items[i][0] >= 0:
                    dp[i+1][w] = max(dp[i+1][w], dp[i][w - self.items[i][0]] + self.items[i][1])

                dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])
        return dp[self.N][self.W]


def main():
    N, W = [int(i) for i in input().split()]
    items = [[int(i) for i in input().split()] for _ in range(N)]
    solver = Solver(N, W, items)
    print(solver.solve())


if __name__ == "__main__":
    main()
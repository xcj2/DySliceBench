class Solver(object):
    def __init__(self, N, happy):
        self.dp = [[99999999 for _ in range(3)] for _ in range(N)]
        self.N = N
        self.happy = happy

    def solve(self):
        happy_list = self.happy
        self.dp[0] = happy_list[0]
        for i in range(1, self.N):
            self.dp[i][0] = max(happy_list[i][0] + self.dp[i-1][1],
                                happy_list[i][0] + self.dp[i-1][2])
            self.dp[i][1] = max(happy_list[i][1] + self.dp[i-1][0],
                                happy_list[i][1] + self.dp[i-1][2])
            self.dp[i][2] = max(happy_list[i][2] + self.dp[i-1][0],
                                happy_list[i][2] + self.dp[i - 1][1])
        return max(self.dp[-1])


def main():
    N = int(input())
    happy = [[int(i) for i in input().split()] for _ in range(N)]
    solver = Solver(N, happy)
    print(solver.solve())


if __name__ == "__main__":
    main()
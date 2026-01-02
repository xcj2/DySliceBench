from itertools import product

class DP:
    def __init__(self, value, variety, coins):
        self.value = value
        self.variety = variety
        self.coins = coins
        self.DP = [[0 for _ in range(value + 1)] for _ in range(variety)]
        self.DPinit()

    def DPinit(self):
        for row in self.DP:
            row[1] = 1
        self.DP[0] = [i for i in range(self.value + 1)]

    def DPcomp(self):
        for (m, n) in product(list(range(1, self.variety)),list(range(self.value + 1))):
                self.DP[m][n] = self.numberOfCoin(m, n)

    def numberOfCoin(self, m, n):
        if n >= self.coins[m]:
            return min(self.DP[m - 1][n], self.DP[m][n - self.coins[m]] + 1)
        else:
            return self.DP[m - 1][n]

    def answer(self):
        self.DPcomp()
        return self.DP[self.variety - 1][self.value]


if __name__ == "__main__":
    status = list(map(int,input().split()))
    coins = list(map(int,input().split()))
    dp = DP(status[0],status[1],coins)
    print(dp.answer())
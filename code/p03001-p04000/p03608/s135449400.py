from itertools import permutations
class Solve():
    def __init__(self):
        self.N, self.M, self.R = map(int, input().split())
        self.r = list(map(int, input().split()))
        self.route = [[float('inf') for _ in range(self.N)] for _ in range(self.N)]
        for _ in range(self.M):
            a, b, c = map(int, input().split())
            self.route[a - 1][b - 1] = c
            self.route[b - 1][a - 1] = c
        for i in range(self.N):
            self.route[i][i] = 0

    def WarshallFloid(self):
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    if self.route[i][j] > self.route[i][k] + self.route[k][j]:
                        self.route[i][j] = self.route[i][k] + self.route[k][j]

    def execute(self):
        self.WarshallFloid()
        ans = float('inf')
        checked = set()
        for path in permutations(self.r):
            if tuple(reversed(path)) in checked:
                continue
            checked.add(tuple(reversed(path)))
            temp = 0
            for i in range(self.R - 1):
                temp += self.route[path[i] - 1][path[i + 1] - 1]
            ans = min(ans, temp)
        print(ans)


if __name__ == '__main__':
    Solve().execute()
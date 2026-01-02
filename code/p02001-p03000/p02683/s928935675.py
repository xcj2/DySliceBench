from itertools import combinations

class Solver:
    def __init__(self, N, M, X, C, A):
        self.N = N
        self.M = M
        self.X = X
        self.C = C
        self.A = A

    def is_achievable(self, A):
        result = [0] * self.M
        for a_row in A:
            for i, a in enumerate(a_row):
                result[i] += a

        for n in result:
            if n < self.X:
                return False
        return True

    def solve(self):
        if not self.is_achievable(self.A):
            print(-1)
            return

        min_cost = 10 ** 10
        index_C = [ i for i in range(N) ]
        for i in range(len(index_C)+1):
            for comb in combinations(index_C, i):
                cur_A = []
                cur_cost = 0
                for i in comb:
                    cur_A.append(self.A[i])
                    cur_cost += C[i]
                if self.is_achievable(cur_A):
                    min_cost = min(min_cost, cur_cost)

        print(min_cost)

N, M, X = map(int, input().split())

C = [0] * N
A = []

for i in range(N):
    query = list(map(int, input().split()))
    C[i] = query[0]
    A.append(query[1:])

solver = Solver(N, M, X, C, A)
solver.solve()


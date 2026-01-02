class DP2D(object):

    def __init__(self, item_n: int, border: int, initializer: int = 0):
        self.item_n = item_n
        self.border = border
        self.table = [[initializer for _ in range(self.item_n + 1)] for _ in range(self.border + 1)]

    def __str__(self):
        return "\n".join(list(map(lambda l:
                                  " ".join(list(map(str, l)))
                                  , self.table)))

    def __repr__(self):
        return "DynamicProgramming object:\n" + \
               "item_n: " + str(self.item_n) + ", border: " + str(self.border) + "\n" + \
               "table:\n" + self.__str__()

    def solve(self, expr: callable) -> list:
        raise NotImplementedError

    def fill_0_idx_with(self, value: int) -> "DP2D":
        self.table[0] = [value for _ in range(self.item_n + 1)]
        for i in range(1, self.border + 1):
            self.table[i][0] = value
        return self


class DP2DOptimizer(DP2D):

    def __init__(self, item_n: int, border: int, obj_coef: list, sbj_coef: list, initializer: int = 0):
        super(DP2DOptimizer, self).__init__(item_n, border, initializer=initializer)

        if len(obj_coef) == self.item_n:  # to 1-base
            obj_coef = [0] + obj_coef
        self.obj_coef = obj_coef

        if len(sbj_coef) == self.item_n:
            sbj_coef = [0] + sbj_coef
        self.sbj_coef = sbj_coef

    def solve(self, expr: callable) -> list:
        for weight_lim in range(1, self.border + 1):
            for item_idx in range(1, self.item_n + 1):
                self.table[weight_lim][item_idx] = expr(weight_lim, item_idx)

        return self.table

    def knapsack_expr(self, weight_lim: int, item_idx: int) -> int:
        res = self.table[weight_lim][item_idx - 1]
        if weight_lim - self.sbj_coef[item_idx] >= 0:
            res = max(res, self.table[weight_lim - self.sbj_coef[item_idx]][item_idx] + self.obj_coef[item_idx])
        return res


if __name__ == '__main__':
    N, W = map(int, input().split())
    v, w = [], []
    for _ in range(N):
        buff = [int(i) for i in input().split()]
        v.append(buff[0])
        w.append(buff[1])
    dp = DP2DOptimizer(N, W, v, w)
    print(dp.solve(dp.knapsack_expr)[W][N])


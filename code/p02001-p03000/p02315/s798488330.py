from collections import namedtuple

Item = namedtuple('Item', 'value, weight')


def make_knapsack_resolver(num_items, max_capacity):
    dp = [[0] * (max_capacity + 1) for _ in range(num_items + 1)]
    items = [Item(*[int(x) for x in input().split()]) for _ in range(num_items)]

    def resolve():
        calc_recurrence()
        return dp[0][max_capacity]

    def calc_recurrence():
        for idx_item in range(num_items - 1, 0 - 1, -1):
            for remaining_capacity in range(1, max_capacity + 1):
                if remaining_capacity < items[idx_item].weight:
                    dp[idx_item][remaining_capacity] = dp[idx_item + 1][remaining_capacity]
                else:
                    dp[idx_item][remaining_capacity] = max(
                        dp[idx_item + 1][remaining_capacity],
                        dp[idx_item + 1][remaining_capacity - items[idx_item].weight] + items[idx_item].value
                    )

    return resolve()


if __name__ == '__main__':
    N, W = list(map(int, input().split()))
    resolver = make_knapsack_resolver(N, W)
    print(resolver)


from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    N, M = read_ints()
    # key to cover
    cover = [0]*M
    # key to cost
    costs = [0]*M
    INF = 10**9+1
    for i in range(M):
        a, b = read_ints()
        costs[i] = a
        for c in read_ints():
            cover[i] |= 1<<(c-1)
    # mask to cost
    mask_to_cost = [INF]*(1<<N)
    mask_to_cost[0] = 0
    for mask in range(1<<N):
        for i in range(M):
            mask_to_cost[cover[i]|mask] = min(mask_to_cost[cover[i]|mask], mask_to_cost[mask]+costs[i])
    return mask_to_cost[(1<<N)-1] if mask_to_cost[(1<<N)-1] != INF else -1


if __name__ == '__main__':
    print(solve())

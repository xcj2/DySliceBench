import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def build(l, A):
    # minimum cost for mask to A
    N = len(l)
    mask_to_cost = [math.inf]*(1<<N)
    for m in range(1, 1<<N):
        i = 0
        cost = 0
        length = 0
        while i < N:
            if m&(1<<i):
                cost += 10
                length += l[N-i-1]
            i += 1
        if cost > 0:
            cost -= 10
        cost += abs(length-A)
        mask_to_cost[m] = cost
    for m in range(1<<N):
        s = m
        while s > 0:
            s = (s-1)&m
            mask_to_cost[m] = min(mask_to_cost[m], mask_to_cost[s])
    return mask_to_cost


def solve():
    N, A, B, C = read_ints()
    l = [read_int() for _ in range(N)]
    A_cost = build(l, A)
    B_cost = build(l, B)
    C_cost = build(l, C)
    min_cost = math.inf
    for a_mask in range(1, 1<<N):
        bc_mask = ((1<<N)-1)-a_mask
        b_mask = bc_mask
        while b_mask > 0:
            b_mask = (b_mask-1)&bc_mask
            c_mask = bc_mask-b_mask
            if b_mask and c_mask:
                min_cost = min(min_cost, A_cost[a_mask]+B_cost[b_mask]+C_cost[c_mask])
    return min_cost


if __name__ == '__main__':
    print(solve())

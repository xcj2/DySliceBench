import sys
from queue import Queue


def print_costs(costs):
    for c in costs:
        print(c)


def solve(inp):
    (H, W) = map(int, inp.readline().strip().split(' '))
    S = [list(inp.readline().strip()) for i in range(H)]

    max_cost = 0
    for start_y in range(H):
        for start_x in range(W):
            if S[start_y][start_x] == '#':
                continue
            costs = [[0 for w in range(W)] for h in range(H)]
            costs[start_y][start_x] = 1
            queue = Queue()
            queue.put((start_y, start_x))
            cost = 1
            while not queue.empty():
                (y, x) = queue.get()
                # print("({},{}): {}".format(y, x, c))
                for (next_y, next_x) in [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]:
                    if 0 <= next_y < H and 0 <= next_x < W and S[next_y][next_x] == '.' and costs[next_y][next_x] == 0:
                        costs[next_y][next_x] = costs[y][x] + 1
                        if cost < costs[next_y][next_x]:
                            cost = costs[next_y][next_x]
                        queue.put((next_y, next_x))
            if cost > max_cost:
                max_cost = cost
            # print("--- cost={}".format(max_cost))
            # print_costs(costs)
            # print()

    return str(max_cost - 1)


def main():
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    main()

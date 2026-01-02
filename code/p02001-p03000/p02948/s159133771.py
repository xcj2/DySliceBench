import heapq


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M = read_ints()
    AB = []
    for _ in range(N):
        AB.append(read_ints())
    AB.sort(reverse=True)
    rewards = []
    total = 0
    for i in range(M):
        while AB and AB[-1][0] <= i+1:
            a, b = AB.pop()
            heapq.heappush(rewards, -b)
        if rewards:
            total += -heapq.heappop(rewards)
    return total


if __name__ == '__main__':
    print(solve())

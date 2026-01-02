import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, K = read_ints()
    P = [p-1 for p in read_ints()]
    C = read_ints()

    max_score = -math.inf
    for i in range(N):
        cycle_score = C[i]
        scores = [0, C[i]]
        j = P[i]
        k = K
        while k > 1 and i != j:
            cycle_score += C[j]
            scores.append(cycle_score)
            j = P[j]
            k -= 1
        cycle_size = len(scores)-1
        cycle_count = K//cycle_size
        max_score = max(max_score, max(scores[1:]))
        if cycle_count != 0:
            max_score = max(max_score,
                            cycle_score*cycle_count+max(scores[:K%cycle_size+1]),
                            cycle_score*(cycle_count-1)+max(scores[1:]))
    return max_score


if __name__ == '__main__':
    print(solve())

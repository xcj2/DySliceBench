from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    N, X, M = read_ints()
    seen = [0]*M
    answer = X
    cycle_length = 1
    cycle_prefix = [0, X]
    N -= 1
    count = 0
    while N > 0:
        next_X = (X**2) % M
        if seen[next_X]:
            cycle_length = count-seen[next_X]+1
            break
        seen[next_X] = seen[X]+1
        cycle_prefix.append(cycle_prefix[-1]+next_X)
        answer += next_X
        N -= 1
        X = next_X
        count += 1
    if N == 0:
        return answer
    answer += (N//cycle_length)*(cycle_prefix[-1]-cycle_prefix[-cycle_length-1])
    N %= cycle_length
    while N > 0:
        X = (X**2) % M
        answer += X
        N -= 1
    return answer


if __name__ == '__main__':
    print(solve())

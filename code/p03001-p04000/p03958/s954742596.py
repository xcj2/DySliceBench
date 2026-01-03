import heapq
from typing import List, Any, Tuple


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    K, T = read_ints()
    A = read_ints()
    cakes: List[List[int]] = [[-A[i], i] for i in range(T)]
    heapq.heapify(cakes)
    last_eaten = -1
    count = 0
    while cakes:
        frequent0 = heapq.heappop(cakes)
        if frequent0[1] == last_eaten:
            if cakes:
                frequent1 = heapq.heappop(cakes)
                last_eaten = frequent1[1]
                frequent1[0] += 1
                if frequent1[0] != 0:
                    heapq.heappush(cakes, frequent1)
            else:
                count += 1
                last_eaten = frequent0[1]
                frequent0[0] += 1
        else:
            frequent0[0] += 1
            last_eaten = frequent0[1]
        if frequent0[0] != 0:
            heapq.heappush(cakes, frequent0)
    return count


if __name__ == '__main__':
    print(solve())

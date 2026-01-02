import math
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    D, G = read_ints()
    p: List[int]= []
    c: List[int]= []
    for _ in range(D):
        pc = read_ints()
        p.append(pc[0])
        c.append(pc[1])
    count = [0]*(1<<D)
    score = [0]*(1<<D)
    for i in range(D):
        count[1<<i] = p[i]
        score[1<<i] = c[i]+(p[i]*100*(i+1))
    for i in range(1, 1<<D):
        submask = i&(i-1)
        submask_complement = i-submask
        count[i] = count[submask]+count[submask_complement]
        score[i] = score[submask]+score[submask_complement]
    min_count = 10**9
    for i in range(1<<D):
        for j in range(D):
            if i&(1<<j) == 0 and score[i] < G and score[i]+score[1<<j] >= G:
                required_count = math.ceil((G-score[i])/((j+1)*100))
                if required_count < count[1<<j]:
                    min_count = min(min_count, required_count+count[i])
                else:
                    min_count = min(min_count, count[1<<j]+count[i])
    return min_count


if __name__ == '__main__':
    print(solve())

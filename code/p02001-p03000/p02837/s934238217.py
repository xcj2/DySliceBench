from collections import namedtuple
from itertools import compress, product

Testimony = namedtuple('Testimony', 'honest_persons unkind_persons')

def bin_iter(num, width=1):
    assert width > 0
    while num > 0 or width > 0:
        yield num & 1
        num >>= 1
        width -= 1

def pop_count(num):
    return sum(bin_iter(num))

def solve(testimonies):
    def is_not_contradicted(honest_persons):
        for testimony in compress(testimonies, bin_iter(honest_persons, len(testimonies))):
            if (testimony.honest_persons | honest_persons) > honest_persons:
                return False
            if testimony.unkind_persons & honest_persons:
                return False
        return True
    return max(map(pop_count, filter(is_not_contradicted, range(1 << len(testimonies)))), default=0)

def main():
    N = int(input())
    testimonies = []
    for _ in range(N):
        honest_persons, unkind_persons = 0, 0
        for _ in range(int(input())):
            x, y = list(map(int, input().split()))
            if y == 1:
                honest_persons |= (1 << (x - 1))
            else:
                unkind_persons |= (1 << (x - 1))
        testimonies.append(Testimony(honest_persons, unkind_persons))
    print(solve(testimonies))

if __name__ == '__main__':
    main()

from collections import Counter


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    """
    H, W = read_ints()
    counter = Counter()
    for _ in range(H):
        counter += Counter(input())
    C = list(counter.values())
    fours = H//2*W//2
    twos = W//2*(H%2)+H//2*(W%2)
    ones = (H%2)*(W%2)
    for c in C:
        while c != 0:
            if c >= 4 and fours > 0:
                fours -= 1
                c -= 4
            elif c >= 2 and twos > 0:
                twos -= 1
                c -= 2
            elif c >= 1 and ones > 0:
                ones -= 1
                c -= 1
            else:
                return 'No'
    return 'Yes'


if __name__ == '__main__':
    print(solve())

from collections import deque


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    K = read_int()
    if K < 10:
        return K
    Q = deque(range(1, 10))
    counter = 10
    while True:
        num = Q.popleft()
        digit = num%10
        for d in range(-1, 2):
            if 0 <= digit+d < 10:
                if counter == K:
                    return num*10+digit+d
                counter += 1
                Q.append(num*10+digit+d)


if __name__ == '__main__':
    print(solve())

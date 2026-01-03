import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M = read_ints()
    students, checkpoints = [], []
    for _ in range(N):
        students.append(read_ints())
    for _ in range(M):
        checkpoints.append(read_ints())
    for s in students:
        min_dist = math.inf
        min_j = math.inf
        for j, c in enumerate(checkpoints, start=1):
            if abs(s[0]-c[0])+abs(s[1]-c[1]) < min_dist:
                min_dist = abs(s[0]-c[0])+abs(s[1]-c[1]) 
                min_j = j
        print(min_j)


if __name__ == '__main__':
    solve()

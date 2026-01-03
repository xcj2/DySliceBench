import sys

# sys.stdin = open('b1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1 - y2)


n, m = read_int_list()
students = [read_int_list() for i in range(n)]
checkpoints = [read_int_list() for j in range(m)]

for student in students:
    dist = 10 ** 20
    res = -1
    for index, checkpoint in enumerate(checkpoints):
        distance1 = distance(student, checkpoint)
        if distance1 < dist:
            dist = distance1
            res = index + 1
    print(res)

import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    H = len(inputs)
    W = len(inputs[0])
    alter = inputs
    count_dot = 0
    reached_alter = []
    for line in alter:
        a = []
        for mass in line:
            if mass == ".":
                count_dot += 1
            a.append(False)
        reached_alter.append(a)
    queue = deque([[0, 0, 0]])

    min = -1
    while len(queue) > 0:
        [x, y, step_num] = queue.popleft()
        if x == -1 or x == W or y == -1 or y == H:
            continue
        if x == W - 1 and y == H - 1:
            min = step_num
            break
        if alter[y][x] == "#" or reached_alter[y][x]:
            continue
        reached_alter[y][x] = True

        queue.append([x - 1, y, step_num + 1])
        queue.append([x + 1, y, step_num + 1])
        queue.append([x, y - 1, step_num + 1])
        queue.append([x, y + 1, step_num + 1])

    if min == -1:
        return -1
    return count_dot - min - 1


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [H, W] = string_to_int(input())
    ret = solve(inputs(H))
    print(ret)

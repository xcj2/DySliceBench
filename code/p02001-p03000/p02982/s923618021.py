import sys
import math

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, D, inputs):
    points = list(map(lambda x: string_to_int(x), inputs))

    count = 0
    for i in range(0, len(points)-1):
        for j in range(i+1, len(points)):
            each_d_sum = 0

            for di in range(0, D):
                each_d_sum += (points[j][di] - points[i][di]) ** 2
            result = math.sqrt(each_d_sum)
            if result.is_integer():
                count += 1
    return count


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N, D] = string_to_int(input())

    ret = solve(N, D, inputs(N))
    print(ret)

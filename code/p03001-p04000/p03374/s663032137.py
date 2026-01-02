import collections


Point = collections.namedtuple('Sushi', ['position', 'value'])


def read_ints():
    return map(int, input().split())


def reverse_points(points, length):
    return [Point(length - p.position, p.value) for p in reversed(points)]


def solve_unidir(points, length):
    forward_peaks = [(-1, 0)]
    forward_accumulated_value = 0
    for i, p in enumerate(points):
        forward_accumulated_value += p.value
        forward_actual_value = forward_accumulated_value - p.position
        if forward_actual_value > forward_peaks[-1][1]:
            forward_peaks.append((i, forward_actual_value))
    best_value = forward_peaks[-1][1]
    backward_accumulated_value = 0
    for i, p in reversed(list(enumerate(points))):
        while forward_peaks[-1][0] >= i:
            forward_peaks.pop()
        backward_accumulated_value += p.value
        backward_actual_value = backward_accumulated_value - 2 * (length - p.position)
        best_value = max(best_value, backward_actual_value + forward_peaks[-1][1])
    return best_value


def solve(points, length):
    return max(solve_unidir(points, length),
               solve_unidir(reverse_points(points, length), length))


def main():
    n, length = read_ints()
    points = []
    for _ in range(n):
        position, value = read_ints()
        points.append(Point(position, value))
    print(solve(points, length))


if __name__ == '__main__':
    main()

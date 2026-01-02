# coding=utf-8


def solve_under_stair(high: float) -> int:
    one_under = int((high + 5) // 5)
    return one_under + 1


def solve_need_time(velocity: float) -> float:
    return velocity / 9.8


def solve_need_height(fall_time: float) -> float:
    return 4.9 * fall_time * fall_time


if __name__ == '__main__':
    while True:
        try:
            v = float(input())
        except EOFError:
            break
        time = solve_need_time(v)
        minimum_height = solve_need_height(time)
        floor_number = solve_under_stair(minimum_height)
        print(floor_number)
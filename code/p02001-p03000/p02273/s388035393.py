import math


def rot60_on_complex_plane(start: complex, end: complex) -> complex:
    v = end - start
    arg = 1 / 2 + complex(0, (math.sqrt(3) / 2))
    return v * arg + start


def print_real_coordinate(z: complex) -> None:
    x = z.real
    y = z.imag
    print(f"{x:.8f} {y:.8f}")


def create_koch_points(p1: complex, p2: complex, n: int) -> None:
    if n == 0:
        return

    # Get s, t, u coordinates on the complex plane.
    s = (p2 - p1) * (1 / 3) + p1
    t = (p2 - p1) * (2 / 3) + p1
    u = rot60_on_complex_plane(s, t)

    # Call the function recursively by the case of n == 0.
    create_koch_points(p1, s, n - 1)
    print_real_coordinate(s)
    create_koch_points(s, u, n - 1)
    print_real_coordinate(u)
    create_koch_points(u, t, n - 1)
    print_real_coordinate(t)
    create_koch_points(t, p2, n - 1)


if __name__ == "__main__":
    n = int(input())
    start_point = (0 + 0j)
    end_point = (100 + 0j)

    print_real_coordinate(start_point)
    create_koch_points(start_point, end_point, n)
    print_real_coordinate(end_point)


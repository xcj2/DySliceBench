import math


def calc_height(b: int, rad: float) -> float:
    h = b * math.sin(rad)
    return h


def calc_area(a: int, h: float) -> float:
    S = a * h / 2
    return S


def calc_lap(a: int, b: int, rad: float) -> float:
    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(rad))
    L = a + b + c
    return L


def calc():
    a, b, deg = map(int, input().split())
    # rad = float(deg * 2 * math.pi / 360)
    rad = math.radians(deg)

    h = calc_height(b, rad)
    S = calc_area(a, h)
    L = calc_lap(a, b, rad)

    print(f"{S:.8f}")
    print(f"{L:.8f}")
    print(f"{h:.8f}")


if __name__ == "__main__":
    calc()


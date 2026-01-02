def answerA():
    a, b = map(int, input().split())
    if a < 10 and b < 10:
        result = a * b
    else:
        result = -1

    print(result)


def answerB():
    def can_be_devided_by_1d(n):
        result = 'No'
        for i in range(1,10):
            floor, mod = divmod(n, i)
            if mod == 0 and floor < 10:
                result = 'Yes'
        return result

    n = int(input())
    print(can_be_devided_by_1d(n))


def answer():
    def make_divisors(n):
        divisors = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.add(i)
                if i != n // i:
                    divisors.add(n // i)
        return divisors

    n = int(input())
    divisors = make_divisors(n)
    candidates = set()

    for i in divisors:
        floor = n // i
        distance = (floor-1) + (i-1)
        candidates.add(distance)

    print(min(candidates))


if __name__ == '__main__':
    answer()

import sys


def PeriodCount(a, mod):
    x = a % mod
    count = 1

    while x != 1:
        x = a * x % mod
        count += 1

    return count


def GreatestCommonDiviser(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2

    return num1


def LeastCommonMultiple(num1, num2):
    return num1 * num2 / GreatestCommonDiviser(num1, num2)


for line in sys.stdin:
    line = line[:-1]

    if line == "0 0 0 0 0 0":
        break

    inputNum = [int(item) for item in line.split(" ")]
    counts = [PeriodCount(inputNum[lp * 2], inputNum[lp * 2 + 1])
              for lp in range(3)]

    lcm = LeastCommonMultiple(counts[0], counts[1])
    lcm = LeastCommonMultiple(lcm, counts[2])

    print(int(lcm))


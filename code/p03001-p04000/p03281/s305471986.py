# -*- coding: utf-8 -*-

def main():
    a = int(input())
    minNum = 3 * 5 * 7
    if a < minNum:
        print(0)
        return
    elif a <= minNum + 1:
        print(1)
        return

    count = 1
    if a % 2 == 1:
        a = a + 1
    for n in range(minNum + 2, a, 2):
        if countDevisor(n) == 8:
            count = count + 1

    print(count)


def factorize(num):
    facts = []
    n = num
    base, expo = 2, 0
    while base * base <= n:
        while n % base == 0:
            n = n // base
            expo = expo + 1
        if expo > 0:
            facts.append((base, expo))
        base = base + 1
        expo = 0

    if n > 1:
        facts.append((n, 1))

    return facts


def countDevisor(num):
    facts = factorize(num)
    count = 1
    for _, expo in facts:
        count = count * (expo + 1)
    return count


if __name__ == '__main__':
    main()

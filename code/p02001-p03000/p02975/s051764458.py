# AGC035A - XOR Circle_2.py
import sys

STDIN = 1
number = 1
elements = [[0]]

sample = """
3
1 2 3
"""

example = """
3
1 1 4
5 1 4
8 1 0
"""

if bool(sample.strip().splitlines()) or bool(STDIN):
    if bool(STDIN):
        number = int(sys.stdin.readline().strip())


        def pick():
            return sys.stdin.readline().strip()

    else:
        stack = sample.strip().splitlines()[::-1]
        number = int(stack.pop().strip())


        def pick():
            return stack.pop().strip()

    elements = list(map(int, pick().split()))

elif bool(number):
    i = 0
    for amp in (sample, example):
        i, j = i + 1, 0
        for p in (amp, amp.strip()):
            j += 1
            print("{}-{} = {}".format(i, j, repr(p)))
            print(p.split())
            print(p.splitlines())

##############################################################################

numbers = tuple(elements)
kinds = set(numbers)


def yes():
    print("Yes")
    sys.exit()


if kinds == {0}:
    yes()

elif len(kinds) == 2:
    if 0 in kinds:
        if numbers.count(0) * 3 == number:
            yes()

elif len(kinds) == 3:
    a, b, c = tuple(kinds)
    if a ^ b == c:
        if (numbers.count(a) == numbers.count(b)) and (numbers.count(b) == numbers.count(c)):
            yes()

print("No")

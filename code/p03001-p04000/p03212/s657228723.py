import itertools

def main():
    n = int(input())
    c = 0
    for m in gen():
        if m > n:
            break

        if is_753(m):
            c += 1

    print(c)

def is_753(n):
    s = str(n)
    if '3' in s and '5' in s and '7' in s:
        return True
    else:
        return False

def gen():
    for i in itertools.count(1):
        for x in gen_1(i):
            yield x

def gen_1(num_digits):
    if num_digits == 1:
        yield 3
        yield 5
        yield 7
    else:
        for sub in gen_1(num_digits - 1):
            yield sub * 10 + 3
            yield sub * 10 + 5
            yield sub * 10 + 7

main()

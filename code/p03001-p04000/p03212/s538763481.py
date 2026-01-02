def n_numbers(n: int) -> int:
    ret = 0
    while True:
        n = n // 10
        ret += 1
        if n <= 0:
            break
    return ret

def gen_numbers(n: int) -> int:
    if n <= 1:
        yield 3
        yield 5
        yield 7
    else:
        for g in gen_numbers(n-1):
            for m in ["3","5","7"]:
                yield int(m + str(g))

def validate(n: int) -> bool:
    three = False
    five = False
    seven = False
    while True:
        k = n % 10
        if k == 3:
            three = True
        elif k == 5:
            five = True
        elif k == 7:
            seven = True
        n = n // 10
        if three and five and seven:
            return True
        if n <= 1:
            break
    return False


n = int(input())

k = n_numbers(n)

if k < 3:
    print(0)
else:
    ret = 0
    for i in range(3, k+1):
        for target in gen_numbers(i):
            if target <= n and validate(target):
                ret += 1
    print(ret)
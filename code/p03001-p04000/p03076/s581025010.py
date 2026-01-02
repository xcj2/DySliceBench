def stupid(a):
    from itertools import permutations
    ret = float('inf')
    for p in permutations(a):
        time = 0
        for dish in p:
            time += (10 - (time % 10)) % 10
            time += dish
        ret = min(ret, time)
    return ret

def fast(a):
    temp = a[::]
    temp.sort(key=lambda x: (10 - (x % 10)) % 10)
    ret = 0
    for dish in temp:
        ret += (10 - (ret % 10)) % 10
        ret += dish
    return ret

def stress(n):
    from random import randint
    for _ in range(n):
        a = [randint(1, 123) for _ in range(5)]
        expected = stupid(a)
        got = fast(a)
        if got != expected:
            raise Exception('%s -> expected:%d, got:%d' % (' '.join(map(str, a)), expected, got))

test = False
if test:
    stress(1000)
else:
    a = [int(input()) for _ in range(5)]
    print(fast(a))
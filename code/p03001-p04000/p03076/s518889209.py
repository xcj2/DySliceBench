###############################################################################

from bisect import bisect_left as binl

def intin():
    input_tuple = input().split()
    if len(input_tuple) <= 1:
        return int(input_tuple[0])
    return tuple(map(int, input_tuple))


def intina():
    return [int(i) for i in input().split()]


def intinl(count):
    return [intin() for _ in range(count)]


def modadd(x, y):
    global mod
    return (x + y) % mod


def modmlt(x, y):
    global mod
    return (x * sy) % mod


def lcm(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


###############################################################################


def main():
    timelist = intinl(5)

    min_broken = 10
    min_i = None

    for i, time in enumerate(timelist):
        broken = time % 10
        if broken and broken < min_broken:
            min_broken = min(broken, min_broken)
            min_i = i

    new_timelist = []
    for time in timelist:
        if time % 10:
            time += (10 - time % 10)
        new_timelist.append(time)


    if min_i is None:
        print(sum(new_timelist))
    else:
        del new_timelist[min_i]
        time = timelist.pop(min_i)
        print(sum(new_timelist) + time)


if __name__ == '__main__':
    main()

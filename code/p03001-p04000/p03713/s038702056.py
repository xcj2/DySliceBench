
def read_input():
    h, w = map(int, input().split())

    return h, w

def short_divide(h, w):
    long_side = max(h, w)
    short_side = min(h, w)

    short1 = short_side // 3
    short2 = (short_side - short1) // 2
    short3 = short_side - short1 - short2

    block1 = short1 * long_side
    block2 = short2 * long_side
    block3 = short3 * long_side

    return max(block1, block2, block3) - min(block1, block2, block3)


def long_divide(h, w):
    long_side = max(h, w)
    short_side = min(h, w)

    long1 = long_side // 3
    long2 = (long_side - long1) // 2
    long3 = long_side - long1 - long2

    block1 = long1 * short_side
    block2 = long2 * short_side
    block3 = long3 * short_side

    return max(block1, block2, block3) - min(block1, block2, block3)


def long_first(h, w):
    long_side = max(h, w)
    short_side = min(h, w)

    mindiff = float('inf')

    for i in range(1, long_side):
        long_block = i * short_side

        long_rest = long_side - i
        short_short_side = short_side // 2
        short_long_side = short_side - short_short_side

        short_short_block = short_short_side * long_rest
        short_long_block = short_long_side * long_rest

        maxarea = max(long_block, short_short_block, short_long_block)
        minarea = min(long_block, short_short_block, short_long_block)

        if mindiff > maxarea - minarea:
            mindiff = maxarea - minarea

    return mindiff


def short_first(h, w):
    long_side = max(h, w)
    short_side = min(h, w)

    mindiff = float('inf')

    for i in range(1, short_side):
        short_block = i * long_side

        short_rest = short_side - i
        long_short_side = long_side // 2
        long_long_side = long_side - long_short_side

        long_short_block = long_short_side * short_rest
        long_long_block = long_long_side * short_rest

        maxarea = max(short_block, long_short_block, long_long_block)
        minarea = min(short_block, long_short_block, long_long_block)

        if mindiff > maxarea - minarea:
            mindiff = maxarea - minarea

    return mindiff



def submit():
    h, w = read_input()

    if h % 3 == 0 or w % 3 == 0:
        print(0)
        return

    print(min(long_first(h, w), short_first(h, w), long_divide(h, w), short_divide(h, w)))

if __name__ == '__main__':
    submit()
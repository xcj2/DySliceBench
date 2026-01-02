t = []
H = 0
W = 0

def is_bomb(h, w):
    if 0 <= h and h < H and 0 <= w and w < W:
        if t[h][w] == '#':
            return 1

    return 0


def count_bomb(h, w):
    global t

    num = 0
    if is_bomb(h - 1, w - 1):
        num += 1

    if is_bomb(h - 1, w):
        num += 1

    if is_bomb(h - 1, w + 1):
        num += 1

    if is_bomb(h, w + 1):
        num += 1

    if is_bomb(h + 1, w + 1):
        num += 1

    if is_bomb(h + 1, w):
        num += 1

    if is_bomb(h + 1, w - 1):
        num += 1

    if is_bomb(h, w - 1):
        num += 1

    t[h][w] = str(num)
        

def do_main():
    global H, W, t

    H, W = list(map(int, input().rstrip().split()))

    t = []

    for i in range(H):
        t.append(list(input().rstrip()))

    for h in range(H):
        for w in range(W):
           if t[h][w] != '#':
                count_bomb(h, w) 


    for h in range(H):
        print(''.join(t[h]))


do_main()

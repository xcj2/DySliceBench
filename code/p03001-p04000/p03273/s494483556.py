coord = []


def compress_y():
    global coord
    for y in range(len(coord)):
        if all(c == '.' for c in coord[y]):
            coord = coord[:y] + coord[y + 1:]
            return True
    return False


def compress_x():
    global coord
    for x in range(0, len(coord[0])):
        if all(row[x] == '.' for row in coord):
            for y in range(len(coord)):
                coord[y] = coord[y][:x] + coord[y][x + 1:]
            return True
    return False


def main():
    global coord
    h, w = map(int, input().split())
    coord = [list(input()) for _ in range(h)]
    while compress_y():
        pass
    while compress_x():
        pass

    for row in coord:
        print(''.join(row))


if __name__ == '__main__':
    main()
